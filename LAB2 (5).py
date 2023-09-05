

# 5)
num = int(input("enter a 5 digit number: "))
a=num%10
a1=num//10
b=num%10
b1=num//10
c=num%10
c1=num//10
d=num%10
d1=num//10
e=num%10
e1=num//10
a=a*10000
b=b*1000
c=c*100
d=d*10
rev=a+b+c+d+e
print(rev)
print(num)
if num==rev:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
    
