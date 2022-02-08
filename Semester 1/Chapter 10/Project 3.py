# Membuka file dengan mode untuk di baca
file = open("d:/file2.txt", "r")

# Membaca file perbaris
readFile = file.readlines()

# List untuk meyimpan semua dictionary
dataMhs = []

# Looping for untuk split data, menghilangkan char, membuat dictionary, serta menambahkannya ke dalam dataList
for i in range(len(readFile)):
    data = readFile[i].rstrip("\n")
    pecahData = data.split("|")
    dataDict = {'nim':pecahData[0], 'nama':pecahData[1], 'alamat':pecahData[2]}
    dataMhs.append(dataDict)

# Cetak dataMhs
print(f'dataMhs = {dataMhs}')

# Menutup file
file.close()
