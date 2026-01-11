import matplotlib.pyplot as pl

file = open("D:\\python\\MCA\\emp.txt","r")

name = []
age = []
sal = []


# strip : is use for remove space , tabs , newnline like "\n"
for line in file:
    data = line.strip().split(",")
    if (len(data) == 4):
        name.append(data[1])
        age.append(int(data[2]))
        sal.append(int(data[3]))
print("name ",name)
print("age ",age)
print("sal ",sal)


max_sal_index = sal.index(max(sal))

print("emp with max sal : ",name[max_sal_index],"\n he is sal is : ",sal[max_sal_index])



pl.plot(name,age, label="age" , color = 'blue')
pl.plot(name ,sal, label = "sal", alpha=0.6, color = 'green')
pl.xlabel("name")
pl.ylabel("Values")
pl.title("age and sal bar graph")
pl.legend()
pl.show()
