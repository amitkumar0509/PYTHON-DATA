#Q1 Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'}(the order does not matter).

#code
# a = [("name", "Elie"), ("job", "Instructor")]
# b= dict(a)
# print(b) # {'name': 'Elie', 'job': 'Instructor'}
#Q2 Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. You can research the zip method to help you.
# a = ["CA", "NJ", "RI"]
# b = ["California", "New Jersey", "Rhode Island"]
# c = dict(zip(a,b))
# print(c)     
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
# Q3 Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
# a = "aeiou"
# b = {char:0 for char in a }
# print(b)

# Q4 Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet. You should return something like this (hint - use chr(65) to get the first letter):
# a = {i:chr(64+i) for i in range(1,27)}
# print(a)
# {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}