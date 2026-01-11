import multiprocessing
import requests
import os

def dwl(url,name):
    print(f"start dowloading{name}")
    r=requests.get(url)
    open(f"D:\python\image/img{name}.jpg","wb").write(r.content)
    print(f"dowloading finis.................{name}")

url="https://picsum.photos/2000/3000"

def call():
    if __name__=='__main__':
        for i in range(10):
            #normal way----> 
            # dwl(url,i)
            process=multiprocessing.Process(target=dwl,args=[url,i])
            process.start()

call()


