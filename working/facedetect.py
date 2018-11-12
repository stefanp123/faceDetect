
from WebcamVideoStream import WebcamVideoStream
import cv2
from fps import FPS

faceCascade = cv2.CascadeClassifier('faceclassifier.xml') 
bodyCascade = cv2.CascadeClassifier('bodyclassifier.xml')
cam=WebcamVideoStream() 
cam.startThread()  
fps=FPS()



        


while True:

    img=cam.read()
    fps.start()
    gray=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray , 1.3 , 5)
    
    for (x , y , w , h) in faces :
        cv2.rectangle(img , (x, y) , (x+w , y+h) , (255 , 0 , 0) , 2)
    
    fps.stop()
    cv2.putText(img , 'FPS:'+str(int(fps.fps())), (450 , 60) , cv2.FONT_HERSHEY_COMPLEX ,1.5,(255,255,255),2,cv2.LINE_AA)
    fps.updateFrames()
    cv2.imshow("frame" , img)



    if chr(cv2.waitKey(1)&255)=='q':
        break 


cam.stop() 
    



cv2.destroyAllWindows()
