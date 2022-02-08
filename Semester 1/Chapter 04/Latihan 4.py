# 4
jarak_A_ke_B = 125
rata_A_ke_B = 62
waktu_A_ke_B = (jarak_A_ke_B/rata_A_ke_B)
konvert_A_ke_B = (waktu_A_ke_B*60)
a_b = (round(konvert_A_ke_B, 2))

istirahat = 45
konvert_istirahat = 45/60

jarak_B_ke_C = 256
rata_B_ke_C = 70
waktu_B_ke_C = (jarak_B_ke_C/rata_B_ke_C)
konvert_B_ke_C = waktu_B_ke_C*60
b_c = (round(konvert_B_ke_C, 2))

berangkat = 06.00
# print(berangkat)

lama = (a_b+istirahat+b_c)
konvert_lama = (round((lama/60), 2))

sampai = (konvert_lama+berangkat)

print("""
Jarak dari Kota A -> B     : 125 Km
Kecepatan rata rata A -> B : 62 Km/Jam.
Istirahat di Kota B        : 45 menit
Jarak Kota B ke Kota C     : 256 km
Kecepatan rata-rata B -> C : 70 km/jam
""")
print("Jika pengendara berangkat pukul 06.00 WIB.\nMaka dia sampai di Kota C pada pukul :", sampai)
