import extractimagefromvideo as extr
import imageLabelDetect as detect

filenameInput = 'bird.mp4'
cutAtTimeInSecond = 3000
filenameOutput = "test.jpg"
output = extr.extractAt(cutAtTimeInSecond, filenameInput, filenameOutput)
print(detect.findTags(output))

