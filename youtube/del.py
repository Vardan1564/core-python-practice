# import os

# data="D:\python\xyz.mp3"
# os.remove(data)

def vip(vb):
    def vip1(*args,**kwargs):
        print("hello ,how r u ")
        vb(*args,**kwargs)
        print("thanks bhai")
    return vip1

@vip
def hi():
    print("hii vardan")


hi()