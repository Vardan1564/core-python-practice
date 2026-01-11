import pandas as pd
import matplotlib.pyplot as pl
# d1 ={
#     "name":['vardan','smit','pratik'],
#     "marks":[22,44,33],
#     "city":['rajkot','jamnagr','rajkot']
# }

# data = pd.DataFrame(d1)
# data.to_csv('sheet1.csv')
# print(data)

data = pd.read_csv('sheet1.csv')
# print(data.head(2))
# print(data.tail(1))
# print(data.describe())

# update marks in normal way
# data['marks'][0]=35

# using LOC frist-> ROWs and second->colunm
# data.loc[1,'marks']=40 

# set index
# data.index=['i','ii','iii']


# data.loc[0,2]='asd'
# data.loc[1,2]='asd'
# data.loc[2,2]='asd'


# print(data.loc[[1],['name','marks']])
# print(data.sort_index(axis=0, ascending=False))
# print(data)

data1=data[data['marks'] == data['marks'].max()] 
data1.to_csv('sheet2.csv')
# print(data1)
# print(data)

print(data[data.marks > 25])
# print(data1)
print(data.index)
# set index like
# data.set_index('column_name')
# data.reset_index(inplace=True)

# sorting data (sort marks)
# print(data.sort_values('marks',ascending=False))

p=data.plot()

