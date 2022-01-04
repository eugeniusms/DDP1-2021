"""
Nama  : Eugenius Mario Situmorang
Kelas : DDP 1-C 2021 (LAH)
Lab   : 07 (Bonus)
Program yang memudahkan dalam pemilihan kereta api berdasarkan komponen
yang ada yaitu nomor kereta, tujuan, keberangkatan, dan harga bayar kereta
"""
list_kereta = []

def info_tujuan(list_kereta):
    """
    Fungsi untuk menampilkan daftar semua tujuan yang ada di dalam masukan jadwal KA,
    Mencari daftar tujuan dalam bentuk variabel set yang mana data dalam set tidak akan 
    memiliki kembaran sehingga lebih efisien untuk assign nilai dalam set, kemudian 
    jika tujuan (lst[1]) tidak ditemukan di dalam set maka print tujuan itu
    """ 
    # *PENGGUNAAN SET*
    tujuan = set({}) 
    print("KA di stasiun ini memiliki tujuan akhir:")
    for lst in list_kereta:
        if lst[1] not in tujuan:
            print(lst[1])
        tujuan.add(lst[1])
        
def tujuan_kelas(list_kereta, tujuan_akhir, kelas_kereta, harga):
    """
    Fungsi untuk mendapatkan daftar kereta dengan tujuan dan kelas tertentu. Pertama-tama
    memecah dahulu isi dari list_kereta ke dalam komponennya masing-masing seperti yang
    sudah dijelaskan dalam fungsi main(). Kemudian untuk kelas_kereta dapat dicek dari 
    indeks pertama pada komponen nomor kereta. Setelah itu jika indeks pertama nomor kereta
    dan tujuan kereta sudah sesuai,maka cetak daftarnya ke terminal.
    """
    jumlah = 0
    kereta_cek, harga_cek = [], []
    # Memperoleh nomor depan dengan menggunakan dictionary get() method
    # *PENGGUNAAN DICTIONARY*
    kelas = {"Eksekutif" : "1", "Bisnis" : "2", "Ekonomi" : "3"}
    nomor_depan = kelas.get(kelas_kereta)
    # Jika input tidak sesuai kelas yang disediakan
    if kelas_kereta not in kelas.keys():
        print("Kelas yang dipilih kurang sesuai, harap pilih : Eksekutif, Bisnis, atau Ekonomi\n")
        isi_perintah(list_kereta)
        pass

    # Mengambil komponen setiap data keberangkatan dan mencocokannya sesuai input user 
    for lst in list_kereta:
        nomor_kereta, tujuan_kereta, jam_kereta, harga_tiket = lst[0], lst[1], int(lst[2]), int(lst[3])
        if nomor_kereta[0] == nomor_depan and tujuan_kereta == tujuan_akhir:
            if harga == "normal":
                print(f"KA {nomor_kereta} berangkat pukul {jam_kereta} dengan harga tiket {harga_tiket}")
            if harga == "murah":
                kereta_cek.append(lst)
                harga_cek.append(int(lst[3]))
            jumlah += 1
    if not jumlah:
        print("Tidak ada jadwal KA yang sesuai.")

    # Mencetak hasil dengan harga termurah berdasarkan harga terkecil dari kereta yang sudah difilter sesuai tujuan dan kelasnya
    if harga == "murah":
        harga_min = min(harga_cek)
        for lst in kereta_cek:
            nomor_kereta, tujuan_kereta, jam_kereta, harga_tiket = lst[0], lst[1], int(lst[2]), int(lst[3])
            if harga_tiket == harga_min:
                print(f"KA {nomor_kereta} berangkat pukul {jam_kereta} dengan harga tiket {harga_tiket}")

def tujuan_jam(list_kereta, tujuan_akhir, jam_keberangkatan, harga):
    """
    Fungsi untuk mendapatkan daftar kereta dengan tujuan dan kelas tertentu. Pertama-tama
    memecah dahulu isi dari list_kereta ke dalam komponennya masing-masing seperti yang
    sudah dijelaskan dalam fungsi main(). Setelah itu jika tujuan kereta sudah sesuai dan
    jam kereta <= jam_keberangkatan (inklusif), maka cetak daftarnya ke terminal.
    """
    jumlah = 0
    kereta_cek, harga_cek = [], []
    jam_keberangkatan = int(jam_keberangkatan)
    # Jika input tidak sesuai range jam, jam > 24 atau jam < 0
    if jam_keberangkatan > 24 or jam_keberangkatan < 0:
        print("Jam keberangkatan yang dipilih kurang sesuai, harap pilih range (0-24)\n")
        isi_perintah(list_kereta)
        pass

    # Mengambil komponen setiap data keberangkatan dan mencocokannya sesuai input user 
    for lst in list_kereta:
        nomor_kereta, tujuan_kereta, jam_kereta, harga_tiket = lst[0], lst[1], int(lst[2]), int(lst[3])
        if tujuan_kereta == tujuan_akhir and jam_kereta <= jam_keberangkatan:
            if harga == "normal":
                print(f"KA {nomor_kereta} berangkat pukul {jam_kereta} dengan harga tiket {harga_tiket}")
            if harga == "murah":
                kereta_cek.append(lst)
                harga_cek.append(int(lst[3]))
            jumlah += 1
    if not jumlah:
        print("Tidak ada jadwal KA yang sesuai.")

    # Mencetak hasil dengan harga termurah berdasarkan harga terkecil dari kereta yang sudah difilter sesuai tujuan dan jamnya
    if harga == "murah":
        harga_min = min(harga_cek)
        for lst in kereta_cek:
            nomor_kereta, tujuan_kereta, jam_kereta, harga_tiket = lst[0], lst[1], int(lst[2]), int(lst[3])
            if harga_tiket == harga_min:
                print(f"KA {nomor_kereta} berangkat pukul {jam_kereta} dengan harga tiket {harga_tiket}")

def isi_perintah(list_kereta):
    """
    Fungsi yang berisi pengambilan input perintah yang dipanggil pada setiap
    kali perintah diperlukan program. User memilih input yang sesuai dengan
    keterangan yang sudah dijelaskan dalam poin 1-4 dalam fungsi main().
    """
    while True:
        perintah = input("Masukkan perintah: ").split() # Membagi perintah ke dalam beberapa indeks list
            
        """
        Melakukan pencocokan data perintah yang diambil melalui if-else kemudian memanggil
        fungsi yang sesuai untuk mengeksekusi program yang akan berjalan.
        indeks [0] => perintah yang diambil
        indeks [1] => tujuan akhir
        indeks [2] => properti sesuai perintah, contoh <kelas_kereta> atau <jam_keberangkatan>
        kemudian menyesuaikan jumlah indeks komponen yang dimasukkan juga harus sesuai
        ketentuan, jika tidak maka cetak tidak valid.
        """
            
        # Jika perintah kosong maka ulang isi perintah (tidak valid)
        # Jika mode termurah maka isi argumen -> "murah", jika kondisi normal -> "normal"
        if len(perintah) == 0:
            print("Perintah yang dimasukkan tidak valid.")
        elif perintah[0] == "INFO_TUJUAN" and len(perintah) == 1:
            info_tujuan(list_kereta)
        elif perintah[0] == "TUJUAN_KELAS" and len(perintah) == 3:
            tujuan_kelas(list_kereta, perintah[1], perintah[2], "normal")
        elif perintah[0] == "TUJUAN_KELAS_TERMURAH" and len(perintah) == 3:
            tujuan_kelas(list_kereta, perintah[1], perintah[2], "murah")
        elif perintah[0] == "TUJUAN_JAM" and len(perintah) == 3:
            tujuan_jam(list_kereta, perintah[1], int(perintah[2]), "normal")
        elif perintah[0] == "TUJUAN_JAM_TERMURAH" and len(perintah) == 3:
            tujuan_jam(list_kereta, perintah[1], int(perintah[2]), "murah")
        elif perintah[0] == "EXIT":
            print("Terima kasih sudah menggunakan program ini!")
            break
        else:
            print("Perintah yang dimasukkan tidak valid.")
        print()

def main():
    """
    Fungsi inisiasi di mana fungsi ini menjadi bagian utama dari program dan
    akan diulang selama program berjalan (berfungsi sebagai menu sebuah program).
    """
    global list_kereta
    print("Selamat datang! Silakan masukkan jadwal KA:")

    # Mengambil input dari user secara berulang sampai input == "selesai"
    # *PENGGUNAAN (LIST)*    
    while True:
        kereta = input()
        if kereta == "selesai":
            break
        # Membentuk list dimensi dua pada setiap input 
        # Sehingga didapati bentuk [[nomor, tujuan, jam, harga],[...],...]
        list_kereta.append(kereta.split()) 

    """
    Mengecek kemungkinan error menggunakan try-except dan "human error" dari pengetikan format
    1. Jika terdapat indeks list kosong dalam list_kereta maka raise error index dan isi ulang jadwal
    2. Raise error juga saat len(lst) lebih maupun kurang dari yang seharusnya yaitu 4 komponen per kereta
    3. Raise issue saat format nomor ka (lst[0]) di luar range 100-399
    4. Raise issue saat jam(lst[2]) jam > 23 atau jam < 0 
    5. Raise issue saat harga (minus) lst[3] < 0
    """
    error_1, error_2, error_3, error_4 = 0, 0, 0, 0
    format_error = 0
    try:
        for lst in list_kereta:
            if lst[0] == "" or lst[1] == "" or lst[2] == "" or lst[3] == "" or len(lst) != 4:
                raise IndexError
            nomor_ka = int(lst[0])
            if nomor_ka > 399 or nomor_ka < 100: # Identifikasi kesalahan
                if format_error == 0: # Identifikasi jumlah salah
                    print()
                error_1 += 1 # Menghitung kesalahan di kasus ini untuk dicetak di print bawah
                print(f"[!] Ditemukan format nomor kereta tak sesuai ({error_1})")
                format_error += 1 # Menghitung semua total kesalahan yang ada
            jam_ka = int(lst[2])
            if jam_ka > 23 or jam_ka < 0:
                if format_error == 0:
                    print()
                error_2 += 1
                print(f"[!] Ditemukan format jam kereta tak sesuai ({error_2})")
                format_error += 1
            harga_ka = int(lst[3])
            if harga_ka < 0:
                if format_error == 0:
                    print()
                error_3 += 1
                print(f"[!] Ditemukan harga kereta tak sesuai ({error_3})")
                format_error += 1
    except IndexError:
        if format_error == 0:
            print()
        error_4 += 1
        print(f"[!] Ditemukan jadwal kosong atau format jadwal tak sesuai ({error_4})")
        format_error += 1
    if format_error > 0:
        # Reset all
        print("Silakan isi ulang jadwal!\n")
        format_error = 0
        list_kereta.clear()
        main()

    # Membuat daftar menu pada tampilan program saat berjalan dan mengambil perintahnya
    print("\nPerintah yang tersedia:")
    print("1. INFO_TUJUAN")
    print("2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>")
    print("3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>")
    print("4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>")
    print("5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>")
    print("6. EXIT\n")
    isi_perintah(list_kereta)

main()
