    
# 2)
h=float(input("enter height in inches: "))
w=float(input("enter weight in pounds: "))
w1=w*0.454
h1=h*0.0254
B=w1/(h1*h1)
if w1<0 or h1<0 or:
    print("invalid input")
else:
    print("BMI is ", B)
    
