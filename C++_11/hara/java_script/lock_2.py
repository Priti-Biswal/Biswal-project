import threading

lock = threading.RLock()

print ("First try :", lock.acquire())
print ("First try :" ,lock.acquire(0))
