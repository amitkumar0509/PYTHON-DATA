def sum_digit(n):
    return sum(int(i) for i in str(n))
n = 1324
b = sum_digit(n)
print(b)# Output: 0