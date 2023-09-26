# Dictionary to store fixed item data (name, price, quantity)
item_data = {
    '100': {'Name': 'chocolates', 'Price': 10.0, 'Quantity': 20},
    '108': {'Name': 'ice-creams', 'Price': 35.0, 'Quantity': 15},
    '102': {'Name': 'biscuits', 'Price': 15.0, 'Quantity': 15},
    '105': {'Name': 'Sprite', 'Price': 20.0, 'Quantity': 15},
    # Add more items as needed
}

# Function to calculate the total cost for an item
def calculate_item_cost(item, quantity):
    return item['Price'] * quantity

# Function to enter item data
def enter_item_data():
    item_cart = []
    while True:
        item_code = input("Enter item code (or 'done' to finish): ")
        if item_code.lower() == 'done':
            break
        if item_code not in item_data:
            print("Invalid item code. Please enter a valid code.")
            continue
        quantity = int(input(f"Enter quantity for {item_data[item_code]['Name']}: "))
        if quantity > item_data[item_code]['Quantity']:
            print(f"Sorry, only {item_data[item_code]['Quantity']} {item_data[item_code]['Name']} available in stock.")
            continue
        item_cost = calculate_item_cost(item_data[item_code], quantity)
        item_cart.append({'Item Name': item_data[item_code]['Name'], 'Quantity': quantity, 'Total Cost': item_cost})
        item_data[item_code]['Quantity'] -= quantity
    return item_cart

# Function to calculate the total bill
def calculate_total_bill(item_cart):
    total_bill = sum(item['Total Cost'] for item in item_cart)
    return total_bill

# Function to generate and display the itemized bill
def generate_itemized_bill(item_cart):
    print("\nItemized Bill:")
    print("-" * 50)
    print("{:<30} {:<10} {:<10}".format("Item Name", "Quantity", "Total Cost"))
    print("-" * 50)
    for item in item_cart:
        print("{:<30} {:<10} ${:<10.2f}".format(item['Item Name'], item['Quantity'], item['Total Cost']))
    print("-" * 50)

# Function to write the itemized bill and update item quantities to a file
def write_itemized_bill_and_update_quantities(item_cart, total_bill, file_name):
    with open(file_name, 'a+') as file:
        file.write("Itemized Bill:\n")
        file.write("-" * 50 + "\n")
        file.write("{:<30} {:<10} {:<10}\n".format("Item Name", "Quantity", "Total Cost"))
        file.write("-" * 50 + "\n")
        for item in item_cart:
            file.write("{:<30} {:<10} ${:<10.2f}\n".format(item['Item Name'], item['Quantity'], item['Total Cost']))
        file.write("-" * 50 + "\n")
        file.write(f"Total Bill: ${total_bill:.2f}\n")
        file.write("\nUpdated Item Quantities:\n")
        file.write("-" * 50 + "\n")
        for item_code, item_info in item_data.items():
            file.write("{:<30} {:<10}\n".format(item_info['Name'], item_info['Quantity']))
        file.write("-" * 50 + "\n")

# Main program
if __name__ == "__main__":
    print("Welcome to the Store Bill Generator!")
    
    item_cart = enter_item_data()
    total_bill = calculate_total_bill(item_cart)
    generate_itemized_bill(item_cart)
    
    file_name = "store_bill.txt"
    write_itemized_bill_and_update_quantities(item_cart, total_bill, file_name)
    print(f"Store bill data and updated quantities have been saved to {file_name}")
