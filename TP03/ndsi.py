# -*- coding: utf-8 -*-
import string
import matplotlib.pyplot as plt

"""
Nama   : Eugenius Mario Situmorang
NPM    : 2106750484
Kelas  : C
Asdos  : LAH
Program: ndsi.py
Program untuk menghitung NDSI dari kata berdasar sentimen positif maupun negatif
dalam sebuah file yang sudah disiapkan. Hasil yang terakumulasi akan ditampilkan
melalui grafik (plot) sehingga memudahkan pembacaan analisis dari sentimen masyarakat
"""

def load_stop_words(filename):
    """
    Fungsi untuk mengambil semua kata yang terkandung di dalam berkas stop_words.
    Setiap kata yang tertera di dalam berkas akan dimasukkan ke dalam sebuah variabel
    berbentuk set di dalam program ini
    """  
    stop_words = set()
    my_file = open(filename)

    # Membaca file dan memasukkan isinya ke dalam variabel kemudian menutup file 
    stop_words = set(my_file.read().split())
    my_file.close()

    return stop_words

def count_words(filepath, stop_words):
    """
    Fungsi untuk membuka dan membaca file yang akan dianalisis (filepath), lalu
    membersihkan tanda baca dan kata (stop_words) di dalamnya. Setelah itu, program
    akan menentukan kata unik dan menghitung kata unik tersebut sesuai jumlah
    yang tertera di dalam file untuk dimasukkan ke dalam dictionary {kata : jumlah}
    bernama word_freq
    """
    # Inisiasi variabel yang akan digunakan di dalam fungsi
    word_freq = {}
    word_clear_punctuation = []
    word_clear = []
    doc_char_clear = ""
    punc_mid = ["[", "]", "(", ")", "/"]

    
    # Membuka file kemudian membaca dan memasukkan isinya ke dalam variabel doc_char, lalu menutup file
    my_file = open(filepath)
    doc_char = my_file.read()
    my_file.close()
    
    """
    Menghilangkan tanda baca dengan ketentuan dan syarat tertentu, saya menggunakan
    algoritma yang saya temukan dengan memilah char satu per satu berdasar satu indeks 
    sebelum dan sesudahnya (untuk menghindari kesalahan pengambilan kata ex : that's),
    dengan algoritma ini saya bisa mempersingkat waktu dibanding pengecekan kata demi kata.
    Program akan selalu berjalan maju sesuai dokumen yang dibaca jadi sekali melangkah dapat
    mengakomodir pengecekan tanda baca sekaligus. 
    [Efisiensi : Dari 5 menit menjadi 5 detik]
    """
    for i in range(len(doc_char)):
        if doc_char[i] not in string.punctuation:
            doc_char_clear += doc_char[i]
        else:
            if i == 0 or i == len(doc_char): # Handle error punctuation string pertama dan terakhir
                continue
            if (doc_char[i] in string.punctuation) and (doc_char[i-1] not in string.punctuation) and (doc_char[i+1] not in string.punctuation):
                if (doc_char[i-1] != " ") and (doc_char[i+1] != " ") and (doc_char[i] not in punc_mid):
                    doc_char_clear += doc_char[i]

    print(doc_char_clear)

    # Memecah dokumen baru yang bersih dari tanda baca menjadi list setiap kata 
    word_clear_punctuation = doc_char_clear.split()

    # Membersihkan stopwords dalam word_clear_punctuation
    for word in word_clear_punctuation:
        if word in stop_words:
            continue
        else:
            word_clear.append(word)

    # Mendapat kata unik
    word_unique = list(set(word_clear))

    # Mengisi dictionary word_freq
    for word in word_unique:
        count = word_clear.count(word)
        word_freq[word] = count

    return word_freq

def compute_ndsi(word_freq_pos, word_freq_neg):
    """
    Fungsi untuk menghitung ndsi di mana NDSI berbentuk rasio dari frekuensi kata positif
    dikurang kata negatif kemudian dibagi jumlahnya sehingga didapati jika frekuensi kata 
    negatif lebih banyak maka akan menghasilkan rasion negatif, ketika kata tidak ada
    di dalam variabel maka akan dituliskan nilai 0.
    """
    word_ndsi = {}

    # Mendapatkan set dari semua key yang ada untuk digabungkan dalam word_total
    word_pos = set(word_freq_pos.keys())
    word_neg = set(word_freq_neg.keys())
    word_total = word_pos.union(word_neg)

    # Menghitung NDSI pada setiap kata di dalam word_total kemudian masukkan ke dictionary baru word_ndsi
    for word in word_total:
        if word not in word_freq_pos:
            word_freq_pos[word] = 0
        if word not in word_freq_neg:
            word_freq_neg[word] = 0
        word_ndsi[word] = float((word_freq_pos[word] - word_freq_neg[word])/(word_freq_pos[word] + word_freq_neg[word]))

    return word_ndsi

def show_ndsi_histogram(word_ndsi):
    """
    Fungsi untuk menampilkan grafik (plot) dari dictionary NDSI yang sudah terakumulasi
    grafik akan menampilkan nilai (value) NDSI dari setiap kata.
    """
    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor = 'g', alpha = 0.75)
    
    # Menginisiasi indeks parameter di dalam grafik
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")

    # Menampilkan grafik ke layar
    plt.show()

if __name__ == "__main__":

    # memuat stop words ke sebuah set
    stop_words = load_stop_words("stopwords.txt")

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment positif
    word_freq_pos = count_words("./sent-polarity-data/rt-polarity.pos", stop_words)

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment negatif
    word_freq_neg = count_words("./sent-polarity-data/rt-polarity.neg", stop_words)

    # hitung NDSI untuk semua kata-kata pada kedua jenis dictionary berisi
    # word frequency
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    # tampilkan histogram dari nilai-nilai NDSI yang dihasilkan
    show_ndsi_histogram(word_freq_ndsi)

    # Mengurutkan data berdasarkan nilai NDSI
    word_ndsi_sorted = dict(sorted(word_freq_ndsi.items(), key=lambda item: item[1]))

    # Menuliskan isi dictionary NDSI yang sudah diurutkan ke dalam file "ndsi.txt"
    ndsi_filename = "ndsi.txt"
    my_file = open(ndsi_filename, "w")
    print(word_ndsi_sorted, file=my_file)
    my_file.close()
