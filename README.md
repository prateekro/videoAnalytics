# videoAnalytics

##### Run
>
> `py main.py`

---
##### To-Do

Add a video in the command with argument `-v "path/videofilename"`

Add an image in command with argument `-i "path/imagename"`

Add an image folder to detect blurs/correct files `-blur "path/imageset_folder"`

## Objective
Merge all modules and detect the objects in the video.

 - Divide video into one second bracket
 - Find one frame / image in the 1 second (or a time-interval) bracket by checking the blur score.
 (The more the score the better the output would be.) [Probably one more check after blur check -- think about the image correctness possible features for better detction - like histogram and sharness]
 - Send that frame to cloud and check the tags associated and show top 5 result.
    - Find object in the frame - possibly trace object with a rectangle using open-cv 
    - Request and caching needs to be nearly real-time and object tracing should make it easier to make it simulate like a real time usage on finding frame tags. 
    
## Ambition
 1. Try to make the traced rectangle / box clickable on the video && pause video and read on popup / go to link 
 1. Define the meaning to each new defined object.
