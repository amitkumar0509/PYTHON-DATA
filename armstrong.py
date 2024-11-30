def armstrong(number):
    digits = str(number)
    power  = len(digits)
    total = sum(int(digit)**power for digit in digits)
    return total == number
def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers


start = 1
end = 10000
result = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end}: {result}")