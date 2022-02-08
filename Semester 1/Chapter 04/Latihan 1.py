# 1
def nomor1():
    jam_tarif_awal = 12
    tarif_awal = 200000
    tarif_lanjut = 10000
    mulai_sewa = 06.00
    akhir_sewa = 23.50
    lama_sewa = akhir_sewa-mulai_sewa
    tarif = (tarif_lanjut*(lama_sewa-jam_tarif_awal))
    total_biaya = (((lama_sewa-jam_tarif_awal)*tarif_lanjut)+tarif_awal)

    print("Mulai sewa mobil pukul                   : 06.00")
    print("Selesai sewa mobil pukul                 : 23.50")
    print("Lama sewa mobil                          :",lama_sewa,"jam")
    print("Tarif sewa mobil 12 jam pertama          : Rp.",tarif_awal)
    print("Tarif sewa mobil setelah 12 jam pertama  : Rp.",tarif_lanjut,"*",(lama_sewa-jam_tarif_awal))
    print("                                         : Rp.", tarif)
    print("----------------------------------------------------------")
    print("Total biaya sewa mobil                   : Rp.",total_biaya)
    
def nomor2():
    mulai_sewa = input("Mulai sewa mobil pukul : ")
    selesai_sewa = input("Selesai sewa mobil pukul : ")
    
    jam_tarif_awal = 12
    tarif_awal = 200000
    tarif_lanjut = 10000
    a = float(mulai_sewa)
    b = float(selesai_sewa)
    lama_sewa = (b-a)
    tarif = (tarif_lanjut*(lama_sewa-jam_tarif_awal))
    total_biaya = (((lama_sewa-jam_tarif_awal)*tarif_lanjut)+tarif_awal)

    
    if lama_sewa <= jam_tarif_awal:
        print("Lama sewa mobil                          :",lama_sewa,"jam")
        print("Tarif sewa mobil kurang dari 12 jam      : Rp.",tarif_awal)
        print("----------------------------------------------------------")
        print("Total biaya sewa mobil                   : Rp.", tarif_awal)
    else:
        print("Lama sewa mobil                          :",lama_sewa,"jam")
        print("Tarif sewa mobil 12 jam pertama          : Rp.",tarif_awal)
        print("Tarif sewa mobil setelah 12 jam pertama  : Rp.",tarif_lanjut,"*",(lama_sewa-jam_tarif_awal))
        print("                                         : Rp.", tarif)
        print("----------------------------------------------------------")
        print("Total biaya sewa mobil                   : Rp.",total_biaya)
        bayar = float(input("Pembayaran                               : Rp. "))
        hasil_bayar = (bayar-total_biaya)
        uang_kembali = (bayar-total_biaya)
        if hasil_bayar < 0:
            tunggakan = abs(hasil_bayar)
            print("Catatan                                  : Mohon maaf, uang anda masih kurang")
            print("Jumlah tunggakan                         : Rp.", tunggakan)
        else:
            print("Kembali                                  : Rp.", uang_kembali)
            print("Catatan                                  : Terima Kasih")
    

def kembali_ke_menu():
    menu()
    
def menu():
    print("Halo, Selamat Datang")
    print("Soal no 1")
    print("1. Lihat hasil soal Nomor 1")
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
