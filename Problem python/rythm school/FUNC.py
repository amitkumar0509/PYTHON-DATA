# def sum(a,b):
#     return a + b
# a = int(input("number 1 :"))
# b = int(input("number 2 :"))
# result = sum(a,b)
# print(f"The sum of {a} + {b} is {result}")

class InvalidAgeError(Exception):
    pass

def validate_age(age):
    try:
        if age < 0:
            raise InvalidAgeError("Age cannot be negative.")
        elif age < 18:
            return "You are not eligible to vote."
        else:
            return "You are eligible to vote."
    except InvalidAgeError as e:
        return f"Error: {e}"

# Calling the function
print(validate_age(25))  # Output: You are eligible to vote.
print(validate_age(-5))  # Output: Error: Age cannot be negative.
