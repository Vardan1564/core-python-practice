import matplotlib.pyplot as pl

file = open("MCA/emp.txt","r")
line = file.readlines()
name =[]
salary = []
for i in line:
    data = i.strip().split(",")
    name.append(data[1])
    salary.append(data[3])


print(name)
print(salary)

pl.bar(name,salary,label="EMP Salary Bar")
pl.xlabel("name")
pl.ylabel("salary")
pl.legend()
pl.show()

max_sal = max(salary)

color = []
for i in salary:
    if i == max_sal:
        color.append("Green")
    else:
        color.append("blue")
    
pl.bar(name,salary,color = color)
pl.show()