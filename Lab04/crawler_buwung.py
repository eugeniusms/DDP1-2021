# Membuat masukan dari file yang ingin dimasukkan dan dihasilkan
file_masukan = input("Masukkan nama file input: ")
file_keluaran = input("Masukkan nama file output: ")

# Menginisiasi isi_file_2 yang akan menjadi output
isi_file_2 = ""
error = ""

# Melakukan pengetesan error, akan error saat tidak file masukan
try:
    # Membaca text yang masuk ke dalam operasi
    file_input = open(file_masukan)
    isi_file = file_input.read() #isi_file adalah isi yang diutak-atik
    file_input.close()

    # Menentukan error untuk file kosong
    if isi_file == "":
        error = "file kosong"

    # Mengubah string isi file menjadi list lalu membagi text dalam barisnya
    ganti_baris = list(map(str, isi_file.split("\n")))
    ganti_baris_cek = []

    # Menyelipkan "SKIP" ketika baris sudah selesai dan ingin berganti
    for baris in ganti_baris:
        ganti_baris_cek.append(baris)
        ganti_baris_cek.append(" SKIP ")

    # Mengubah list menjadi string isi file kembali agar bisa displit dengan spasi
    # Kemudian memasukannya kembali ke list dan membaginya sesuai spasi
    isi_file = ''.join(str(kata) for kata in ganti_baris_cek)
    isi_file = list(map(str, isi_file.split()))

    # Untuk "SKIP" terakhir bisa dihilangkan karena jika tidak akan terhitung 2 kali ganti baris
    isi_file.pop()

    # Menginisiasi variabel simpan dari mention, hashtag, dan url
    mention = 0
    hashtag = 0
    url = 0

    # Membuat perulangan untuk setiap setiap kata di dalam isi_file
    for i in isi_file:
        # Ketika karakter pertama dari kata == "@" hanya tuliskan "(M)" dan menambah mention +1
        if i[0] == "@":
            isi_file_2 += "(M)"
            mention += 1
        # Ketika karakter pertama dari kata == "#" hanya tuliskan "(H)" dan menambah hashtag +1
        elif i[0] == "#":
            isi_file_2 += "(H)"
            hashtag += 1
        # Ketika karakter pertama sampai keempat dari kata == "www." hanya tuliskan "(U)" dan menambah url +1
        elif i[0:4] == "www.":
            isi_file_2 += "(U)"
            url += 1
        # Ketika kata == "SKIP" lakukan pergantian baris dan continue for
        elif i == "SKIP":
            isi_file_2 += "\n"
            continue
        # Selain semua itu maka tulis seperti yang ada di dalam wujud text -> kata == i
        else:
            isi_file_2 += i

        # Setiap memasukan suatu string maka tambahkan spasi agar terpisah kecuali pada "SKIP"
        isi_file_2 += " "

    # Lakukan pencetakan dari apa yang sudah di dapat di operasi atas
    isi_file_2 += "\n###############\n"

    # Mengubah bentuk variabel menjadi string agar print dapat berjalan mudah
    mention, hashtag, url = str(mention), str(hashtag), str(url)

    # 5 - len(str(variable)) -> mengartikan tersisa beberapa spasi yang sudah terpakai sebanyak len(str(variable)) dari total 5
    isi_file_2 += "Mention : " + " "*(5-len(mention)) + mention + "\n"
    isi_file_2 += "Hashtag : " + " "*(5-len(hashtag)) + hashtag + "\n"
    isi_file_2 += "Url     : " + " "*(5-len(url)) + url + "\n"

    # Menulis text yang sudah dioperasikan ke dalam text output
    my_file = open(file_keluaran, mode='w')
    print(isi_file_2, file=my_file)
    my_file.close()
# Ketika try di atas error maka tidak ada file yang dipanggil
except FileNotFoundError:
    error = "file tidak ada"

# Print suatu kalimat yang menandakan bahwa program telah usai beserta kasus errornya jika ada
if error == "file tidak ada":
    print("File input tidak ada :(")
elif error == "file kosong":
    print("File input ada tapi kosong :(")
else:
    print("Output berhasil ditulis pada {}".format(file_keluaran))
print("Program selesai. Tekan enter untuk keluar...")
