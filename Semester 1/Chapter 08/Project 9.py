buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print("\nDaftar Buah :")
no = 1
for key, value in buah.items():
    print(f'{no}. {key} Rp. {value}/Kg.')
    no += 1
namaBuah = input("\nNama buah yang dibeli : ")
if (namaBuah in buah):
    kg = float(input('Berapa Kg             : '))
    print('-------------------------------')
    print(namaBuah)
    print("Total harga           :",buah[namaBuah] * kg)
else:
    print(f'{namaBuah} sedang kosong / sudah habis')
