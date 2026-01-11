import asyncio
import requests

async def fun1():
    print("DONE 1")
    url="https://img.freepik.com/free-photo/autumn-leaf-falling-revealing-intricate-leaf-vein-generated-by-ai_188544-9869.jpg?w=1060&t=st=1707753567~exp=1707754167~hmac=a3b2ce8d93055b007ce671a20ce6960099065e23acc0fe00a8b5b268775764b9"
    respons=requests.get(url)
    open("mying.jpg","wb").write(respons.content)
    
    
async def fun2():
    print("DONE 2 ")
    url="https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg?w=1060&t=st=1707753593~exp=1707754193~hmac=3db38f95cee11979bd0ec5ade0695166eb3a22e4e59eec1f700a59c582d5ed4b"
    respons=requests.get(url)
    open("abc.jpg","wb").write(respons.content)

async def main():
    l=await asyncio.gather(
        fun1(),
        fun2(),
    )
    print(l)

asyncio.run(main())