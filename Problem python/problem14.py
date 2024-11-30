first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number+1):
    if num > 1 :
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)