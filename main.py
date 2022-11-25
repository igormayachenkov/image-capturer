import time
import datetime
import json

# datetime https://www.w3schools.com/python/python_datetime.asp

print("============ image-capturer =============")

# last = datetime.datetime(2022,11,24,  19,00)
last = None

def loadConfig():
    f = open('image-capturer-config.json')  # Opening JSON file
    config = json.load(f) # returns JSON object as a dictionary
    f.close() # Closing file
    #print(config)
    return config

class Hourly:
    def timeOfInterval(self, dt)       : return 60*dt.minute + dt.second
    def isNewInterval(self, last, now) : return last.hour != now.hour 

class Daily:
    def timeOfInterval(self, dt)       : return 60*dt.hour + dt.minute
    def isNewInterval(self, last, now) : return last.day != now.day 

def checkSchedule(scheduler, times,now):
    if last==None : timeLast = None
    else:           timeLast = scheduler.timeOfInterval(last)
    timeNow  = scheduler.timeOfInterval(now)
    print("timeNow, timeLast", timeNow, timeLast)
    for t in times:
        # parse the time in format "hh:mm"
        parts = t.split(':')
        h = int(parts[0])
        m = int(parts[1])
        timeSched = 60*h + m #the formula is suitable for all periodicity values
        print(parts,h,m,timeSched)
        if timeLast!=None and timeLast>=timeSched : continue #this time has been played already
        if timeNow > timeSched : return True
    return False

def doAction():
    print("doAction")
    global last
    last = datetime.datetime.now()
  
def onTimer():
    global last

    # Load config
    config = loadConfig()
    periodicity = config["schedule"]["periodicity"]
    times       = config["schedule"]["times"]
    if periodicity=="hourly" : scheduler = Hourly()
    if periodicity=="daily"  : scheduler = Daily()

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
        doAction()

# THE LOOP
while True:
    onTimer()
    time.sleep(60)

#onTimer()
