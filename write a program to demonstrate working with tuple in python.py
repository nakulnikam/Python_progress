def count_vowels(string):
 vowels = "aeiouAEIOU"
 count = sum(1 for char in string if char in vowels)
 return count
# Example usage:
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
