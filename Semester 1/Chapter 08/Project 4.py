sayur = ['Bayam', 'Kangkung', 'Wortel', 'Selada']
def add_sayur():
    sayur.append(input('Sayur yang ingin ditambahkan : ').title())
    tanya = input('Tambah lagi [y/t] ? : ')
    if tanya.lower() == 'y':
        return add_sayur()
    elif tanya.lower() == 't':
        return btm()
    else:
        print('Data yang dimasukkan tidak diketahui')
        return add_sayur()
def del_sayur():
    sayur.remove(input('Sayur yang ingin di hapus : ').title())
def btm():
    btm = input('Kembali ke menu [y/t] ? : ')
    if btm.lower() == 'y':
        return main()
    elif btm.lower() == 't':
        return exit()
    else:
        exit()
def main():
    try:
        print('\nMenu\nA. Tambah data sayur\nB. Hapus data sayur\nC. Tampilkan data sayur\nD. Keluar')
        choice = input('Pilihan Anda : ')
        if choice.upper() == 'A':
            add_sayur(); btm()
        elif choice.upper() == 'B':
            del_sayur(); btm()
        elif choice.upper() == 'C':
            print(sayur); btm()
        elif choice.upper() == 'D':
            exit()
    except ValueError:
        print('Nama Sayur tersebut tidak ditemukan')
        btm()
main()
