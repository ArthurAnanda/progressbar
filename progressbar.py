import time as TI

class ProgressBar:
    def __init__(self):
        self.scale=100
        self.loopLen=100
        self.timeStart=0


    def printBar(self,i):
        m=int(self.loopLen/self.scale)
        inow=int(i/m)
        c = ((inow+1) / self.scale) * 100
        a = '>' * inow
        b = '-' * (self.scale - inow)
        dur = TI.perf_counter() - self.timeStart
        timeM = (self.scale - inow + 2) / (max(1, inow))
        lasttime = dur * timeM
        print('\r{:>3.0f}%[{}{}] :{:>3.0f} seconds'.format(c, a, b, lasttime), end='')

    def confirmCompleted(self):
        a = '>' * self.scale
        print('\r{:>3.0f}%[{}{}] completed'.format(100, a, ''), end='\n')

    def barSet(self,scale,loopLen):
        self.scale=scale
        self.loopLen=loopLen
        self.timeStart=TI.perf_counter()

loopLen=1000
bar=ProgressBar()
bar.barSet(scale=100,loopLen=loopLen)
print('Start looping:')
for i in range(loopLen):
    TI.sleep(0.00001)
    bar.printBar(i)
bar.confirmCompleted()

