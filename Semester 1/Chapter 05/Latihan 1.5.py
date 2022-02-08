import string
import random
import time


# ID / KODE KARYAWAN GENERATOR =======================================================================================
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
# ====================================================================================================================
# TANYA AKUN =========================================================================================================
def tanya_akun():
    tanya = input("Yakin sudah mempunyai akun [y/t] ? : ")
    print("==============================================")
    if tanya == 'Y' or tanya == 'y':
        return masuk()
    elif tanya == 'T' or tanya == 't':
        return start()
    else:
        return keluar()   
# ====================================================================================================================
# TANYA MASUK ========================================================================================================
def tanya_masuk():
    tanya = input('Lanjutkan untuk masuk [y/t] ? : ')
    if tanya == 'Y' or tanya == 'y':
        return masuk()
    elif tanya == 'T' or tanya == 't':
        return keluar()
    else:
        print('Pilihan tidak diketahui')
        print('Masukkan kembali pilihan dengan benar')
        return tanya_masuk()
# ====================================================================================================================
# MASUK AKUN =========================================================================================================
def masuk():
    user = input('Nama Pengguna / Kode Karyawan : ')
    passwrd = input('Kata Sandi : ')
    if ((user == nama) or (user == kode)) and (passwrd == pswd):
        return menu()
    else:
        print('Salah')
        return masuk()
# ====================================================================================================================
# DAFTAR AKUN ========================================================================================================
def daftar():
    # GLOBAL =========================================================================================================
    global nama
    global gol
    global kode
    global pswd
    
    # PROGRAM ========================================================================================================
    nama = input('Nama : ')
    print('Golongan : A - B - C - D')
    gol = input('Golongan : ')
    if gol == 'A' or gol == 'a':
        pass
    elif gol == 'B' or gol == 'b':
        pass
    elif gol == 'C' or gol == 'c':
        pass
    elif gol == 'D' or gol == 'd':
        pass
    else:
        print('Golongan yang dimasukkan tidak diketahui')
        print('Mohon maaf anda harus keluar dari program ini')
        return start()
    pswd_palsu = input('Kata Sandi : ')
    pswd = input ('Verifikasi Kata Sandi : ')
    if pswd_palsu == pswd:
        pass
    else:
        print('Kata Sandi yang dimasukkan salah')
        print('Mohon maaf anda harus keluar dari program ini')
        return start()
    kode = id_generator()
    print('Kode Karyawan :', kode)
    return tanya_masuk()
    return #Selesai
# ====================================================================================================================
# DATA GAJI KARYAWAN =================================================================================================
def data_gaji_krywn():
    print("Data Gaji Karyawan")
    print("=============================================")
    print('| No | Golongan |   Gaji  Pokok  | Potongan |')
    print('---------------------------------------------')
    print('| 01 |     A    | Rp. 10.000.000 |   2.5 %  |')
    print('| 02 |     B    | Rp. 8.500.000  |   2.0 %  |')
    print('| 03 |     C    | Rp. 7.000.000  |   1.5 %  |')
    print('| 04 |     D    | Rp. 5.500.000  |   1.0 %  |')
    print("=============================================")
# ====================================================================================================================
# TANYA GAJI KARYAWAN ================================================================================================
def tanya_cek_gaji_krywn():
    tanya = input('Ulangi lagi [y/t] ? : ')
    if tanya == 'y' or tanya == 'Y':
        return cek_gaji_krywn()
    elif tanya == 't' or tanya == 'T':
        tanya = input('Kembali ke menu [y/t] ? : ')
        if tanya == 'y' or tanya == 'Y':
            return menu()
        elif tanya == 't' or tanya == 'T':
            return exit()
        else:
            print('Pilihan tidak diketahui')
            print('Masukkan kembali pilihan dengan benar')
            return cek_gaji_krywn
    else:
        print('Pilihan tidak diketahui')
        print('Masukkan kembali pilihan dengan benar')
        return cek_gaji_krywn
# ====================================================================================================================
# TANYA GAJI KARYAWAN ================================================================================================
def cek_gaji_krywn():
    # GLOBAL =========================================================================================================
    global gaji_pk
    global p
    global pt
    # PROGRAM ========================================================================================================  
    code = input('Kode Karyawan            : ')
    name = input('Nama Karyawan            : ')
    golongan = input('Golongan Karyawan (A - D): ')
    if ((code == kode) and (name == nama) and (golongan == gol)):
        pass
    else:
        print('Data tidak diketahui')
        print('Mohon maaf, Anda harus kembali ke Menu')
        return menu()
    if golongan == 'A' or golongan == 'a':
        gaji_pk = 10000000
        p = '2.5%'
        pt = 0.025
    elif golongan == 'B' or golongan == 'b':
        gaji_pk = 8500000
        p = '2%'
        pt = 0.02
    elif golongan == 'C' or golongan == 'c':
        gaji_pk = 7000000
        p = '1.5%'
        pt = 0.015
    elif golongan == 'D' or golongan == 'd':
        gaji_pk = 5500000
        p = '1%'
        pt = 0.01
    else:
        print('Hanya ada 4 Golongan saja [A, B, C, D]')
    nikah = input('Sudah menikah [y/t] ? :')
    if nikah == 'y' or nikah == 'Y':
        global anak
        anak = int(input('Punya anak berapa [0 jika belum mempunyai anak] : '))
        return tanya_struk_nikah()
    else:
        return tanya_struk()
# ====================================================================================================================
# TANYA STRUK ========================================================================================================
def tanya_struk():
    tanya = input('Cetak Struk Gaji [y/t] ? : ')
    if tanya == 'Y' or tanya == 'y':
        return struk()
    elif tanya == 'T' or tanya == 't':
        return tanya_menu()
    else:
        print('Pilihan tidak diketahui')
        print('Masukkan kembali pilihan dengan benar')
        return cek_gaji_krywn()
    
def tanya_struk_nikah():
    tanya = input('Cetak Struk Gaji [y/t] ? : ')
    if tanya == 'Y' or tanya == 'y':
        return struk_nikah()
    elif tanya == 'T' or tanya == 't':
        return tanya_menu()
    else:
        print('Pilihan tidak diketahui')
        print('Masukkan kembali pilihan dengan benar')
        return cek_gaji_krywn()
# ====================================================================================================================            
def struk():
    # GLOBAL =========================================================================================================
    global potongan
    global gaji_bs
    # RUMUS ==========================================================================================================
    potongan = gaji_pk*pt
    gaji_bs = gaji_pk-(potongan)
    # STRUK GAJI =====================================================================================================
    print("==============================================")
    print("         STRUK RINCIAN GAJI KARYAWAN          ")
    print("==============================================")
    print('Nama Karyawan            : ' + nama)
    print('Golongan                 : ' + gol)
    print('---------------------------------------------')
    print('Gaji Pokok               : Rp.', gaji_pk)
    print('Potongan ' + p + '            : Rp.', potongan)
    print('------------------------------------------  -')
    print('Gaji Bersih              : Rp.', gaji_bs)
    print("==============================================")
def struk_nikah():
    # GLOBAL =========================================================================================================
    global tjI
    global tjA
    global potongan
    global gaji_bs
    # RUMUS ==========================================================================================================
    tjI = 0.1*gaji_pk
    tjA = 0.05*anak*gaji_pk
    potongan = gaji_pk*pt
    gaji_ktr = gaji_pk+tjI+tjA
    gaji_bs = gaji_ktr-(potongan)
    # STRUK GAJI =====================================================================================================
    print("==============================================")
    print("         STRUK RINCIAN GAJI KARYAWAN          ")
    print("==============================================")
    print('Nama Karyawan            : ' + nama)
    print('Golongan                 : ' + gol)
    print('---------------------------------------------')
    print('Gaji Pokok               : Rp.', gaji_pk)
    print('Tunjangan Istri/Suami    : Rp.', tjI)
    print('Tunjangan Anak           : Rp.', tjA)
    print('---------------------------------------------')
    print('Gaji kotor               : Rp.', gaji_ktr)
    print('Potongan ' + p + '            : Rp.', potongan)
    print('------------------------------------------  -')
    print('Gaji Bersih              : Rp.', gaji_bs)
    print("==============================================")
# ====================================================================================================================
# KELUAR =============================================================================================================
def keluar():
    print("==============================================")
    print('==         T E R I M A   K A S I H          ==')
    print("==============================================")
    return exit()
# ====================================================================================================================
# TANYA MENU =========================================================================================================
def tanya_menu():
    tanya = input('Kembali ke menu [y/t] ? : ')
    if tanya == 'Y' or tanya == 'y':
        return menu()
    elif tanya == 't' or tanya == 'T':
        return keluar()
    else:
        print('Data tidak diketahui')
        print('Mohon maaf, Anda harus kembali ke Menu')
# ====================================================================================================================
# MENU ===============================================================================================================
def menu():
    print('1. Data Gaji Karyawan')
    print('2. Cek Gaji Karyawan')
    print('3. Logout')
    pilih = input('=> ')
    if pilih == "1":
        return data_gaji_krywn()
        return tanya_menu()
    elif pilih == "2":
        return cek_gaji_krywn()
        return tanya_menu()
    elif pilih == "3":
        return keluar()
    else:
        print('Pilihan tidak diketahui')
        print('Masukkan kembali pilihan dengan benar')
# ====================================================================================================================
# START FUNCTION =====================================================================================================
def start():
    while True:
        print("==============================================")
        print("==       S E L A M A T    D A T A N G       ==")
        print("==============================================")
        print('1. Masuk')
        print('2. Daftar')
        print('3. Keluar\n')
        print("==============================================")
        pilih = input('=> ')
        print("==============================================")
        if pilih == '1':
            print("==============================================")
            print("==       S E L A M A T    D A T A N G       ==")
            print("==============================================\n")
            return tanya_akun()
            break
        elif pilih == '2':
            daftar()
            break
        elif pilih == '3':
            break
        else:
            print('Pilihan tidak diketahui')
            print('Masukkan kembali pilihan dengan benar')
# ====================================================================================================================
# START PROGRAM ======================================================================================================
if __name__=='__main__':
    start()
# ====================================================================================================================
