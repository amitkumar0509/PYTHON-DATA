def sum_of_digit(n):
    return sum(int(digit) for digit in n)
a = (input())
b= (input())
sum_1 = sum_of_digit(a)
sum_2= sum_of_digit(b)
result=sum_1*sum_2
print(result)
