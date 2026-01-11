a={1:'vardan',2:'shiv',3:'vijay',4:'lalo'}
b={
    1:'90164 10956',
    2:'94098 09498',
    3:'92348 84891',
    4:'89562 89541'
}
print(a)

user=input("ENTER THE NAME FOR YOU WANT NUMBER: ")

if (user==a[1]):
    print("Phone is: ",b[1])
elif(user==a[2]):
    print("Phone is: ",b[2])
elif(user==a[3]):
    print("Phone is: ",b[3])
elif(user==a[4]):
    print("Phone is: ",b[4])
else:
    print("THIS NAME IS NOT HERE...... ")