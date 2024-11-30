def vowels_consonent(input):
    vowel = "aeiou"
    consonent = 0
    vowel_count =0
    for char in input:
        if char.isalpha():
            if char in vowel:
                vowel_count+=1
            else :
                consonent+=1
    return vowel_count,consonent
                
input = "helloworld"
vowel , consonent = vowels_consonent(input)
print(f"vowels:{vowel},consonent:{consonent}")



    
   