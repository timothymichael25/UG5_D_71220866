import math

while True:
    jarak_awal = input("Masukkan jarak awal (dalam meter): ")
    if jarak_awal.lower() == "berhenti" or jarak_awal.lower() == "stop":
        break
    sudut1 = input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat): ")
    sudut2 = input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat): ")
    try:
        jarak_awal = float(jarak_awal)
        sudut1 = math.radians(float(sudut1))
        sudut2 = math.radians(float(sudut2))
        tinggi_awal = jarak_awal * math.tan(sudut1)
        jarak_akhir = jarak_awal * math.tan(sudut2) - jarak_awal * math.tan(sudut1)
        selisih_ketinggian = jarak_akhir * math.tan(sudut2)
        print("Ketinggian drone pada menit ke-5 adalah ", tinggi_awal, "meter")
        print("Selisih ketinggian drone pada menit ke-5 dan ke-8 adalah ", selisih_ketinggian, "meter")
    except ValueError:
        print("Input yang dimasukkan tidak valid. Masukkan kembali.")