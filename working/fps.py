import datetime
class FPS:
    def __init__(self):
        self._start=None
        self._end=None
        self._numframes=0
        self._returnVal=0

    def start(self):
        self._start=datetime.datetime.now()
        return self

    def stop(self):
        self._end=datetime.datetime.now()
        return self 

    def updateFrames(self):
        self._numframes+=1
        return self 

    def elapsed(self):
        return(self._end-self._start).total_seconds()

    def fps(self):
        self._returnVal=self._numframes
        self._numframes=0;
        return (self._returnVal/self.elapsed())


    
