


# 9
x= int(input("Enter The Basic Salary: "))
h=(20*x)/100
t=(5*x)/100
d=(10*x)/100
gross=x+h+t+d
if gross<300000:
    print("Tax is 0%")
elif 300000<gross<1000000:
    print("Tax is 10% of the gross salary")
elif 1000000<gross<2500000:
    print("Tax is 20% of the gross salary")
else:
    print("Tax is 30% of the gross salary")
    
