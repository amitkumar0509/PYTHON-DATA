sum = 0 
while True:
    userinput = input("Customer item price : ")
    if userinput!='q':
        sum +=int(userinput)
    else:
        print(f"The total amount is {sum}")
        break