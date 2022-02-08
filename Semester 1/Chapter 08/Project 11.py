def dataBuah():
    print('\nData Buah\n')
    for data in buah:
        print(f' - {data} (Harga Rp. {buah[data]})')
def addDataBuah():
    try:
        dataBuah()
        addBuah = input('\nMasukkan buah  : ')
        addHarga = float(input('Harga satuan Rp. '))
        dict_1 = {"a": 1, "b":2, "c":3}
        if addBuah.title() in buah:
            print(f"Mohon maaf {addBuah} sudah ada dalam daftar buah")
            return menu()
        else:
            print(f"{addBuah.title()} berhasil di tambahkan")
            buah[addBuah.title()] = addHarga
            dataBuah()
            tanya = input('\nKembali ke menu [y/t]? : ')
            if tanya.lower() == 'y':
                return menu()
            else:
                return exit()
    except ValueError:
        print('Input salah / bukan angka\n')
        return addBuah()
def menu():
    choice = input('\nMENU\n\nA. Tambah data buah\nB. Beli buah\nC. Keluar\n\nPilihan menu : ')
    if choice.upper() == 'A':
        addDataBuah()
    elif choice.upper() == 'B':
        beliBuah()
    else:
        print('Terima Kasih')
        exit()
def beliBuah():
    try:
        namaBuah = input("\nBuah yang dibeli [nama]\t\t: ")
        if (namaBuah.title() in buah):
            kg = float(input('Berapa Kg\t\t\t: '))
            hasilBelanja[namaBuah.title()] = (buah[namaBuah.title()]*kg)
            again = input('\nBeli buah yang lain(y/n)\t: ')
            if again.lower() == "y":
                return beliBuah()
            else:
                print('\n=======================  STRUK  =======================')
                for i in hasilBelanja:
                    print(f'{i}\t\t\t\t: Rp. {hasilBelanja[i]}')
                print('-------------------------------------------------------')
                print(f'Total Harga\t\t\t: Rp. {sum(hasilBelanja.values())}')
                print('=======================================================')
                tanya = input('\nKembali ke menu [y/t]? : ')
                if tanya.lower() == 'y':
                    return menu()
                else:
                    return exit()
        else:
            print(f'{namaBuah.title()} tidak ada\nTuliskan nama buah yang akan di beli!')
    except ValueError:
        print('Input salah / bukan angka')
    
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
hasilBelanja ={}
menu()
