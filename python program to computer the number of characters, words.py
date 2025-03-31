def count_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Count lines
            num_lines = len(lines)
            
            # Count words and characters
            num_words = 0
            num_characters = 0
            for line in lines:
                num_words += len(line.split())
                num_characters += len(line)
            
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_characters}")
    except FileNotFoundError:
        print("The specified file does not exist.")

# Example usage:
file_path = input("Enter the file path: ")
count_file_content(file_path)