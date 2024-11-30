# name = "Amit kumar "
# nmaespace = name[3:6]
# print(nmaespace)
# codespace1 =name[1]
# print(codespace1)

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050"))