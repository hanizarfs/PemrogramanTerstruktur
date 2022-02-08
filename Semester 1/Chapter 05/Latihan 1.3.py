bi = float(input('Nilai Bahasa Indonesia : '))
mtk = float(input('Nilai Matematika : '))
ipa = float(input('Nilai IPA :'))

if (bi<0) or (mtk<0) or (ipa<0) or (bi>100) or (mtk>100) or (ipa>100):
    print("\nMaaf input ada yang tidak valid")
elif ((bi and ipa)<60) or (mtk<70):
    print("\nStatus Kelulusan                  : TIDAK LULUS")
    print('Sebab                             :')
    if bi < 60:
        print('-  Nilai Bahasa Indonesia kurang dari 60')
    if mtk < 70:
        print('-  Nilai Matematika kurang dari 60')
    if ipa < 60:
        print('-  Nilai IPA kurang dari 60')
else:
    print("\nStatus Kelulusan                  : LULUS")
