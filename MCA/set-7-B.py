d1 = {'a':10 , 'b':20, 'c':40}
d2 = {'a':20, 'b':20 , 'c':10}

add = d1.copy()

for key , value in d2.items():
    if key in add:
        add[key] += value

print(add)

lst = ['A', 'B', 'C', 'B', 'B', 'A', 'D', 'C', 'D']

unique = list(set(lst))

print("original list",lst)
print("After Remove Duplicate : ",unique)