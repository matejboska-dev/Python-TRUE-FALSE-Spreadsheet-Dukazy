## 11. Jakými všemi metodami je možné upravit hodnotu existujícího prvku v kolekci?

# tuple
# muzeme vytvorit novy tuple kombinaci casti puvodniho.
tuple_example = (1, 2, 3, 4, 5)
tuple_example = tuple_example[:2] + (10,) + tuple_example[3:]  # zmena tretiho prvku
print("upraveny tuple:", tuple_example)

# list
# v listu muzeme zmenit hodnotu prvku pomoci indexu.
list_example = [1, 2, 3, 4, 5]
list_example[2] = 10  # zmenime treti prvek
print("upraveny list:", list_example)

# set
set_example = {1, 2, 3, 4, 5}
set_example.remove(3)  # odebrani prvku
set_example.add(10)  # pridani prvku
print("upraveny set:", set_example)

set_example.discard(4)  # odebrani prvku (bez chyby, pokud prvek neexistuje)
set_example.update([6, 7])  # pridani vice prvku
print("set po pouziti metod:", set_example)

# dictionary
dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_example['c'] = 10  # zmena hodnoty pro klic 'c'
print("upraveny dictionary:", dict_example)

dict_example.update({'f': 6})  # pridani noveho klice-hodnoty
dict_example.pop('a')  # odebrani klice 'a'
del dict_example['b']  # odebrani klice 'b'
print("dictionary po pouziti metod:", dict_example)

# string
string_example = "abcde"
string_example = string_example[:2] + "x" + string_example[3:]  # zmenime treti znak
print("upraveny string:", string_example)

string_example = string_example.replace("x", "z")  # nahrazeni znaku 'x' za 'z'
print("string po pouziti metody replace:", string_example)
