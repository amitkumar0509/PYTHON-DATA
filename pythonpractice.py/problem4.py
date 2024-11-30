def factorial(number):
    if number ==1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)
    
a = int(input("Enter a number : "))
output = factorial(a)
print("the factorial of number is:",output)