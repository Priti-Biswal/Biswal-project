import logging
import threading
import time
import os 
def task1(): 
    print("Task 1 assigned to thread: {}\n".format(threading.current_thread().name)) 
    print("ID of process running task 1: {}\n".format(os.getpid()))
    
def thread_function(name):
    logging.info("Thread %s: starting\n", name)
    time.sleep(2)
    logging.info("Thread %s: finishing\n", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread\n")
    x = threading.Thread(target=thread_function, args=(1,))
    t1 = threading.Thread(target=task1, name='t1') 
    logging.info("Main    : before running thread\n")
    t1.start();
    x.start()
    logging.info("Main    : wait for the thread to finish\n")
    x.join()
    t1.join() 
    logging.info("Main    : all done")
