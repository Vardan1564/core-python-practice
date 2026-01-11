import pandas as pd
import matplotlib.pyplot as pl

df = pd.read_csv('Stud_marks.csv')
data = pd.DataFrame(df)

# all sub marks chart

pl.plot(data['name'],data['sub1_m'],label='sub1 marks')
pl.plot(data['name'],data['sub2_m'],label='sub2 marks')
pl.plot(data['name'],data['sub3_m'],label='sub3 marks')
pl.title('all subject marks')
pl.xlabel('Name')
pl.ylabel('ALL Subject Marks')
pl.legend()
pl.grid(True)
pl.show()









# find avg marks
# avg_sub2 = data['sub2_m'].mean()
# print(avg_sub2)

# plot avg sub2
# pl.bar(data['name'],data['sub2_m'],label='AVG sub2 Marks')
# pl.axhline(avg_sub2,color='red',linestyle='--',label=avg_sub2)
# pl.xlabel('name')
# pl.ylabel('sub2 marks')
# pl.legend()
# pl.show()


# find max marks 
# max_sub1 = data['sub1_m'].max()
# topper_name = data['name'][data['sub1_m'].idxmax()]

# colors = []
# for name in data['name']:
#     if name == topper_name:
#         colors.append('green')
#     else:
#         colors.append('blue')
# pl.bar(data['name'],data['sub1_m'],color = colors)
# pl.show()


# df = pd.read_csv('sheet1.csv')

# df.plot(x='name',y='marks',kind = 'bar')
# pl.title("Marks by Student")
# pl.xlabel("Name")
# pl.ylabel("Marks")

# pl.show()
# print(df)

# -----------------

# student = {
#     'name': ['vardan','smit','jay','pratik','kamlesh'],
#     'sub1_m': [45,40,30,35,34],
#     'sub2_m': [47,35,37,49,42],
#     'sub3_m': [44,45,20,29,34]
# }
# df =  pd.DataFrame(student)
# df.to_csv('Stud_marks.csv')

