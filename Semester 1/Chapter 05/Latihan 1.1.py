bi = float(input('Nilai Bahasa Indonesia : '))
mtk = float(input('Nilai Matematika : '))
ipa = float(input('Nilai IPA :'))

if (bi<0) or (mtk<0) or (ipa<0) or (bi>100) or (mtk>100) or (ipa>100):
    print("\nMaaf input ada yang tidak valid")
elif ((bi and ipa)<60) or (mtk<70):
    print("\nStatus Kelulusan                  : TIDAK LULUS")
else:
    print("\nStatus Kelulusan                  : LULUS")
