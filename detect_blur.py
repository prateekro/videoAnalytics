# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
import argparse
import cv2
import sys
import time

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

countBlurImages = 0
countCorrectImages = 0
# loop over the input images
for imagePath in paths.list_images(args["images"]):
	start_time = time.time()
	# load the image, convert it to grayscale, and compute the
	# focus measure of the image using the Variance of Laplacian
	# method
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	text = "Not Blurry"

	countCorrectImages += 1

	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
	if fm < args["threshold"]:
		text = "Blurry"
		countCorrectImages -= 1
		countBlurImages += 1

	# show the image
	cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	# if text == "Blurry":
	# 	cv2.imshow("Image", image) #Show image in  new window

	sys.stdout.write('\r') # Reset the counter
	sys.stdout.write("Correct: "+ str(countCorrectImages) + "\tBlur: "+ str(countBlurImages) +"\tCompleted processing: " + str(countCorrectImages+countBlurImages))
	sys.stdout.flush()
	key = cv2.waitKey(0)

print("--- %s seconds ---" % (time.time() - start_time))


