buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def buahTermahal(buah):
    return max(buah, key=buah.get)
print(f'Buah dengan harga termahal satuannya yaitu {buahTermahal(buah)}')
