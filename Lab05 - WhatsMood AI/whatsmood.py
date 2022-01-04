# Memberi input nama sebuah file untuk diproses
file_masukan = input("Masukkan nama file input: ")

# Mengecek keadaan error saat file tidak ada
try:
    # Membaca isi file dan menuliskan pada sebuah variabel isi_file
    my_file = open(file_masukan)
    isi_file = my_file.read()
    my_file.close()

    # Apabila file ada tetapi tidak berisi maka print sebagai berikut
    if isi_file == "":
        print("File input ada tapi kosong :(")
    # Apabila file terdapat isi maka jalankan program normal di bawah
    else:
        # Menginisiasi list isi_baru dan memecah isi_file per baris 
        isi_baru = []
        isi_file = isi_file.split("\n")

        # Membuat variabel list 2 dimensi untuk menambahkan penanda setiap ganti baris pada dimensi 1, pada dimensi 2 berisi isi dari kalimat
        for baris in isi_file:
            isi_baru.append(baris.split())
            isi_baru.append("gantibaris")
        # Kembalikan variabel ke variabel awal agar penggunaan variabel konstan
        isi_file = isi_baru
        
        # Menginisiasi variabel perhitungan
        total_smile = 0
        total_sad = 0
        total_angry = 0
        kalimat_cek = []

        # Membuat 2 parameter fungsi untuk indeks kalimat dalam isi_file dan kata dalam kalimat
        # Ubah isi list dua dimensi untuk isi_file dengan emoticon
        # Hanya menambahkan nilai dari Pak Chanek saja ketika kalimat_cek[0] + kalimat_cek[1] == "Pak" + "Chanek:"
        def smile(kalimat, kata):
            global total_smile , kalimat_cek
            isi_file[kalimat][kata] = "\U0001f603"
            if kalimat_cek[0] == "Pak" and kalimat_cek[1] == "Chanek:":
                total_smile += 1

        def sad(kalimat, kata):
            global total_sad, kalimat_cek
            isi_file[kalimat][kata] = "\U0001f622"
            if kalimat_cek[0] == "Pak" and kalimat_cek[1] == "Chanek:":
                total_sad += 1

        def angry(kalimat, kata):
            global total_angry, kalimat_cek
            isi_file[kalimat][kata] = "\U0001f621"
            if kalimat_cek[0] == "Pak" and kalimat_cek[1] == "Chanek:":
                total_angry += 1

        # Melakukan perulangan untuk setiap kalimat (dimensi 1 list)
        for kalimat in isi_file:
            kalimat_cek = kalimat
            # Melakukan perulangan untuk setiap kata (dimensi 2 list)
            for kata in kalimat:
                if kata == "(smile)":
                    # Jika terdapat kesamaan maka lakukan fungsi smile(kalimat, kata)
                    smile(isi_file.index(kalimat),list(kalimat).index(kata))
                elif kata == "(sad)":
                    sad(isi_file.index(kalimat),list(kalimat).index(kata))
                elif kata == "(angry)":
                        angry(isi_file.index(kalimat),list(kalimat).index(kata))
                else:
                    # Jika tidak ada maka lakukan iterasi selanjutnya
                    continue
        
        # Membuat output dengan mengidentifikasi gantibaris untuk pergantian baris
        print()
        for kalimat in isi_file:
            if kalimat == "gantibaris":
                print()
            else:
                # Jika tidak maka setiap isi list dapat dijoin ke string kalimat
                kalimat = " ".join(str(kata) for kata in kalimat)
                print(kalimat, end = "")

        # Membuat fungsi output kesimpulan
        def kesimpulan(happiness, sadness, anger):
            # Memasukkan parameter fungsi ke dalam list data untuk memudahkan perhitungan
            data = [happiness, sadness, anger]
            kesimpulan = ["bahagia", "sedih", "marah"]
            # Mencari nilai max dari data
            maks = max(data)
            indeks_maks = []

            # Mencari nilai max itu ada di indeks ke berapa
            for i in range(len(data)):
                if data[i] == maks:
                    indeks_maks.append(i)
            
            # Membuat if-else di mana ada 3 kemungkinan:
            # Jika max ada 1 maka langsung saja print return indeks dari max
            # Jika max ada 2 maka langsung saja print return indeks dari max sejumlah 2 (list pasti terurut dari depan)
            # JIka max ada 3 maka langsung saja print tidak dapat disimpulkan
            print("\n##### Kesimpulan #####")
            if len(indeks_maks) == 1:
                print("Pak Chanek sedang {}.".format(kesimpulan[indeks_maks[0]]))
            elif len(indeks_maks) == 2:
                print("Pak Chanek sedang {} atau {}.".format(kesimpulan[indeks_maks[0]], kesimpulan[indeks_maks[1]]))
            else:
                print("Kesimpulan tidak ditemukan.")

        # Membuat fungsi dari pengukuran
        def ukur():
            print("\nMengukur suasana hati....\n\n##### Hasil Pengukuran #####")
            # Melakukan perhitungan poin di dalam fungsi smile, sad, angry yang sudah ada dengan settingan pdf lab dan start poin 50
            happiness = 50 + (total_smile * 9) - (total_angry * 5)
            sadness = 50 + (total_sad * 10) - (total_smile * 6)
            anger = 50 + (total_angry * 13) - (total_sad * 8)

            # Membuat batas minimal 0 dan maksimal 100
            perasaan = [happiness, sadness, anger]
            for i in range(len(perasaan)):
                if perasaan[i] > 100:
                    perasaan[i] = 100
                if perasaan[i] < 0:
                    perasaan[i] = 0
            # Mengembalikan nilai variabel dari bentuk list
            happiness, sadness, anger = perasaan[0], perasaan[1], perasaan[2]

            # Membuat print dari setiap nilai ekspresi
            print("Happiness = {} | Sadness = {} | Anger = {}".format(happiness, sadness, anger))
            # Memanggil fungsi kesimpulan dengan argumen ketiga ekspresi
            kesimpulan(happiness, sadness, anger)

        # Memanggil fungsi ukur untuk dijalankan
        ukur()

except FileNotFoundError:
    # Membuat print jika tidak ada file ditemukan -> error FileNotFound
    print("File input tidak ada :(")
