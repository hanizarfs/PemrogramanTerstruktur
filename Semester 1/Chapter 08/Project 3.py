try:
    mhs = []
    n = int(input('Berapa mahasiswa yang ingin dimasukkan? : '))
    for data in range(n):
        namaMhs = input(f'Nama mahasiswa ke-{data+1} : ')
        mhs.append(namaMhs)
    charOfValue = [len(i) for i in sorted(mhs)]
    print('\nDaftar nama mahasiswa yang diurutkan berdasarkan banyaknya karakter\n')
    for nama, char in zip(sorted(mhs), charOfValue):
        print(f'{nama} ({char} Karakter)')
except ValueError :
    print('Input yang dimasukkan bukan berupa angka')
