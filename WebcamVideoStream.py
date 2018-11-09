import cv2 
from threading import Thread


class WebcamVideoStream:
	def __init__(self , src=0):
		self.stream=cv2.VideoCapture(src)
		(self.grabbed , self.frame)=self.stream.read()
		self.stopped=False				 									

	def update(self):
		while True:

			if self.stopped:
				self.stream.release()
				return 

			else:
			
				(self.grabbed , self.frame)=self.stream.read()

	def read (self):
		return self.frame
			
	def startThread(self):
		Thread(target=self.update).start()
		return self 

	def stop(self):
		self.stopped=True




