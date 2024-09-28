##3. Používá se pro přístup k hodnotám index?

# Tuple
tuple_example = (1, 2, 3)
print("tuple: ")
print(tuple_example[0])  # true

# List
list_example = [1, 2, 3]
print("list: ")
print(list_example[0])  # true

# Set
print("Set: ")
set_example = {1, 2, 3}
# false no index


# Dictionary
print("Dict: ")
dict_example = {'a': 1, 'b': 2, 'c': 3}
print(dict_example['a'])  # false (key ne index)

# String
print("String: ")
string_example = "abc"
print(string_example[0])  # true