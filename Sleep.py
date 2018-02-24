
#sleep cycles

import time
import math
def TimeSet():
	HourI = int(raw_input("Hour you go to sleep:"))
	MinuteI= int(raw_input("Minute:"))	
	
	print "Time you sleep:%dh-%dm"%(HourI,MinuteI)
	
	print "You should go to bed at later time:"
	for x in range(1,6):
		MinuteR=MinuteI+x*(104)
		HourO=HourI+MinuteR/60
		MinuteO=MinuteR%60
		if(HourO>=24):
			HourO-=24
		print "- %dh-%dm"%(HourO,MinuteO)
def TimeFixed():

	HourI = int(raw_input("You want to wake up at hour:"))
	MinuteI= int(raw_input("Minute:"))		

	HourT=0
	print "You should go to bed at later time:"	
	for x in xrange(1,6):
		MinuteR=MinuteI-x*(104)
		while (MinuteR<0):
			MinuteR+=60
			HourT+=1
			# 00
		HourO=HourI-HourT	
		if (HourO<0):
			HourO=24-abs(HourI-HourT)
		print "- %dh-%dm"%(HourO,abs(MinuteR)) 
		HourT=0
print "================================"	
print "Do you want choice about thing?"
localtime = time.asctime( time.localtime(time.time()) )
print "Time now:",localtime
print "1:Do you want sleep in time?"
print "2:Do you want wake up? "
print "0:Exit"
print "================================"
while (1):
	choice=int(raw_input('you choice:'))
	if (choice==1):
		TimeSet()
	if (choice==2):
		TimeFixed()
	if(choice==0):
		exit()

	
