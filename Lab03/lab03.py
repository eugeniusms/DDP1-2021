# Memberi masukan ke dalam 2 variabel
himpunan_a = str(input("Masukkan input himpunan A: "))
himpunan_b = str(input("Masukkan input himpunan B: "))

# Menghitung jumlah koma dalam kalimat
koma_a = himpunan_a.count(",") 
koma_b = himpunan_b.count(",") 

# Untuk mengetahui banyaknya pasangan sehingga bisa menentukan titik akhir
total = (koma_a + 1) * (koma_b + 1)
hitung = 1

# Menginisiasi indeks untuk mencari indeks koma
indeks, indeks_b = -1, -1
indeks_koma_b = ""

# Membuat program tampilan keluaran
output = "{"

for i in range(koma_a + 1):
    # Membuat indeks start dan end untuk pemotongan string A, indeks terakhir adalah saat koma + 1
    indeks_terakhir = indeks + 1
    indeks = himpunan_a.find(",", indeks + 1)
    
    for j in range(koma_b + 1):
        # Mengawali pemotongan dengan indeks terekam koma terakhir + 1
        # Memunculkan nilai A, jika indeks = -1 ketika tidak ada koma lagi maka end di akhir
        # Jika tidak, maka end saja di indeks koma (eksklusif)
        if indeks == -1:
            output += "(" + himpunan_a[indeks_terakhir:] + ","
        else:
            output += "(" + himpunan_a[indeks_terakhir : indeks] + ","

        # Membuat indeks start dan end untuk pemotongan string B, indeks terakhir adalah saat koma + 1
        indeks_terakhir_b = indeks_b + 1
        indeks_b = himpunan_b.find(",", indeks_b + 1)

        # Mengawali pemotongan dengan indeks terekam koma terakhir + 1
        # Memunculkan nilai B, jika indeks = -1 ketika tidak ada koma lagi maka end di akhir
        # Jika tidak, maka end saja di indeks koma (eksklusif)
        if indeks_b == -1:
            output += himpunan_b[indeks_terakhir_b:]
            # Mengakhiri jawaban agar tidak ada bentuk "), }" di akhir
            if hitung == total:
                output += ")"
            else:
                output += "), "
        else:
            output += himpunan_b[indeks_terakhir_b : indeks_b]
            # Mengakhiri jawaban agar tidak ada bentuk "), }" di akhir
            if hitung == total:
                output += ")"
            else:
                output += "), "
        
        # Menghitung sejauh mana program berjalan
        hitung += 1

    # Untuk reset ulang indeks awal dari himpunan b
    indeks_b = -1

print("A x B = " + output + "}")
# Catatan : Selama program berjalan, saya menambahkan output dengan string yang sesuai diminta soal
#           contohnya seperti : "(", ",", ")" oleh karena itu saya menggunakan string penuh pada program ini
