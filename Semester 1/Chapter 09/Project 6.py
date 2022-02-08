nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*70)
print('NIM'.ljust(10)+'NAMA'.ljust(20)+'N.MID'.ljust(10)+'N.UAS'.ljust(10)+'N.AKHIR'.ljust(10)+'STATUS'.ljust(15))
print('-'*70)
for i in range(len(nilai)):
    nAkhir = round((((nilai[i]['mid'])+(2*(nilai[i]['uas'])))/3), 2)
    if nAkhir >= 60:
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print(nilai[i]['nim'].ljust(10) + nilai[i]['nama'].ljust(20) + str(nilai[i]['mid']).ljust(10) + str(nilai[i]['uas']).ljust(10)+str(nAkhir).ljust(10)+status.ljust(15))
print('='*70)
