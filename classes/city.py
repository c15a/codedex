####  Favorite Cities


# Define a class named City
class City:
	# Constructor method to initialize the attributes of the City class
	def __init__(self, name, country, population, landmarks):
		self.name = name # Name of the city
		self.country = country # Country that the city is located 
		self.population = population 
		self.landmarks = [landmarks] # List of landmarks in the city
		## Additional attributes that I could add
		# self.mayor = mayor
		# self.flag = flag

	def display_info(self):
		print("The city " + self.name + '\'s population is approximately ' + str(self.population))

	def country_and_landmarks(self):
		# print the country and landmarks function
		# we make sure that we put the str(self.landmarks) when we want to Output a list - python reads that as a Tuple instead of List
		print("The country of " + self.name + "is " + self.country + "and some of its landmarks are " + str(self.landmarks))


# Create an instance of the City class for Frankfurt
frankfurt = City("Frankfurt", "Germany", 50000, ("Museum", "Bars"))
# Call forward the display_info from the class to show the population of the city
frankfurt.display_info()
frankfurt.country_and_landmarks()

# Create an instance of the City class for Vienna
vienna = City("Vienna", "Austria", 43000, ("Madam de sau", "Lakes"))
# Call forward the display_info from the class to show the population of the city
vienna.display_info()
vienna.country_and_landmarks()


# Print the attributes of Frankfurt city instance using vars() function
print(vars(frankfurt))
print(vars(vienna))