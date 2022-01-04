# Membuat header selamat datang di program
print("Selamat datang di Kalkulator IPK!")

# Membuat inisiasi agar perulangan di dalam while dapat terjadi
total_matkul = -1

# Untuk perulangan masukan selama masukan bernilai negatif
while total_matkul < 0:
    total_matkul = int(input("Masukkan jumlah mata kuliah: "))
print()

# Jika masukan bernilai 0 (dalam artian tidak ada mata kuliah diambil maka hentikan program dalam output di bawah)
if total_matkul == 0:
    print("Tidak ada mata kuliah yang diambil.")
# Ketika else -> Saat total_matkul > 0 maka lakukan program di bawah (kondisi normal perhitungan)
else:
    # Menginisiasi 4 variabel yang saya gunakan dalam perhitungan sementara dan akhir
    total_sks = 0
    total_sks_lulus = 0
    mutu_lulus = 0
    mutu_total = 0

    # Melakukan perulangan sebanyak total_matkulnya, agar lebih mudah buat range 1 sampai total_matkul+1
    for i in range(1, total_matkul + 1):

        # Membuat input yang selalu terulang sebanyak range
        # Menuliskan str(i) untuk memberi kode matkul ke berapa sesuai for
        matkul = str(input("Masukkan nama mata kuliah ke-"+str(i)+": "))
        # Menuliskan matkul yang sudah diinput di atas untuk diprint di bawah
        jumlah_sks = int(input("Masukkan jumlah SKS "+matkul+": "))
        # Menggunakan float untuk nilai karena bisa bernilai koma
        nilai = float(input("Masukkan nilai yang kamu dapatkan: "))
        # Ketika nilai bernilai negatif, maka lakukan perulangan masukan nilai
        while nilai < 0:
            print("Nilai yang kamu masukkan tidak valid")
            nilai = float(input("Masukkan nilai yang kamu dapatkan: "))
        print()

        # Membuat bentuk if-elif-else untuk rentang nilai, agar memudahkan di sini saya hanya menggunakan batas bawah
        # Di mana ketika batas bawah tidak terpenuhi, maka program berlanjut ke batas yang lebih rendah sampai ditemukan kesesuaian
        # Bobot = 4 untuk rentang 85 <= nilai < tak hingga
        if nilai >= 85:
            bobot = 4
        # Bobot = 3.7 untuk rentang 80 <= nilai < 85
        elif nilai >= 80:
            bobot = 3.7
        # Bobot = 3.3 untuk rentang 75 <= nilai < 80
        elif nilai >= 75:
            bobot = 3.3
        # Bobot = 3 untuk rentang 70 <= nilai < 75
        elif nilai >= 70:
            bobot = 3
        # Bobot = 2.7 untuk rentang 65 <= nilai < 70
        elif nilai >= 65:
            bobot = 2.7
        # Bobot = 2.3 untuk rentang 60 <= nilai < 65
        elif nilai >= 60:
            bobot = 2.3
        # Bobot = 2 untuk rentang 55 <= nilai < 60
        elif nilai >= 55:
            bobot = 2
        # Bobot = 1 untuk rentang 40 <= nilai < 55
        elif nilai >= 40:
            bobot = 1
        # Bobot = 0 untuk rentang 0 <= nilai < 40
        else:
            bobot = 0

        # Sigma(SKS * Bobot) -> Total jumlah semua yang ada
        mutu_total += (jumlah_sks * bobot)
        # Total SKS ditambah semua jumlah SKS yang ada
        total_sks += jumlah_sks

        # Sigma(SKS Lulus * Bobot) -> Untuk lulus saja (ketika bobot >= 2)
        if bobot >= 2:
            mutu_lulus += (jumlah_sks * bobot)
            # Total SKS untuk yang lulus saja (ketika bobot >= 2)
            total_sks_lulus += jumlah_sks

    # Ingat! Mutu = Sigma(SKS * Bobot)
    # Ingat dalam perhitungan matematis pembagian nol mengakibatkan error sehingga jika penyebut 0 bisa kita simpulkan tidak ada nilai yang diperoleh = 0
    # Menghitung IPK di mana rumusnya adalah (Total mutu lulus / Total SKS lulus)
    if total_sks_lulus != 0:
        ipk = mutu_lulus / total_sks_lulus
    else:
        ipk = 0
    # Menghitung IPT di mana rumusnya adalah (Total mutu total / Total SKS total)
    if total_sks != 0:
        ipt = mutu_total / total_sks
    else:
        ipt = 0

    # Membuat string formatting agar menyisakan dua angka di belakang titik
    mutu_lulus = "{:.2f}".format(mutu_lulus)
    mutu_total = "{:.2f}".format(mutu_total) 
    ipk = "{:.2f}".format(ipk)
    ipt = "{:.2f}".format(ipt)

    # Membuat hasil ouput dari operasi program di atas dengan str() agar dapat diconcatenate (+) dengan string
    print("Jumlah SKS lulus : "+str(total_sks_lulus)+" / "+str(total_sks))
    print("Jumlah mutu lulus: "+str(mutu_lulus)+" / "+str(mutu_total))
    print("Total IPK kamu adalah "+str(ipk))
    print("Total IPT kamu adalah "+str(ipt))
