## 13. Jakymi všemi metodami je možné získat hodnotu v pořadí třetího prvku v kolekci?

# tuple
tuple_example = (1, 2, 3, 4, 5)
print("treti prvek v tuple:", tuple_example[2])  # primy pristup pomoci indexu

# list
list_example = [1, 2, 3, 4, 5]
print("treti prvek v listu:", list_example[2])  # primy pristup pomoci indexu

# set
set_example = {1, 2, 3, 4, 5}
sorted_set = sorted(set_example)  # seradi prvky setu
print("treti prvek v setu po serazeni:", sorted_set[2])  # pristup pomoci indexu po serazeni

# dictionary
dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
third_key = list(dict_example.keys())[2]  # ziska treti klic
print("treti prvek ve slovniku (hodnota tretiho klice):", dict_example[third_key])

# string
string_example = "abcde"
print("treti znak ve stringu:", string_example[2])  # primy pristup pomoci indexu
