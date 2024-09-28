##5. Je možné vložit hodnotu None?

# Tuple
tuple_example = (1, None, 2)
print(tuple_example)  # true

# List
list_example = [1, None, 2]
print(list_example)  # true

# Set
set_example = {1, None, 2}
print(set_example)  # true

# Dictionary
dict_example = {'a': 1, 'b': None}
print(dict_example)  # true

# String
string_example= " " + None
print(string_example) # false