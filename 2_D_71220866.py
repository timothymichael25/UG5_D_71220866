def hitung_mobil():
    jumlah_kendaraan_mobil = {k: 0 for k in ['Solo', 'Surabaya', 'Jogja', 'Magelang']}
    
    while True:
        asalMobil = input("Masukkan asal mobil (ketik 'Done' untuk keluar): ").capitalize()
        
        if asalMobil == 'Done':
            break
        if asalMobil in jumlah_kendaraan_mobil:
            jumlah_kendaraan_mobil[asalMobil] += 1
        else:
            print("Asal mobil tidak valid!")
    for asalKota, jumlah in jumlah_kendaraan_mobil.items():
        print("Jumlah mobil dari {}: {}".format(asalKota, jumlah))

hitung_mobil()