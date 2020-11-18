import threading
import time
import random
import queue

BUF_SIZE = int(input('Buffer size: '))
q = queue.Queue(BUF_SIZE)
req = int(input('Requests: '))
t0 = time.time()
class ProducerThread(threading.Thread):

    def run(self):
        while (True):
            if not q.full():
                item = random.randint(1,BUF_SIZE)
                q.put(item)
            
        return

class ConsumerThread(threading.Thread):

    def run(self):
        global req
        global t0
        a = 0
        
        while (True):
            if  q.full():
                item = q.get()
                a = a + 1                
            if a == req:
                t1 = time.time()
                fsd = req/(t1-t0)
                print('\nSuccessfully consumed ',a, 'requests',(a*100)/req,'%')
                print('Elapsed Time: %.2f'%(t1-t0),'s')
                print(f'Throughput: {fsd:.2f}','successful requests/s' )
                break
                
                
        return 
        

if __name__ == '__main__':
    
    ProducerThread().start()
    ConsumerThread().start()

    
    