str1 = "aaabbccddzzmm"
output = ""
char = str1[0]
count =0
for ch in str1:
    if ch == char:
        count += 1
    else:
        output  += str(count) +char
        char = ch
        count = 1
output  += str(count) +char
print(output)