import eve
import time
for i in range(10):
    eve.start()
    print("sleep started")
    time.sleep(3600)
    print("sleep ended")