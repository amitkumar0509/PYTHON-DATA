number = int(input("Enter a number: "))
sum = 0 
a = len(str(number))
copy = number
while(number>0):
    digit = number % 10
    sum += digit**a
    number = number//10
if(sum == copy):
    print("true")
else:
    print("false")