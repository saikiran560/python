#import roman
 
# converting the integer to Roman
# and storing it in variable 'r'
#i = roman.toRoman(2023)
# Printing the converted value
#print(i)



class int_to_roman:
    def convert(self, num):
        result = ''
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        for value, numeral in zip(values, numerals):
            while num >= value:
                result += numeral
                num -= value

        return result

# Example usage:
if __name__ == "__main__":
    int_input = int(input("Enter an integer between 1 and 3999: "))

    converter = int_to_roman()
    roman_numeral = converter.convert(int_input)

    print(f"The Roman numeral representation of {int_input} is: {roman_numeral}")
