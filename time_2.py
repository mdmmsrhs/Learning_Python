#!/bin/python
# 27/11/2015 15:20:43 Richard Stephens

""" All functions converted to methods, watch out for syntax when calling,
intTime() left as function since it wouldn't work as method for some reason
(probably because it doesn't take a time object as an argument')
Need to pay close attention to indents and the syntax by which methods call
other methods """

class Time():
    """ Time object has attributes: hour, minute and second """
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

class Time:
    """
    Time object has attributes: hour, minute, second.  
    Rewritten to make it easier to instantiate.
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def printTime(self):
        """ Function to print a time object to screen """
        h = self.hour
        m = self.minute
        s = self.second
        print "Time is: ",h,":",m,":",s
    
    def is_after(self,t2):
        """compare times as tuples to return a logical value, because this
        evaluates the paired elements in each tuple for TRUE from left
        to right in turn, moving to the next element in line if the first
        returns FALSE"""
        
        return (t2.hour,t2.minute,t2.second) > (self.hour,self.minute,
        \self.second)
        """ PS this is how you define a function to return a logical value"""
    
    def is_am(self):
        """ Tests whether the time is in the morning """
        return(self.hour < 12)
    
    def is_pm(self):
        """ Tests whether time is in the afternoon """
        return(self.hour >=12)
        
    def timeInt(self):
        """ converts a time object to an integer corresponding
        to the number of second since midnight """
        mins = (self.minute + self.hour*60)
        secs = (mins*60 + self.second)
        return secs
    

    
    def addTime(self,t2):
        """ function  to add two times together"""
        sum_int = (self.timeInt() + t2.timeInt())
        sum = intTime(sum_int)
        return sum
        
#def addTime(self,t2):
#    """ function  to add two times together"""
#    sum = Time()
#    sum.hour = self.hour + t2.hour
#    sum.minute = self.minute + t2.minute
#    sum.second = self.second + t2.second
#    
#    if sum.second >= 60:
#        sum.second -= 60
#        sum.minute += 1
#        
#    if sum.minute >= 60:
#        sum.minute -= 60
#        sum.hour += 1
#
#    return sum
    
    def increment(self,seconds):
        """ A more efficient method for incrementing time without 
        while loops using the intTime and timeInt functions as inter-
        mediate stages to obviate the >60 problem """
        seconds += self.timeInt()
        return intTime(seconds)
    
    def duration(self,time2):
        duration = intTime(time2.timeInt() - self.timeInt())
        return duration

def intTime(self):
    """ converts an integer corresponding to second since 
    midnight into a Time object """
    time = Time()
    minute, second = divmod(self, 60)
    hour, minute = divmod(minute, 60)
    time = Time(hour,minute,second)
    return time

def main():

    #Instantiate a Time() object
    time = Time(11,15,50)
    
    time.printTime()
    
    time2 = Time(11,14,15)
    
    time2.printTime
    
    print(time2.is_after(time))
    print "placeholder \n"
    print(time.is_am())
    print(time.is_pm())
    
    newTime = time.addTime(time2)
    newTime.printTime()
    
    print(newTime.is_pm())
    
    currentTime = Time()
    currentTime.hour = 9
    currentTime.minute = 15
    currentTime.second = 40
    
    breadTime = Time()
    breadTime.hour = 3
    breadTime.minute = 30
    breadTime.second = 30
    
    doneTime = currentTime.addTime(breadTime)
    print "Time now: "
    currentTime.printTime()
    print "Time bread is ready: "
    doneTime.printTime()
    
    baseTime = Time()
    baseTime.hour = 1
    baseTime.minute = 10
    baseTime.second = 10
    incTime = (baseTime.increment(100))
    incTime.printTime()
    
    baseTime = Time(1,10,10)
    baseTime.printTime()
    secs = baseTime.timeInt()
    print(secs)
    rebaseTime = intTime(secs)
    rebaseTime.printTime()
    biggerTime = rebaseTime.increment(60)
    biggerTime.printTime()
    
    t3 = baseTime.duration(biggerTime)
    t3.printTime()

if __name__ == '__main__':
    main()

#end



