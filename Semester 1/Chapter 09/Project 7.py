mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print('='*60,'\nNIM'.ljust(8)+'NAMA MAHASISWA'.ljust(25)+'TGL LAHIR'.ljust(15)+'TEMPAT LAHIR'.ljust(10))
print('-'*60)
for j in mhs:
    data = []
    data.extend(j.split(':'))
    newTgl = data[2].replace('-', '/')
    newDataMhs = data.pop(2) and data.insert(2, newTgl)
    print(data[0].ljust(8)+data[1].ljust(24)+data[2].ljust(15)+data[3].ljust(10))
print('='*60)
