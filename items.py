# Function to calculate the total cost for an item
def calculate_item_cost(price, quantity):
    return price * quantity

# Function to enter item data
def enter_item_data():
    item_data = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter quantity: "))
        item_cost = calculate_item_cost(price, quantity)
        item = {
            'Item Name': item_name,
            'Price per Item': price,
            'Quantity': quantity,
            'Total Cost': item_cost
        }
        item_data.append(item)
    return item_data

# Function to calculate the total bill
def calculate_total_bill(item_data):
    total_bill = sum(item['Total Cost'] for item in item_data)
    return total_bill

# Function to display the item data and total bill
def display_item_data_and_total(item_data, total_bill):
    print("\nItem Data:")
    for item in item_data:
        print(f"Item Name: {item['Item Name']}")
        print(f"Price per Item: ${item['Price per Item']:.2f}")
        print(f"Quantity: {item['Quantity']}")
        print(f"Total Cost: ${item['Total Cost']:.2f}")
        print()
    print(f"Total Bill: ${total_bill:.2f}")

# Function to write item data and total bill to a file
def write_item_data_to_file(item_data, total_bill, file_name):
    with open(file_name, 'w') as file:
        file.write("Item Data:\n")
        for item in item_data:
            file.write(f"Item Name: {item['Item Name']}\n")
            file.write(f"Price per Item: ${item['Price per Item']:.2f}\n")
            file.write(f"Quantity: {item['Quantity']}\n")
            file.write(f"Total Cost: ${item['Total Cost']:.2f}\n\n")
        file.write(f"Total Bill: ${total_bill:.2f}\n")

# Main program
if __name__ == "__main__":
    item_data = enter_item_data()
    total_bill = calculate_total_bill(item_data)
    display_item_data_and_total(item_data, total_bill)
    
    file_name = "bill.txt"
    write_item_data_to_file(item_data, total_bill, file_name)
    print(f"Bill data has been saved to {file_name}")