try:
    listBuah = []
    n = int(input('Berapa banyak buah yang ingin dimasukkan? : '))
    for x in range(n):
        buah = input(f'Nama buah ke-{x+1} : ')
        listBuah.append(buah)
    def sortStringByChar(listBuah):
        listBuah.sort(reverse=True,key=len)
        return(listBuah)
    print(sortStringByChar(listBuah))
except:
    print('Input yang dimasukkan bukan berupa angka')
