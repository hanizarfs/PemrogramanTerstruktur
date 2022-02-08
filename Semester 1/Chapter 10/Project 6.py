try:
    # Input pathfile dengan isi filenya berupa teks asli
    filename = input("Path File  : ")
    teks = open(filename, "r").read()
    n = int(input('Nilai N    : '))

    # String variable untuk menampung teks asli
    teksSandi = ''

    # Jika teks dalam file kapital, maka akan di enkripsi disini.
    if teks.isupper():
        for i in teks:
            value = ord(i)
            newValue = value + n
            if newValue >= 90:
                newValue = newValue - 26
            elif newValue <= 65:
                newValue = 32
            teksSandi += chr(newValue)
     
#   ==================================================================================================  #
#   ===== INI DAPAT SAJA DI HAPUS APABILA TEKS ASLI YANG INGIN DI ENKRIPSI TEKSNYA KAPITAL SEMUA =====  #
#     Jika teks dalam file huruf kecil, maka akan di enkripsi disini.                                   #
#     elif teks.islower():                                                                              #
#         for i in teks:                                                                                #
#             value = ord(i)                                                                            #
#             newValue = value + n                                                                      #
#             if newValue >= 122:                                                                       #
#                 newValue = newValue - 26                                                              #
#             elif newValue <= 97:                                                                      #
#                 newValue = 32                                                                         #
#             teksSandi += chr(newValue)                                                                #
#                                                                                                       #
#     # Namun jika teks dalam file huruf campuran, maka akan di enkripsi disini.                        #
#     else:                                                                                             #
#         for i in teks:                                                                                #
#             value = ord(i)                                                                            #
#             newValue = value + n                                                                      #
#             if i.isupper():                                                                           #
#                 if newValue >= 90:                                                                    #
#                     newValue = newValue - 26                                                          #
#                 elif newValue <= 65:                                                                  #
#                     newValue = 32                                                                     #
#                 print(chr(newValue), end='')                                                          #
#             elif i.islower():                                                                         #
#                 if newValue >= 122:                                                                   #
#                     newValue = newValue - 26                                                          #
#                 elif newValue <= 97:                                                                  #
#                     newValue = 32                                                                     #
#             teksSandi += chr(newValue)                                                                #
#   ==================================================================================================  #
   
    # Membuat file text
    file = open("d:/file6_enkripsi.txt", "a+")


    # Menuliskan teks sandi ke dalam file text yang sudah dibuat
    file.write(f'{teksSandi}')
    print(f'Teks Asli  : {teks}\nTeks Sandi : {teksSandi}')

    # Menutup file
    file.close()
    
except FileNotFoundError:
    print('File tidak ditemukan')
except PermissionError:
    print('File tidak ditemukan')
