def is_alphabet(char):
 if char.isalpha():
 return "It is an alphabet."
 else:
 return "It is not an alphabet."
# Example usage:
char = input("Enter a character: ")
if len(char) == 1: # Ensuring a single character input
 print(is_alphabet(char))
else:
 print("Please enter a single character.")