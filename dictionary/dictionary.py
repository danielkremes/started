# First part
fruits = {"fruits": "apple", "price": 24.99}
print(fruits)  # Output: {"fruits": "apple", "price": 24.99}

print("\n================================")

# Second part
contact = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "+1 123-456-7890"
}
print(contact)  # Output: {"name": "John Doe", "email": "johndoe@example.com", "phone": "+1 123-456-7890"}

print("\n================================")

# Third part (contacts database)
contacts_database = {
    "daniel.kremes@brf.com": {"name": "Daniel", "phone": "123-456-7890"},
    "jane.doe@gmail.com": {"name": "Jane", "phone": "987-654-3210"},
    "john.doe@example.com": {"name": "John", "phone": "098-765-4321"}
}

# Print specific contact
print(contacts_database["daniel.kremes@brf.com"])  # Output: {'name': 'Daniel', 'phone': '123-456-7890'}

# Loop over the contacts database and print details
for key in contacts_database:
    print(f"Email: {key}")
    print(f"Name: {contacts_database[key]['name']}")
    print(f"Phone: {contacts_database[key]['phone']}")
    print("-------------------------------")

print("\n================================")

# Loop over the contacts database with items() method
for key, value in contacts_database.items():
    print(key, value)

print("\n================================")

# Make a copy of a specific contact
copy = contacts_database["daniel.kremes@brf.com"].copy()
print(copy)  # Output: {'name': 'Daniel', 'phone': '123-456-7890'}

print("\n================================")

# Correct use of dict.fromkeys() method
fruits = dict.fromkeys(["data_price_update"], "07/10/2024")
print(fruits)  # Output: {'data_price_update': '07/10/2024'}

# Get 'price' key, and use a default empty dictionary if it doesn't exist
result = fruits.get("price", {})
print(result)  # Output: {}

# Output the 'fruits' dictionary
print(fruits)  # Output: {'data_price_update': '07/10/2024'}

print("\n================================")

# Correct use of dict.pop() method
fruits.pop("price", None)  # Pop 'price', if it exists, with a fallback (None) if it doesn't
print(fruits)  # Output: {'data_price_update': '07/10/2024'}

print("\n================================")

# Correct usage of setdefault() method:
# Adding a single key 'price' with a default value of 24.99
fruits.setdefault("price", 24.99)

# Now we want to add additional keys with default values using dictionary assignment
# To add multiple keys, we can simply assign them like this:
fruits["color"] = "orange"
fruits["name"] = "orange"

print(fruits)  # Output: {'data_price_update': '07/10/2024', 'price': 24.99, 'color': 'orange', 'name': 'orange'}

print("\n================================")

# Correct usage of update() method:

# Adding multiple key-value pairs using the update() method

additional_fruits = {
    "size": "medium",
    "taste": "sweet"
}

fruits.update(additional_fruits)

print(fruits)  # Output: {'data_price_update': '07/10/2024', 'price': 24.99, 'color': 'orange', 'name': 'orange', 'size': 'medium', 'taste': 'sweet'}

print("\n================================")

# Correct usage of clear() method:

# Clearing all the key-value pairs from the dictionary

fruits.clear()

print(fruits)  # Output: {}

print("\n================================")

# Correct usage of del keyword:

# Deleting a specific key-value pair using the del keyword

fruits = {"data_price_update": "07/10/2024", "price": 24.99, "color": "orange", "name": "orange"}

del fruits["price"]

print(fruits)  # Output: {'data_price_update': '07/10/2024', 'color': 'orange', 'name': 'orange'}

print("\n================================")

# Correct usage of popitem() method:

# Removing a key-value pair using the popitem() method

fruits = {"data_price_update": "07/10/2024", "price": 24.99, "color": "orange", "name": "orange"}

fruits.popitem()

print(fruits)  # Output: {'data_price_update': '07/10/2024', 'color': 'orange'}

print("\n================================")

# Correct usage of dict.keys() method:

# Getting all the keys from the dictionary

fruits_keys = fruits.keys()

print(fruits_keys)  # Output: dict_keys(['data_price_update', 'color', 'name'])

print("\n================================")

names =  {"name":"Daniel", "age":24, "occupation":"Internship"}

"name" in names# First part
fruits = {"fruits": "apple", "price": 24.99}
print(fruits)  # Output: {"fruits": "apple", "price": 24.99}

print("\n================================")

# Second part
contact = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "+1 123-456-7890"
}
print(contact)  # Output: {"name": "John Doe", "email": "johndoe@example.com", "phone": "+1 123-456-7890"}

print("\n================================")

# Third part (contacts database)
contacts_database = {
    "daniel.kremes@brf.com": {"name": "Daniel", "phone": "123-456-7890"},
    "jane.doe@gmail.com": {"name": "Jane", "phone": "987-654-3210"},
    "john.doe@example.com": {"name": "John", "phone": "098-765-4321"}
}

# Print specific contact
print(contacts_database["daniel.kremes@brf.com"])  # Output: {'name': 'Daniel', 'phone': '123-456-7890'}

# Loop over the contacts database and print details
for key in contacts_database:
    print(f"Email: {key}")
    print(f"Name: {contacts_database[key]['name']}")
    print(f"Phone: {contacts_database[key]['phone']}")
    print("-------------------------------")

print("\n================================")

# Loop over the contacts database with items() method
for key, value in contacts_database.items():
    print(key, value)

print("\n================================")

# Make a copy of a specific contact
copy = contacts_database["daniel.kremes@brf.com"].copy()
print(copy)  # Output: {'name': 'Daniel', 'phone': '123-456-7890'}

print("\n================================")

# Correct use of dict.fromkeys() method
fruits = dict.fromkeys(["data_price_update"], "07/10/2024")
print(fruits)  # Output: {'data_price_update': '07/10/2024'}

# Get 'price' key, and use a default empty dictionary if it doesn't exist
result = fruits.get("price", {})
print(result)  # Output: {}

# Output the 'fruits' dictionary
print(fruits)  # Output: {'data_price_update': '07/10/2024'}

print("\n================================")

# Correct use of dict.pop() method
fruits.pop("price", None)  # Pop 'price', if it exists, with a fallback (None) if it doesn't
print(fruits)  # Output: {'data_price_update': '07/10/2024'}

print("\n================================")

# Correct usage of setdefault() method:
# Adding a single key 'price' with a default value of 24.99
fruits.setdefault("price", 24.99)

# Now we want to add additional keys with default values using dictionary assignment
# To add multiple keys, we can simply assign them like this:
fruits["color"] = "orange"
fruits["name"] = "orange"

print(fruits)  # Output: {'data_price_update': '07/10/2024', 'price': 24.99, 'color': 'orange', 'name': 'orange'}

print("name" in fruits)
