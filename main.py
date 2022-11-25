import time
import datetime
import json

# datetime https://www.w3schools.com/python/python_datetime.asp

print("============ image-capturer =============")

last = datetime.datetime(2022,11,24,  19,00)
#last = None
print('last',last)

def loadConfig():
    f = open('image-capturer-config.json')  # Opening JSON file
    config = json.load(f) # returns JSON object as a dictionary
    f.close() # Closing file
    #print(config)
    return config

def checkSchedule(now, times):
    if last==None : minutesLast = None
    else:           minutesLast = 60*last.hour + last.minute
    minutesNow  = 60*now.hour  + now.minute
    print("minutesNow, minutessLast", now, minutesNow, minutesLast)
    for t in times:
        # parse the time in format "hh:mm"
        parts = t.split(':')
        h = int(parts[0])
        m = int(parts[1])
        minutes = 60*h + m
        print(parts,h,m,minutes)
        if minutesLast!=None and minutesLast>=minutes : continue #this time has been played already
        if minutesNow > minutes : return True
    return False
  
def onTimer():
    # Load config
    config = loadConfig()
    times = config["schedule"]["times"]

    # Fix the current time
    now = datetime.datetime.now() #format like: 2022-11-24 18:14:24.447269
    # print(d,d.strftime("%d"))

    doAction=checkSchedule(now,times)
    print("doAction",doAction)


# THE LOOP

# while True:
#     onTimer()
#     time.sleep(1)

onTimer()
