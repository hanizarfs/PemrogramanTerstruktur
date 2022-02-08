buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def average(buah):
    total = sum(buah.values())/len(buah)
    return total
print(f'Rata rata harga satuan dari keseluruhan buah adalah Rp. {average(buah)}')
