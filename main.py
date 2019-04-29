import extractimagefromvideo as extr
import imageLabelDetect as detect
import detectBlurForFile as isblur

filenameInput = 'videos/bird.mp4'
cutAtTimeInSecond = 3000
filenameOutput = "test.jpg"
output = extr.extractAt(cutAtTimeInSecond, filenameInput, filenameOutput)
isblur.detect_blur(output)
# print(detect.findTags(output))
print(detect.findTags(isblur.detect_blur(output)[1]))

