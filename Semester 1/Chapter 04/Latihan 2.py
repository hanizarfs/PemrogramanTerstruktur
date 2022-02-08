# 2
def nomor1():
    print("Pak Budi melakukan perjalanan dari kota A ke kota C dengan jarak 795 km.\nApabila konsumsi 1 lt BBM digunakan untuk 12 km, maka berapa liter BBM yang harus diperlukan?")
    jarak = 795
    BBM = (jarak*1)/12
    print("Minimal Pak Budi harus mengisi BBM sebanyak", BBM,"Liter")

def nomor2():
    kota_asal = input("Kota Asal : ")
    kota_tujuan = input("Kota Tujuan : ")
    jarak = int(input("Jarak dari kota " + kota_asal + " ke kota " + kota_tujuan + "  :"))

    bbm = (jarak*1)/12
    print("Minimal anda harus menyiapkan BBM sebanyak", bbm, "Liter")
    
def kembali_ke_menu():
    menu()
    
def keluar():
    print("Terima Kasih")
    exit()
    
def menu():
    print("Halo, Selamat Datang")
    print("Soal no 2")
    print("1. Lihat hasil soal Nomor 2")
    print("2. Bagaimana dengan situasi yang lain?")
    print("3. Keluar")
    jawab = input("=>")
    if jawab == "1":
        nomor1()
        jawab = input("Kembali ke menu [y/n] ? : ")
        if jawab == "y" or "Y":
            kembali_ke_menu()
        else:
            keluar()
    elif jawab == "2":
        nomor2()
        jawab = input("Kembali ke menu [y/n] ? : ")
        if jawab == "y" or "Y":
            kembali_ke_menu()
        else:
            keluar()
    else:
        keluar()
    
menu()
