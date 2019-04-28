import cv2

filenameInput = 'bird.mp4'
cutAtTimeInSecond = 3000
filenameOutput = "test.jpg"
def extractAt(cutAtTimeInSecond, filenameInput, filenameOutput="test.jpg"):
    cap = cv2.VideoCapture(filenameInput)
    cap.set(cv2.CAP_PROP_POS_MSEC,cutAtTimeInSecond)      # Go to the 1 sec. position
    ret,frame = cap.read()                   # Retrieves the frame at the specified second
    cv2.imwrite(filenameOutput, frame)          # Saves the frame as an image
    # cv2.imshow("Frame Name",frame)           # Displays the frame on screen
    # cv2.imshow(filenameInput+" @ "+str(cutAtTimeInSecond),frame)           # Displays the frame on screen
    cv2.waitKey()                            # Waits For Input
    return filenameOutput
