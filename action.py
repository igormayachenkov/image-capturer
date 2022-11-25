import os
import cv2

def processSource(src, dst):
    print("process:", src)

    # VERIFY/CREATE dir
    output = dst+"/"+src["dir"]
    print("output:", output)
    if not os.path.exists(output) :
        os.mkdir(output)
        print("dir created:", output)



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




