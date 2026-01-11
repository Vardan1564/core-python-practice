import pandas as pd
import matplotlib.pyplot as ml

# d1= {
#     "name": ['vardan','dhairya'],
#     "age": [21,18]
# }
# data =pd.DataFrame(d1)
# print(data)

# ml.bar(data["name"],data["age"])
# ml.show()


df = pd.read_csv('D:\\python\\MCA\\stud.csv')
data = pd.DataFrame(df)
print(data)
fdata = df[(df["course"]!="mca") & (df["age"]>=22)]
print(fdata)