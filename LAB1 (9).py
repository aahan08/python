

# 9)
month =int(input("Enter monthly installment amount in Rs. :"))
duration=int(input("Enter the duration in months :"))
rate=7.1
d=duration/12
if month >= 500 and d >= 0.5:
    i=(month*d*rate)/100
    print("Interest is ",round(i,2))
elif month<500:
    print("The monthly investment should be more than Rs.500")
elif d<0.5:
    print("The duration shoud atleast be 6 months")
else:
    print("Invalid input")

