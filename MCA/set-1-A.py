def bubble_sort(l1):
    n = len(l1)
    ite = []
    m_i =3
    for i in range(n):
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j] 
        ite.append(l1.copy())
        if i+1 == m_i:
            break
        print(ite)
    
l1=[95,79,19,43,52,3]
print(l1)
bubble_sort(l1)
print("After Short : ",l1)

def fromtxt():
    file = open("MCA\\t1.txt","r")
    lines = file.readlines()

    for i in lines:
        print(i)
        num = [int(x) for x in i.strip().split(',')]
        print(num)
        
fromtxt()


    