def faktorial(n):
    if n > 2:
        return n * faktorial(n - 1)
    return 2

nilai_jml_faktorial =[]
nilai_faktorial = []
while True:
    n = int(input('Masukkan angka : '))
    hasil_faktorial = faktorial(n)
    print(f'{n}! = {hasil_faktorial}')
    
    n_fix = str(n)+'!'
    nilai_faktorial.append(n_fix)
    nilai_jml_faktorial.append(hasil_faktorial)
    
    tanya = input('Selesai [y/t] ? : ')
    if tanya.lower() == 'y':
        jumlah = sum(nilai_jml_faktorial)
        print(f'Hasil dari {" + ".join(map(str, nilai_faktorial))} adalah : {jumlah}')
        break
    elif tanya.lower() == 't':
        pass
    else:
        print('Jawaban Tidak Diketahui')
        break
