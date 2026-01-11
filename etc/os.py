import os

file = os.listdir("python,vvip")
i=0
for files in  file:
    print(files)
    os.rename(f"python/vvip{files}",f"python/vvip/{i}.png")
    i=i+1

# a=os.rename("vip1/a1.txt","vip1/image.txt")
# print(a)