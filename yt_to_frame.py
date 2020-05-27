import os
import re
import cv2
import time
def video_to_frames_url_auto(url, folder='../../../../../Desktop/'):
    """Function to extract frames from input video url or file and save them as separate frames
    in an output directory. Output directory will be named starting from video_1. If a new file is downloaded,
    a video_2 folder will be created and so on.
    Dependencies:
        OpenCV
        youtube-dl (sudo pip install --upgrade youtube_dl)

    Args:
        url: Youtube video URL.
        folder: Directory to download and save each frames.

    Returns:
        None

    Work to be done:
    1. Handle exceptions
    """


    # Log start time
    time_start = time.time()

    # To make a directory for saving video automatically considering all the existing foldernames
    reg = re.compile(r'^video_')
    lst = sorted(os.listdir(folder))
    newlist = filter(reg.match, lst)
    numbers = [reg.sub('', x).strip() for x in newlist]
    results = map(int, numbers)
    results = sorted(results)

    # Make a directory for the video
    # If no video's exist as of now, create a folder.
    if(len(results) == 0):
        os.mkdir(folder+"video_1")
        newfile = 1
    else:
        newfile = int((results[-1]) + 1)
        os.mkdir(folder+"video_" + str(newfile))
    # Create a folder according to the files that are already present.
    file_loc = folder + "video_" + str(newfile) + "/video_" + str(newfile) + ".mp4"
    # Download from local video file
    if (url):
        print("Downloading Youtube Video")
        os.system("youtube-dl -o " + file_loc + " -f mp4 " + url)
        cap = cv2.VideoCapture(file_loc)
    else:
        print("This is where I should raise an error. --EXCEPTION HANDLING--")
    cap = cv2.VideoCapture(file_loc)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    while cap.isOpened():
        print(count)
        ret,frame = cap.read()

        cv2.imwrite(folder + "video_" + str(newfile) + "/%d.jpg" % (count+1), frame)
        count = count + 1
        if (count > (video_length-1)):
            time_end = time.time()
            cap.release()
            print ("Done extracting frames.\n%d frames extracted" %count)
            print("It took %d seconds for conversion." %(time_end-time_start))
            break
