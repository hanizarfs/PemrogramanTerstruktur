nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
nilai = []
def nilaiAkhir(mid, uas):
    for i in range(0, len(mid)):
        nilai.append((mid[i] + (2*uas[i]))/3)
    index = nilai.index(max(nilai))
    print(f'Mahasiswa yang memiliki nilai tertingi yaitu {nilaiMhs[index]["nama"]} dengan nim {nilaiMhs[index]["nim"]}')
nilaiAkhir([ sub['mid'] for sub in nilaiMhs ], [ sub['uas'] for sub in nilaiMhs ])
