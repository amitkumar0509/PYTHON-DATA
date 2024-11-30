str1 = "a3b5m3n6c8"
output = ""
for char in str1:
    if char.isalpha():
        var = char
    else:
        num= int(char)
        output += var*num
print(output)