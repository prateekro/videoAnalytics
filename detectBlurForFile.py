# USAGE
# python detect_blur.py --images images

# import the necessary packages
import os

from imutils import paths
# import argparse
import cv2
import sys
import time

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", required=True,
# 	help="path to input directory of images")
# ap.add_argument("-t", "--threshold", type=float, default=100.0,
# 	help="focus measures that fall below this value will be considered 'blurry'")
# args = vars(ap.parse_args())

# loop over the input images
# for imagePath in paths.list_images(args["images"]):


def imageProcessor(imagePath, threshold):
	# load the image, convert it to grayscale, and compute the
	# focus measure of the image using the Variance of Laplacian
	# method
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	text = "Blurry"

	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"

	if fm > threshold:
		text = "Not Blurry"
		return imagePath

	return None


def detect_blur(imagesFolder, threshold = 100.0):
	start_time = time.time()
	notBlurList = []
	if len(str(imagesFolder).split(".")) == 2:
		print(str(imagesFolder).split(".")[1], " ::PNG FOUND")
		if imageProcessor(imagesFolder, threshold) != None:
			# print("Test: ", imagesFolder.split("/")[-1])
			notBlurList.append(imagesFolder.split("/")[-1])

	for imagePath in paths.list_images(imagesFolder):
		if imageProcessor(imagePath, threshold) != None:
			# print("Test: ", imagePath.split("\\")[-1])
			# notBlurList.append(imagePath.split("\\")[-1])
			notBlurList.append(imagePath.split("/")[-1])

	print("--- %s seconds ---" % (time.time() - start_time))
	print(notBlurList)
	return notBlurList, imagesFolder

# print (detect_blur(os.path.join(os.path.dirname(__file__)+'/image_data_set/dogimages/image_010.png')))
print (detect_blur(os.path.join(os.path.dirname(__file__)+'/image_data_set/dogimages/')))
# print(os.path.join(os.path.dirname(__file__),'image_data_set/dogimages'))  #/image_010.png
