##7. Je možné za běhu programu změnit velikost kolekce?

# Tuple
tuple_example = (1, 2, 3)
# false

# List
list_example = [1, 2, 3]
list_example.append(4)  # true
print(list_example)

# Set
set_example = {1, 2, 3}
set_example.add(4)  # true
print(set_example)

# Dictionary
dict_example = {'a': 1, 'b': 2}
dict_example['c'] = 3  # true
print(dict_example)

# String

my_string = "Hello"
print(f"Original string: {my_string}")
try:
    my_string[0] = "h"
except TypeError as e:
    print(f"Error: {e}") # false

