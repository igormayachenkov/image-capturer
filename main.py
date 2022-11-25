import time
import datetime
import json
import schedulers
from action import doAction

# datetime https://www.w3schools.com/python/python_datetime.asp

print("============ image-capturer =============")

last = None

def loadConfig():
    f = open('/etc/image-capturer-config.json')  # Opening JSON file
    config = json.load(f) # returns JSON object as a dictionary
    f.close() # Closing file
    #print(config)
    return config

def checkSchedule(scheduler, times,now):
    if last==None : timeLast = None
    else:           timeLast = scheduler.timeOfInterval(last)
    timeNow  = scheduler.timeOfInterval(now)
    print("timeNow, timeLast", timeNow, timeLast)
    for t in times:
        timeSched = scheduler.parseTime(t)
        if timeLast!=None and timeLast>=timeSched : continue #this time has been played already
        if timeNow > timeSched : return True
    return False
  
def onTimer():
    global last

    # Load config
    config = loadConfig()
    periodicity = config["schedule"]["periodicity"]
    times       = config["schedule"]["times"]
    if periodicity=="hourly" : scheduler = schedulers.Hourly()
    if periodicity=="daily"  : scheduler = schedulers.Daily()

    # Fix the current time
    now = datetime.datetime.now() #format like: 2022-11-24 18:14:24.447269
    # print(d,d.strftime("%d"))
    print('----------------------------------------')
    print('now ', now)
    print('last',last)

    # clear last time if new interval started
    if last!=None :
        if scheduler.isNewInterval(last,now) :
            last = None  

    if checkSchedule(scheduler, times, now) : 
    # if True : 
        last = now
        try:
            doAction(config)
        except Exception as e:
            print('LOOP ERROR:',type(e),e)

    
    # rerurn the next sleep time
    return scheduler.getTimerSleepTime()

# THE LOOP
while True:
    sleeptime = onTimer()
    print('next sleep time',sleeptime)
    time.sleep(sleeptime)

#onTimer()
