# --------- * patne------------------
# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ---------------------lc 18

# ----position arguments---------

def f1(a,b):
    print("a =",a,"b =",b)

f1(10,12) # it is position args 
# 10 pela che to "a" ma avse 
# 12 e 10 pachi che to e "b" ma avse

# -------default argument -------

def f2(a,b=0): # b=0 is default args 
    print("a ",a,"b ",b) 

f1(12)
# aa chalse karn ke apde b mato default args apel che.

# ---------keyword argument ----------------------

def f3(a,b): 
    print("a =",a,"b =",b)

f3(b=10,a=11)
# ama apde mention kari che ke kai value kema apse to tene keyword args kevay

# note:
      # f2(a=11,10) aa khotu che  ✖️ rule : apde keyword args pachi position args no apiski
      # f2(10,a=88) aa pan khotu che ✖️   because a ma be value jay che