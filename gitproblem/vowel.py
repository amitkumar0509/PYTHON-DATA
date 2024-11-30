def vowel_consonents(input_str):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonents_count = 0
    for char in input_str:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonents_count += 1
            
    return vowel_count, consonents_count
input_str = input("Enter a string :")
vowel_count, consonents_count = vowel_consonents(input_str)
vowel_consonents(input_str)
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonents:{consonents_count}")

