def less_prime(n):
    if n<=2:
        print(n,"is the prime number")
        return
    for num in range(2,n):
        for divisor in range(2,num):
            if num % divisor == 0:
                break
        else:
            print(num, end=", ")
    print()  

# Example usage
n = 20
print("Prime numbers less than", n, "are:")
less_prime(n)