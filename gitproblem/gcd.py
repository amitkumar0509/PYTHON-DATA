def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
result = gcd(36,60)
print(result)
