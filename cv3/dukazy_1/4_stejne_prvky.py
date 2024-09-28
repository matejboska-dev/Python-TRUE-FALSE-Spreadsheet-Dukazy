##4. Je možné vložit dva stejné prvky?

# Tuple
tuple_example = (1, 1, 2, None, None)
print(tuple_example)  # true

# List
list_example = [1, 1, 2]
print(list_example)  # true

# Set
set_example = {1, 1, 2, None, None}
print(set_example)  # false

# Dictionary
dict_example = {'a': 1, 'b': 1}
print(dict_example)  # klice jedinecne, hodnoty mohou byt duplicitni

# String
string_example = "aabc"
print(string_example)  # true