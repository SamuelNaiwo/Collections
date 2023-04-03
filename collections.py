## Collections
# Lists
# [] for list
# Shopping List
shopping_list = ["milk", "bread", "eggs", "chocolate", "jam"]
print(shopping_list)
print(type(shopping_list))

# Access a particular part of the list
print(shopping_list[0])  # Selects index from list = milk

# Change element in a list
shopping_list[2] = "butter"  # Changes eggs to butter
print(shopping_list)

# Using list methods

# Add to list with append()
shopping_list.append("fish")
print(shopping_list)

# Remove from list with remove()
shopping_list.remove("bread")
print(shopping_list)

# Remove last item without specifying pop()
shopping_list.pop()
print(shopping_list)

# You can have list with mixed data types
mixture = [1, 2, 3, 4.5, "five", "six"]
print(mixture)

# List Slicing
print(mixture[1:3])

# Reverse order of slice
print(mixture[-2::])  # Returns "five", "six"

# Step over (Skip item on list)
print(mixture[::2])  # Returns 1, 3, "five"

#Tuples (Immutable) - Can not be changed
tuple_example = ("bread", "eggs", "milk")
print(tuple_example)

## Dictionaries
# Another way to manage data but a bit more dynamic and complex

# Key-value pairs
# Key - reference to object
# Value - The data mechanism to store that data in (e.g string, int, list and another dictionary)

student_1 = {
    "name": "Samuel",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variable", "data_types", "setup"]
}

# Access the dictionary
print(student_1["stream"])

# Access a part of the list in the dictionary
print(student_1["completed_lesson_names"][0])

# Change a value in dictionary
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# Changing an element of a list within dictionary
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

# Dictionary methods
print(student_1.keys())  # Returns all the keys
print(student_1.values())  # Returns all the values

## Sets and Frozen Sets
# Set - A list that has no order
car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)
car_parts.add("windows")
print(car_parts)

# Remove a list item
car_parts.discard("doors")
print(car_parts)

# Frozen sets (immutable)
x = frozenset([1, 2, 3, 4])
print(x)