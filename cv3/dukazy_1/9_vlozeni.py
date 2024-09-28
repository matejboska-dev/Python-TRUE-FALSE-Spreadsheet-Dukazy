##9. Jakymi všemi metodami je možné vložit nový prvek do kolekce a jaké mají tyto metody vstypy?

# Tuple
# lze vytvorit novy tuple s tim starym a pridat tam hodnotu
tuple_example = (1, 2, 3)
new_tuple = tuple_example + (4,)
print("Nový tuple:", new_tuple)

# List
list_example = [1, 2, 3]
list_example.append(4)  # prida se prvek na konec
list_example.insert(1, 5)  # vlozeni prvku na konkretni index
list_example.extend([6, 7])  # prida prvky z jine kolekce 
print("List po přidání prvků:", list_example)

# Set
set_example = {1, 2, 3}
set_example.add(4)  # jeden prvek
set_example.update([5, 6])  # vice prvku
print("Set po přidání prvků:", set_example)

# Dictionary
dict_example = {'a': 1, 'b': 2}
dict_example['c'] = 3  # pridani noveho klice s hodnotou
dict_example.update({'d': 4, 'e': 5})  # pridani vice klicu a hodnot najednou
print("Dictionary po přidání prvků:", dict_example)

# String
# stringy nejsou menitelne ale lze vytvorit novy a pridat stary a novou hodnotu
string_example = "abc"
new_string = string_example + "d"
print("Nový string:", new_string)