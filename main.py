import extractimagefromvideo as extr
import imageLabelDetect as detect
import detect_blur as isblur

filenameInput = 'bird.mp4'
cutAtTimeInSecond = 3000
filenameOutput = "test.jpg"
output = extr.extractAt(cutAtTimeInSecond, filenameInput, filenameOutput)
# isblur.detect_blur()
print(detect.findTags(output))

