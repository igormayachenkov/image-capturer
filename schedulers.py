class Scheduler:
    def parseTime(self,str):
        # parse the time in format "hh:mm" or "mm:ss"
        parts = str.split(':')
        hh = int(parts[0])
        ll = int(parts[1])
        time = 60*hh + ll #the formula is suitable for all periodicity values
        print(parts,hh,ll,time)
        return  time

class Hourly (Scheduler):
    def timeOfInterval(self, dt)       : return 60*dt.minute + dt.second
    def isNewInterval(self, last, now) : return last.hour != now.hour 
    def getTimerSleepTime(self)        : return 60 # 1 min

class Daily (Scheduler):
    def timeOfInterval(self, dt)       : return 60*dt.hour + dt.minute
    def isNewInterval(self, last, now) : return last.day != now.day 
    def getTimerSleepTime(self)        : return 900 # 15 min
