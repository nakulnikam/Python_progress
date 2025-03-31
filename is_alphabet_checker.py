def is_alphabet(char):
    """
    Check if the given character is an alphabet.
    :param char: Single character input
    :return: String indicating if it is an alphabet or not
    """
    return "It is an alphabet." if char.isalpha() else "It is not an alphabet."

def main():
    """
    Main function to handle user input and output.
    """
    char = input("Enter a character: ")
    if len(char) == 1:  # Ensuring a single character input
        print(is_alphabet(char))
    else:
        print("Please enter a single character.")

if __name__ == "__main__":
    main()
