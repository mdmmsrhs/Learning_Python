#!/bin/python

class Time():
	""" Time object has attributes: hour, minute and second """
	def __init__(self):
	      self.hour = 0
	      self.minute = 0
	      self.second = 0
	      
class Time(object):
    """
    Time object has attributes: hour, minute, second.  
    Rewritten to make it easier to instantiate.
    """
    
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second	      

def printTime(t):
	""" Function to print a time object to screen """
	h = t.hour
	m = t.minute
	s = t.second
	print "Time is: ",h,":",m,":",s

def is_after(t1,t2):
	"""compare times as tuples to return a logical value, because this evaluates the 
		paired elements in each tuple for TRUE from left to right in turn, moving to 
		the next element in line if the first returns FALSE"""
	return (t2.hour,t2.minute,t2.second) > (t1.hour,t1.minute,t1.second)
	""" PS this is how you define a function to return a logical value"""

def is_am(t):
	""" Tests whether the time is in the morning """
	return(t.hour < 12)

def is_pm(t):
	""" Tests whether time is in the afternoon """
	return(t.hour >=12)
					
def oldAddTime(t1,t2):
	""" function  to add two times together"""
	sum = Time()
	sum.hour = t1.hour + t2.hour
	sum.minute = t1.minute + t2.minute
	sum.second = t1.second + t2.second
	return sum
	
def addTime(t1,t2):
	""" function  to add two times together"""
	sum = Time()
	sum.hour = t1.hour + t2.hour
	sum.minute = t1.minute + t2.minute
	sum.second = t1.second + t2.second
	
	if sum.second >= 60:
		sum.second -= 60
		sum.minute += 1
		
	if sum.minute >= 60:
		sum.minute -= 60
		sum.hour += 1

	return sum
	
def increment(time,second):
	""" function  to add second to time, the while loops substitute
	for the if expressions for cases where time.second is MUCH more
	than 60.  It is correct but inefficient"""
	time.second += second
	
	while time.second >= 60:
		time.second -= 60
		time.minute += 1
		
	while time.minute >= 60:
		time.minute -= 60
		time.hour += 1

	return time	
	
#######################################################################################
# This block partly inspired by http://www.greenteapress.com/thinkpython/code/Time2.py
#######################################################################################

def timeInt(time):
	""" converts a time object to an integer corresponding
	to the number of second since midnight """
	mins = int(time.minute + time.hour*60)
	secs = int(mins*60 + time.second)
	return secs
	
def intTime(secs):
	""" converts an integer corresponding to second since 
	midnight into a Time object """
	time = Time()
	minute, second = divmod(secs, 60)
	hour, minute = divmod(minute, 60)
	time.hour = hour
	time.minute = minute
	time.second = second
	return time

def increment2(time,second):
	""" A more efficient method for incrementing time without 
	while loops using the intTime and timeInt functions as inter-
	mediate stages to obviate the >60 problem """
	tempTime = timeInt(time)
	incInt = tempTime + second
	incTime = intTime(incInt)
	return incTime
	
#######################################################################################
# This block partly inspired by http://www.greenteapress.com/thinkpython/code/Time2.py
#######################################################################################
# this is also increment as a PURE FUNCTION
#######################################################################################

def duration(time1,time2):
	duration = intTime((timeInt(time2)) - (timeInt(time1)))
	return duration

def main():
	
  # Instantiate a Time() object
  time = Time()
  time.hour = 11
  time.minute = 15
  time.second = 30
  
  printTime(time)
  
  time2 = Time(11,14,15)
#  time2.hour = 11
#  time2.minute = 14
#  time2.second = 45
  
  print(is_after(time,time2))
  print(is_am(time))
  print(is_pm(time))
  
  newtime = addTime(time,time2)
  printTime(newtime)
  
  print(is_pm(newtime))
  
  currentTime = Time()
  currentTime.hour = 9
  currentTime.minute = 15
  currentTime.second = 40
  
  breadTime = Time()
  breadTime.hour = 3
  breadTime.minute = 30
  breadTime.second = 30
  
  doneTime = addTime(currentTime,breadTime)
  print "Time now: "
  printTime(currentTime)
  print "Time bread is ready: "
  printTime(doneTime)
  
  baseTime = Time()
  baseTime.hour = 1
  baseTime.minute = 10
  baseTime.second = 10
  incTime = (increment(baseTime,100))
  printTime(incTime)
  
  baseTime = Time()
  baseTime.hour = 1
  baseTime.minute = 10
  baseTime.second = 10
  printTime(baseTime)
  secs = timeInt(baseTime)
  print(secs)
  rebaseTime = intTime(secs)
  printTime(rebaseTime)
  biggerTime = increment(rebaseTime,60)
  printTime(biggerTime)
  
  t3 = duration(baseTime,biggerTime)
  printTime(t3)

if __name__ == '__main__':
  main()

#end



	