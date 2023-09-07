def replace_vowels_with_asterisk(input_string):
    vowels = "AEIOUaeiou"
    result = ""
    for char in input_string:
        if char in vowels:
            result += '*'
        else:
            result += char
    return result

# Get input from the user
input_string = input("Enter a string: ")

# Call the function and display the result
new_string = replace_vowels_with_asterisk(input_string)
print(f"The string with vowels replaced by '*' is: {new_string}")
