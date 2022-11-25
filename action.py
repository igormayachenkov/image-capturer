import cv2

def processSource(src, dst):
    print("src:", src)


def doAction(config):
    sources     = config["sources"]
    dst         = config["destination"]
    print("===== DO ACTION =====")
    print("OpenCV version",cv2.__version__)

    for src in sources:
        try:
            processSource(src, dst)
        except Exception as e:
            print('SOURCE PROCESSING ERROR:',type(e),e)




