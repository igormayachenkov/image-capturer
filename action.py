import os
import cv2
import pafy  #documentation: https://pypi.org/project/pafy/
import datetime

def processSource(src, dst):
    print("process:", src)

    # VERIFY/CREATE output dir
    output = dst+"/"+src["dir"]
    if not os.path.exists(output) :
        os.mkdir(output)
        os.chmod(output,777) #to allow remove files by ftp
        print("created:", output)

    # CAPTURE IMAGE
    url = src["url"]
    #url = 'https://youtu.be/LXb3EKWsInQ' #Costa Rica - doesn't work!
    video = pafy.new(url)
    print("title  :", video.title)
    best  = video.getbest()
    print("video  :", best.resolution, best.extension)
    #print("best.url !!!:", best.url) #https://manifest.googlevideo.com/api/manifest/....
    capture = cv2.VideoCapture(best.url) #cv2.VideoCapture object
    result, frame = capture.read()
    print ("result :",result)
    capture.release()

    # SAVE IMAGE
    if result :
        output = output+"/"+datetime.datetime.now().strftime("%y%m%d-%H%M%S.jpg")
        cv2.imwrite(output, frame)
        print("output :", output)

def doAction(config):
    sources     = config["sources"]
    dst         = config["destination"]
    print("===== DO ACTION =====")
    print("OpenCV version",cv2.__version__)

    # VERIFY DESTINATION
    if not os.path.exists(dst) :
        raise Exception("destination path does not exist")

    # PROCESS SOURCES
    for src in sources:
        try:
            processSource(src, dst)
        except Exception as e:
            print('SOURCE PROCESSING ERROR:',type(e),e)




