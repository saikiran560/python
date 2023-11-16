def get_unique_words(filename):
    # Open the file and read its content
    with open(filename, 'r') as file:
        content = file.read()

    # Split the content into words and convert to lowercase
    words = [word.lower() for word in content.split()]

    # Get unique words and sort them alphabetically
    unique_words = sorted(set(words))

    return unique_words

if __name__ == "__main__":
    # Prompt the user for a file name
    file_name = input("Enter the name of the text file: ")

    # Get and print unique words from the file
    unique_words = get_unique_words(file_name)

    if unique_words:
        print("\nUnique words in alphabetical order:")
        for word in unique_words:
            print(word)
