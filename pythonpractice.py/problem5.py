principle = float(input("Enter a principle amount: "))
rate =  float(input("Enter a rate: "))
time =  float(input("Enter a total time: "))

amount = principle *(1+ rate/100)**time
compound_interest = amount - principle

print("The total compound interest is : ",compound_interest)