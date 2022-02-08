def menu():
    try:
        print("\nDAFTAR BUAH\n")
        no = 1
        for key, value in buah.items():
            print(f'{no}. {key} Rp. {value}/Kg.')
            no += 1
        shop()
    except ValueError:
        print('Input salah / bukan angka\n')
def shop():
    try:
        while True:
            namaBuah = input("\nBuah yang dibeli [nama]\t\t: ")
            if (namaBuah in buah):
                kg = float(input('Berapa Kg\t\t\t: '))
                hasilBelanja[namaBuah] = (buah[namaBuah]*kg)
                again = input('\nBeli buah yang lain(y/n)\t: ')
                if again.lower() == "y":
                    pass
                else:
                    print('\n=======================  STRUK  =======================')
                    for i in hasilBelanja:
                        print(f'{i}\t\t\t\t: Rp. {hasilBelanja[i]}')
                    print('-------------------------------------------------------')
                    print(f'Total Harga\t\t\t: Rp. {sum(hasilBelanja.values())}')
                    print('=======================================================')

                    break
            else:
                print(f'{namaBuah} tidak ada\nTuliskan nama buah yang akan di beli!')
    except ValueError:
        print('Input salah / bukan angka')
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
hasilBelanja ={}
menu()
