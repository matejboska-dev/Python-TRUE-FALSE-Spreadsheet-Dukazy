##6. Je možné kolekce vnořovat, tedy vložit kolekci do kolekce?

# Tuple
tuple_example = ((1, 2), (3, 4))
print(tuple_example)  # true

# List
list_example = [[1, 2], [3, 4]]
print(list_example)  # true

# Set
set_example = {frozenset([1, 2]), frozenset([3, 4])}
print(set_example)  # false

# Dictionary
dict_example = {'a': [1, 2], 'b': [3, 4]}
print(dict_example)  # true

# String
string_example = " " + (1,2)
print(string_example) # false