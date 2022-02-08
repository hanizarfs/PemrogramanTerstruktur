a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a.insert(3, 10); b.insert(2, 15)
print("\nList A dan B","\nA =",a,"\nB =",b)

a.sort(); b.sort()
print("\nHasil Sort","\nA =",a,"\nB =",b)

c = []
d = []
c.append(a[2-9:])
d.append(b[2-9:])
print("\nHasil Add Sublist A dan B ke List C dan D","\nC =",(*c),"\nD =",(*d))

print("")
print(c)
print(d)
zipped_lists = zip(c, d)
print("")
print(c)
print(d)
sum = [x + y for (x, y) in zipped_lists]
print('\n', sum)


# ASDPOADAODDASDJAS
a = [1, 5, 6, 3, 6, 9, 11, 20, 12] 
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

print('data awal list a\n',a)
print('\ndata awal list b\n',b)
print('='*60)

a.insert(3,10)
b.insert(2,15)
print('\nhasil list a setelah di sisipkan nilai 10 ke indeks 3\n',a)
print('\nhasil list b setelah di sisipkan nilai 15 ke indeks 2\n',b)
print('='*60)

a.append(4)
b.append(8)
print('\nhasil list a setelah di sisipkan nilai 4 ke indeks terakhir\n',a)
print('\nhasil list b setelah di sisipkan nilai 8 ke indeks terakhir\n',b)
print('='*60)


a.sort()
b.sort()
print('\nhasil list a setelah sorting secara ascending\n',a)
print('\nhasil list a setelah sorting secara ascending\n',b)
print('='*60)

c = a[:8]
d = b[2:10]
print('\nlist c yang merupakan sublist dari a(indeks 0-7)\n',c)
print('\nlist d yang merupakan sublist dari b(indeks 2-9)\n',d)
print('='*60)


e = []
for i in range(len(d)):
    e += [c[i] + d[i]]
print('\nhasil list e yang merupakan penjumlahan dari setiap elemen list c dan d\n',e)
e = tuple(e)
print('\nhasil list e yang dijadikan tuple\n',e)
print('='*60)

min = min(e)
max = max(e)
sum = sum(e)

print('\nhasil min dari tuple e\n',min)
print('\nhasil max dari tuple e\n',max)
print('\nhasil sum dari tuple e\n',sum)
print('='*60)

myString = "python adalah bahasa pemrograman yang menyenangkan"
myStringSet = set(myString)

print('\nvariabel myString\n',myString)
print('\nkarakter huruf yang menyusun myString\n',myStringSet)

myStringSetList = list(myStringSet)
print('\nbentuk list myString\n',myStringSetList)
myStringSetList.sort()
print('\nbentuk list myString setelah di sorting ascending\n',myStringSetList)
