import threading
import time
from concurrent.futures import ThreadPoolExecutor

def thread(sec):
    time.sleep(sec)
    print(f"the sec is {sec}")


# normal call method.
# thread(2)
# thread(5)
    
# run use thread.. 
ti1=time.perf_counter()
    
t1=threading.Thread(target=thread,args=[4])
t2=threading.Thread(target=thread,args=[2])
t3=threading.Thread(target=thread,args=[1])


def thread_run():
    # run using start method ..
    t1.start()
    t2.start()
    t3.start()

    # using join method it is give total time of fuction is execute like/ this function have big sec is 4 than it return 4.somthing sec ..
    t1.join()
    t2.join()
    t3.join()

    ti2=time.perf_counter()
    print(ti2-ti1)


def poolingdemo():

    with ThreadPoolExecutor()as executor:
        # t1=executor.submit(thread,3)
        # t2=executor.submit(thread,2)

        # print(t1.result())
        # print(t2.result())
        l=[3,2,3,4]
        ru=executor.map(thread,l)
        for i in ru:
            print(i)


poolingdemo()      

