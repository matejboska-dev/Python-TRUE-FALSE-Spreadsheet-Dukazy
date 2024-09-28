##10. Jakymi všemi metodami je možné smazat/odebrat existující prvek do kolekce a jaké mají tyto metody vstypy?

# Tuple
# nelze přímo smazat prvek.
tuple_example = (1, 2, 3)
new_tuple = tuple(x for x in tuple_example if x != 2)  # novej tuple bez hodnoty 2
print("Nový tuple:", new_tuple)

# List
list_example = [1, 2, 3, 4]
list_example.remove(3)  # smazani konkretniho prvku podle hodnoty
list_example.pop(1)  # smazani prvku na konkretnim indexu
del list_example[0]  # smazani pomoci del na indexu
print("List po odstranění prvků:", list_example)

# Set
set_example = {1, 2, 3, 4}
set_example.remove(3)  # smazani konkretni hodnoty v prvku
set_example.discard(2)  # smaze prvek pokud existuje
set_example.pop()  # smaze random prvek
print("Set po odstranění prvků:", set_example)

# Dictionary
dict_example = {'a': 1, 'b': 2, 'c': 3}
dict_example.pop('b')  # smaze prvek a jeho klic
del dict_example['a']  # smaze klic a prvek s pomoci del
dict_example.clear()  # smaze vsechny prvky
print("Dictionary po odstranění všech prvků:", dict_example)

# String
# stringy jsou nemenne
string_example = "aaabbbcccdddeee"
new_string = string_example.replace("b", "")  # odstrani vsechny vyskyty znaku 'b'
print("Nový string po odstranění znaku:", new_string)

