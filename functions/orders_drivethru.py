# Drive-thru

# a function to retrieve the name of an item based on its number
def get_item(item_number):
	# Dictionary containing item numbers as keys and item names as values
	items = {
		1: "Burger",
		2: "Pizza",
		3: "Fries",
		4: "Salad",
		5: "Soda",
		6: "Pasta"
	}
	# Return the item name corresponding to the item number
	# Invalid when the number is not on the Dictionary 
	return items.get(item_number, "Invalid item number")

# a function to welcome the user and display the menu
def welcome():
	print("Welcome to DriveThru. Tell us what would you like to have")
	print("Find our menu below")
	# Iterate over the items dictionary to display the menu
	for item_number, item_name in items.items():
		print(f"{item_number}: {item_name}")

def order():
	order_list = []
	while True:
		option = input("What would you like to order? (Enter item number or type 'done' to finish): ")
		if option.lower() == 'done':
			break
		try:
			item_number = int(option)
			if item_number in items:
				order_list.append(get_item(item_number))
			else:
				print("Invalid item number. Please try again.")
		except ValueError:
			print("Invalid input. Please enter a valid number.")
	return order_list
			
items = {
		1: "Burger",
		2: "Pizza",
		3: "Fries",
		4: "Salad",
		5: "Soda",
		6: "Pasta"
}

welcome()
order_list = order()

print("Your order: ")
for item in order_list:
	print(item)