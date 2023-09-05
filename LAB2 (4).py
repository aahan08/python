    
# 4)
num = float(input("enter a 3 digit number: "))
sum=0
sum= sum +num%10
num=num//10
sum= sum +num%10
num=num//10
sum=sum + num
print(sum)
if num%3==10:
    print("It is divisible by 3")
else:
    print("It is not divisible by 3")
