#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from textwrap import wrap



def callbackdrive(data):
	mydata = str(data.data)
	if len(mydata) == 18:
		edit(mydata)
	

def callbackarm(data):
	mydata = str(data.data)
	if len(mydata) == 26:
		edit(mydata)


def edit(data):
	if mydata[0] == 'A' and mydata[-1] == 'B':
		datanum1 = str(mydata[1:-1])
		septdata1 = int(wrap(datanum1,4))

		for i in septdata1:
			if septdata[i] > 1000:
				if septdata[i] > 1255:
					septdata[i] = 255
				septdata[i] = septdata[i] - 1000
				
			elif septdata[i] < 1000:
				if 255 < septdata[i] < 1000:
					septdata[i] = -255
				septdata[i] = -septdata[i]
			
			lastdata1[i] = str(septdata1[i])
				

	return lastdata1



def listen():
	rospy.init_node('listen', anonymous=True)
	rospy.Subscriber("serial/drive", String, self.callbackdrive)
	rospy.Subscriber("serial/robotic_arm", String, self.callbackarm)
	rospy.spin()


def publish():
	rospy.init_node('publish', anonymous=True)
	pubdrive = rospy.Publisher("position/drive", String, queue_size = 10)
    pubarm = rospy.Publisher("position/robotic_arm", String, queue_size = 10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
    	rospy.loginfo(lastdata1)


if __name__ == "__main__":
	listen()
	publish()
