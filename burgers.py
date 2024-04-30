# Define the Restaurant class
class Restaurant:
    # Initialize attributes for name, category, rating, and delivery status
    name = ''       # Name of the restaurant
    category = ''   # Category of the restaurant (e.g., American Diner, American Pizza)
    rating = 0.0    # Rating of the restaurant (out of 5.0)
    delivery = False  # Whether the restaurant offers delivery service or not

# Create an instance of the Restaurant class for Bob's Burgers
bobs_burgers = Restaurant()

# Set the attributes for Bob's Burgers
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.6
bobs_burgers.delivery = False

# Create another instance of the Restaurant class for Pizza Hut
pizza_hut = Restaurant()

# Set the attributes for Pizza Hut
pizza_hut.name = 'Pizza Hut'
pizza_hut.category = 'American Pizza'
pizza_hut.rating = 4.2
pizza_hut.delivery = True

# Create an instance of the Restaurant class for McDonalds
mcdonalds = Restaurant()

# Set the attributes for Mcdonalds
mcdonalds.name = 'McDonalds'
mcdonalds.category = 'Nasty Burgers'
mcdonalds.rating = 4.9
mcdonalds.delivery = True

# Print the attributes of Bob's Burgers
print(vars(bobs_burgers))

# Print the attributes of Pizza Hut
print(vars(pizza_hut))

# Printe the attributes of McDonalds
print(vars(mcdonalds))
