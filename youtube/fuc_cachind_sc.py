from functools import lru_cache
import time
# aa fun no use value ne store kar note - one time run kar va
# @lru_cache aa readymait decorater che aa fun.. nu 
@lru_cache(maxsize=None)
def xyz(a,b):
    time.sleep(3)
    c=a+b
    print(c)
    return xyz

print(xyz(4,5))
print("diferant")
print(xyz(5,5))
print("same")
print(xyz(5,5))
print("same")