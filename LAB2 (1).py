# 1)
x = float(input("enter the lenght of side= "))
y = float(input("enter the lenght of second side= "))
h = float(input("enter the lenght of hieght= "))
area= 0.5*(x+y)*h
if x<0 or y<0 or h<0:
    print("invalid input")
else:
    print(area)
    


