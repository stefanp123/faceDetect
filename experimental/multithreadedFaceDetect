from threading import Thread 
import threading
import cv2 
import Queue 
import time 

lock1=threading.Lock()
lock2=threading.Lock()
queue1=Queue.LifoQueue()
queue2=Queue.LifoQueue()

class imageProcessor:
		def __init__(self):
			self._newimg=0
			self._tempimg=0
			self._classifier=cv2.CascadeClassifier('faceclassifier.xml')
			self._stop=False
			self._numFrames=0
			
			

		def processImage (self):
			while queue1.empty():
					time.sleep(0.005)
			while not queue1.empty():
					lock1.acquire()
					self._newimg=queue1.get()
					lock1.release()
					self._tempimg=cv2.cvtColor(self._newimg , cv2.COLOR_BGR2GRAY)
					faces=self._classifier.detectMultiScale(self._tempimg , 1.3 , 5)
					for (x , y , w , h) in faces:
						cv2.rectangle(self._newimg , (x , y) , (x+w , y+h) , (255 , 0 , 0) , 2)
					lock2.acquire()
					queue2.put(self._newimg)
					lock2.release()
					self._numFrames+=1

					if self._stop:
						break 


		def retFPS(self):
			return int(self._numFrames)

		def startThread (self):
			Thread(target=self.processImage).start()	
			return self

		def stopThread (self):
			self._stop=True 

class WebCamThread:
	def __init__(self , cam=0):
		self._camera=cv2.VideoCapture(cam)
		(self._grabbed , self._frame)=self._camera.read()
		self._run=True

		

	def update(self):
		while self._run:
			(self._grabbed , self._frame)=self._camera.read()
			lock1.acquire()
			queue1.put(self._frame)
			lock1.release()
		self._camera.release()

	def startThread (self):
		Thread(target=self.update).start()	
		return self

	def stopThread (self):
		self._run=False




cam=WebCamThread()
processor1=imageProcessor()
processor2=imageProcessor()


cam.startThread()
processor1.startThread()
processor2.startThread()
start=time.time()

while True:
	if not queue2.empty():
		returnimage=queue2.get()
		stop=time.time()
		cv2.putText(returnimage, "FPS:"+str(int(((processor1.retFPS()+processor2.retFPS())/(stop-start)))) , (450 , 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)
		cv2.imshow('frame' , returnimage)
		if chr(cv2.waitKey(1)&255)=='q':
			break 


processor1.stopThread()
processor2.stopThread()
cam.stopThread()

cv2.destroyAllWindows()

