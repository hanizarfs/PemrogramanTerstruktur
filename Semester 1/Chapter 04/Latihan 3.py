def nomor1():
    jarak = 795
    print("Kota asal                 : A")
    print("Kota tujuan               : C")
    print("Jarak Kota A ke Kota C    : 795 km")
    print("Kapasitas full tangki BBM : 50 lt")
    bbm = (jarak*1)/12
    print("Minimal anda harus menyiapkan BBM sebanyak", bbm, "Liter")
    numerator = bbm
    denominator = 50
    rounded_up = -(-numerator // denominator)
    print("Anda cukup mengisi tangki BBM ", rounded_up, "kali.")
    
    
def nomor2():
    kota_asal = input  ("Kota Asal                  : ")
    kota_tujuan = input("Kota Tujuan                : ")
    while True:
        print("Jarak dari kota", kota_asal, "ke", kota_tujuan, "adalah : ")
        try:
            jarak = int(input("Tuliskan hanya dengan angka dan dalam satuan [KM] : "))
        except ValueError:
            print("Mohon maaf, data yang anda masukkan salah. Anda cukup memasukkan angkanya saja dalam satuan [KM]\nsaya ulangi dari awal ya :)")
            continue
        else:
            #Lanjut
            break
    else:
        print("You are not able to vote in the United States.")
    
    print("Kapasitas full tangki BBM  : 50 lt")
    bbm = (jarak*1)/12
    print("Minimal anda harus menyiapkan BBM sebanyak", bbm, "Liter")
    numerator = bbm
    denominator = 50
    rounded_up = -(-numerator // denominator)
    print("Anda cukup mengisi tangki BBM ", rounded_up, "kali.")

def kembali_ke_menu():
    menu()
    
def menu():
    print("\nHalo, Selamat Datang")
    print("Soal no 1")
    print("1. Lihat hasil soal Nomor 3")
    print("2. Bagaimana dengan situasi yang lain?")
    print("3. Keluar")
    jawab = input("=>")
    if jawab == "1":
        nomor1()
        jawab = input("Kembali ke menu [y/n] ? : ")
        if jawab == "y" or "Y":
            kembali_ke_menu()
        else:
            print("Terima Kasih")
            exit()
    elif jawab == "2":
        nomor2()
        jawab = input("Kembali ke menu [y/n] ? : ")
        if jawab == "y" or "Y":
            kembali_ke_menu()
        else:
            print("Terima Kasih")
            exit()
    else:
        print("Terima Kasih")
        exit()
    
menu()
