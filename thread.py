import threading
import time

def task(num):
    print(num,'-1')
    time.sleep(0.5)
    print(num,'-2')
    time.sleep(0.5)
    print(num,'-3')
    time.sleep(0.5)
    
thread = threading.Thread(target=task(1))
thread.start()
task(2)
# thread.join()

print("End")