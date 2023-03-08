def ganti_kata(kalimat, cari, ganti):
    kalimat_baru = ""
    kata = ""
    for i in range(len(kalimat)):
        if kalimat[i] == " ":
            if kata == cari:
                kalimat_baru += ganti + " "
            else:
                kalimat_baru += kata + " "
            kata = ""
        else:
            kata += kalimat[i]
    if kata == cari:
        kalimat_baru += ganti
    else:
        kalimat_baru += kata
    return kalimat_baru
kalimat = input('Masukkan kalimat: ')
cari = input('Kata yang dicari: ')
ganti = input('Diganti menjadi: ')
kalimat_baru = ganti_kata(kalimat, cari, ganti)
print(kalimat_baru)
