try:
    bil = []
    n = int(input('Berapa banyak angka yang ingin dimasukkan? : '))
    for x in range(n):
        num = int(input(f'Bilangan bulat ke-{x+1} : '))
        bil.append(num)
    bil.sort(reverse=True)
    print(f'Berikut urutan bilangan dari angka terbesar ke terkecil\n{bil}')
except ValueError:
    print('Input yang dimasukkan bukan berupa angka')
