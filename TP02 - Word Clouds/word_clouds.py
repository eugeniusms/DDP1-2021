import string
import html_functions

# file_masukan = input("Silakan masukan nama file: ")
file_masukan = "CommencementSpeechByGates2014.txt"
file_keluaran = file_masukan + ".html"

# READ IN FILE INPUT
file_input = open(file_masukan)
isi_file = file_input.read() #isi_file adalah isi yang diutak-atik
file_input.close()

# Mengecilkan huruf pada paragraf agar pencarian dan pencocokan lebih mudah
isi_file = isi_file.lower()
kata = isi_file.split()
print(kata)

# Untuk menghilangkan tanda baca 
isi_file_bersih = isi_file.translate(str.maketrans('', '', string.punctuation))

print(isi_file_bersih)
# Untuk memasukan dalam list
lst_kata = isi_file_bersih.split()

# PAKAI SET UNTUK BENTUK UNIK(?) TERUS MASUKIN KE LIST LAGI
kata_unik = list(set(lst_kata))

print(kata_unik)

# Menghilangkan kata dalam stopwords--------------------------------------------------

filter_kata = []

# Membaca file stopwords
file_input = open("stopwords.txt")
stopwords = file_input.read()

# Mengecek apakah ada di dalam stopwords
for kata in kata_unik:
    cek = stopwords.find(kata) # Jika tidak ada maka akan mengembalikan -1, jika ada akan mengembalikan indexnya
    if cek == -1:
        filter_kata.append(kata)

print(filter_kata)
#---------------------------------------------------------------------------------------
# Mencari jumlah kata
jumlah_kata = []

# Mencari jumlah dari tiap kata
for kata in filter_kata:
    hitung = lst_kata.count(kata)
    jumlah_kata.append(hitung)

print(jumlah_kata)

# inisiasi data terbanyak---------------------------------------------------------------
data_terbanyak = []

# ambil remove ambil remove
# Mencari terbesar terus append and remove sebanyak 56 kali
for i in range(56):
    # Mencari terbesar dan indeks sementaranya
    terbesar = max(jumlah_kata)
    indeks_terbesar = jumlah_kata.index(terbesar)

    # Memasukkan data
    data_terbanyak.append(filter_kata[indeks_terbesar])
    data_terbanyak.append(terbesar)

    # Mereset angka yang sudah terpakai agar tidak terulang
    jumlah_kata[indeks_terbesar] = -1

print(data_terbanyak)
#---------------------------------------------------------------------------------------
# Membuat urutan berdasarkan huruf

data_kata = ""

# Memasukan data ke dalam string untuk diambil katanya saja
for i in range(56*2):
    if i % 2 == 0:
        data_kata += " " + data_terbanyak[i]
    
# Mengurutkan kata berdasar abjad dalam bentuk list
data_kata = data_kata.split()
data_kata.sort()

print(data_kata)

# Menginisasi isi data final
data_final = []

# Membuat model data final dari kata yang sudah diurutkan beserta jumlahnya
for kata in data_kata:
    # Cek
    indeks_kata = data_terbanyak.index(kata)

    data_final.append(kata)
    data_final.append(data_terbanyak[indeks_kata + 1])

print(data_final)

# Membuat file html----------------------------------------------------------------------
keluaran = ""
body = ""
data_count = []

for i in range(len(data_final)):
    if i % 2 == 1:
        data_count.append(data_final[i])

print(data_count)

hitung_program =  0
while hitung_program < 56*2:
    # Mencari atribut dengan pencarian nilai yang ada
    word = data_final[hitung_program]
    cnt = float(data_final[hitung_program + 1])
    high_count =float(max(data_count))
    low_count = float(min(data_count))

    body = body + " " + html_functions.make_HTML_word(word, cnt, high_count, low_count)

    hitung_program += 2 # (Agar berulang berpasangan dua-dua)

body = html_functions.make_HTML_box(body)
keluaran = html_functions.print_HTML_file(body, "A Word Cloud of "+file_masukan)

# WRITE TO FILE OUTPUT
my_file = open(file_keluaran, mode='w')
print(keluaran, file=my_file)
my_file.close()
