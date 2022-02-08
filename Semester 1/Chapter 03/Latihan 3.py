# 3
# import Library
import time
# import datetime

# # Input nama user
# nama = input('Halo... nama saya Mr. Kompie, nama Anda siapa? ')

# # Tampilkan nama user
# print("Oh... nama Anda", nama, ", nama yang bagus sekali.")

# # Kasih jeda 3 detik
# time.sleep(3)

# # Input tahun lahir
# thnLahir = int(input("BTW... " + nama + " kamu lahir tahun berapa? "))

# # Kasih jeda 3 detik
# time.sleep(3)

# # Hitung usia user
# skrng = datetime.datetime.now()
# usia = skrng.year + thnLahir

# # Tampilkan usia
# print('Hmmm...', namax, "kamu sudah", usia, "tahun ya...")

# # Kasih jeda 3 detik
# time.sleep(3)

# # Tampilkan pesan sesuai range usia
# if (usia > 50):
#     print("Anda sudah cukup tua ya")
#     print("Jaga kesehatan ya!!")
# elif (usia > 20):
#     print("Ternyata Anda masih cukup muda belia")
#     print("Jangan sia-siakan masa mudamu ya!!")
# elif (usia > 17):
#     print("Hihihi... Anda ternyata masih ABG")
#     prnint("Mulai berpikirlah secara dewasa ya!!")
# else:
#     print("Oalah... Anda masih anak anak toh?")
#     print("Jangan suka merengek-rengek minta jajan ya!!")
           
# # Kasih jeda 3 detik
# time.sleep(3)

# # Say Goodbye
# print("Ok.. see you later", nama, ".. senang berkenalan denganmu")


# MODIFIKASI
import datetime

# Input nama user
nama = input('Halo... nama saya Mr. Kompie, nama Anda siapa? ')

# Tampilkan nama user
print("Oh... nama Anda", nama, ", nama yang bagus sekali.")

# Kasih jeda 3 detik
time.sleep(3)

# Input tahun lahir
thnLahir = int(input("BTW... " + nama + " kamu lahir tahun berapa? "))

# Kasih jeda 3 detik
time.sleep(3)

# Hitung usia user
skrng = datetime.datetime.now()
usia = skrng.year - thnLahir

# Tampilkan usia
print('Hmmm...', nama, "kamu sudah", usia, "tahun ya...")

# Kasih jeda 3 detik
time.sleep(3)

# Tampilkan pesan sesuai range usia
if (usia > 50):
    print("Anda sudah cukup tua ya")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
else:
    print("Oalah... Anda masih anak anak toh?")
    print("Jangan suka merengek-rengek minta jajan ya!!")
           
# Kasih jeda 3 detik
time.sleep(3)

# Say Goodbye
print("Ok.. see you later", nama, ".. senang berkenalan denganmu")
