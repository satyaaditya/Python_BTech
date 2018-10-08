import threading
import time


class myThread (threading.Thread):
   def __init__(self, startt, end, arr,listt):
      self.count = 0
      threading.Thread.__init__(self)
      # self.summ = summ
      self.startt =  startt
      self.end = end
      self.arr = arr

   def run(self):
      global summ
      while(self.startt<self.end) :
          lock.acquire()
          self.count+= self.arr[self.startt]
          self.startt+=1
          lock.release()
      listt.append(self.count)
# Create new threads
if __name__== "__main__":
    thread= []
    arr= xrange(100)
    arr1 =  [0]*10
    listt = []
    for i in range(10):
        thread.append(myThread(i*10,i*10+10,arr,listt))


    lock = threading.Lock()
    # Start new Threads
    i=0
    while i < 10:
        thread[i].start()
        i+=1
    i=0

    while i < 10:
        thread[i].join()
        i+=1
    print "Exiting Main Thread"
    print sum(listt)