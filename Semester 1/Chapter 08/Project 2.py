try:
    def average(bil):
        return sum(bil) / len(bil)
    bil = []
    n = int(input('Berapa banyak angka yang ingin dimasukkan? : '))
    for x in range(n):
        num = int(input(f'Bilangan bulat ke-{x+1} : '))
        bil.append(num)
    print(f'\nRata rata dari list {bil}        : {average(bil)}\nNilai tertinggi dari list {bil}  : {sorted(bil)[-1]}\nNilai terrendah dari list {bil}  : {sorted(bil)[0]}')
except ValueError:
    print('Input yang dimasukkan bukan berupa angka')
