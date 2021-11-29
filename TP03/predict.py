# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import ast

"""
Nama   : Eugenius Mario Situmorang
NPM    : 2106750484
Kelas  : C
Asdos  : LAH
Program: predict.py
Program untuk menggambarkan grafik sentimen dalam suatu teks berdasarkan data hasil analisis
yang ada. Di mana pada setiap baris di dalam teks tersebut akan dihitung untuk dipertimbangkan
nilai positif maupun negatifnya sehingga pada akhirnya akan ditampilkan grafik x,y dengan 
hasil sentimen yang sudah diatur sedemikian rupa.
"""

# lengkapi fungsi berikut
def load_ndsi(ndsi_filename):
    """
    Fungsi ini memuat daftar kata-kata dan nilai NDSI yang bersesuaian ke dalam sebuah 
    dictionary (dari file ndsi.txt), dimana key adalah kata (string) dan value adalah 
    NDSI score (float) dari kata tersebut.
    """
    word_ndsi = {}

    # Membaca file dan memasukkan isinya ke dalam variabel kemudian menutup file 
    my_file = open(ndsi_filename)
    word_ndsi = my_file.read()
    my_file.close()

    # Ini digunakan untuk mengubah bentuk string menjadi bentuk dictionary karena bentuk teks di dalam file masih berbentuk string
    word_ndsi = ast.literal_eval(word_ndsi) 

    return word_ndsi

def compute_score(filename, word_ndsi):
    """
    Fungsi ini mengembalikan list of pairs, dimana setiap elemen merupakan pasangan 
    (positive score, negative score) untuk sebuah kalimat. Sebuah kalimat akan diklasifikasikan 
    sebagai positif jika positive score > negative score; dan sebaliknya. 
    Jika kedua nilai sama, kalimat diklasifikaskan sebagai netral.
    """

    # Membagi masalah sesuai alphabet untuk mempersingkat pencarian kata dari data
    # Bentuk menjadi : [['a',{apple : 0.5}, {america : 0.1}]]
    lst_alpha = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for chr in range(len(alpha)):
        lst_alpha.append([alpha[chr]])
        for k,v in word_ndsi.items():
            if k[0] == alpha[chr]:
                lst_alpha[chr].append(k)
                lst_alpha[chr].append(v)

    # Membuka, menuliskan, dan menutup file di dalam parameter fungsi : "sent-unknown-label.txt"
    pos_neg_scores = []
    my_file = open(filename, 'r')
    lines = my_file.readlines()
    my_file.close()

    """
    Program akan melakukan filterisasi pada setiap kata dengan melakukan operasi pada jumlah
    positif dan negatif yang ditemui di dalam word_ndsi. Di sini saya menggunakan pemecahan
    masalah dengan search word berdasarkan huruf depan kata sehingga mempercepat hingga 26x lebih
    """
    count = 0
    # Untuk setiap line di dalam file yang sudah dibaca readlines() lakukan pemecahan per kata
    for line in lines:
        count += 1
        line = line.split()
        pos = 0
        neg = 0
        # Di mana setiap kata tersebut akan dicari panjangnya (untuk kata dengan 1 huruf tidak terhitung karena berpengaruh pada algoritma alphabet tadi
        for word in line:
            if len(word) == 1:
                continue 
            
            # Program akan melanjutkan mencari letak indeks dalam alpha (mencari indeks huruf dalam alphabet)
            ind = alpha.find(word[0])
            
            # Kemudian akan dipanggil list indeks ke-[ind] (berdasarkan abjad tadi untuk mempercepat pencarian)
            if word in lst_alpha[ind]:
                # Jika ndsi ada dan sudah ditemukan sesuai indeks sesuaikan hitung positif atau negatif (kembalikan bentuk positif)
                indeks = lst_alpha[ind].index(word)
                ndsi = float(lst_alpha[ind][indeks + 1])
                if ndsi > 0:
                    pos += ndsi
                elif ndsi < 0:
                    neg += abs(ndsi)

        # Kemudian tambahkan pos dan neg ke dalam list pos_neg_scores jika setiap kata dalam baris sudah difilter
        pos_neg_scores.append((pos, neg))

    return pos_neg_scores

def show_scatter_plot(pos_neg_scores):
    """
    Fungsi yang menampilkan scatter plot untuk semua kalimat di sent-unknown-label.txt. 
    Sumbu X merupakan nilai positif dan sumbu Y merupakan nilai negatif. Titik-titik 
    warna biru yang berada di bawah garis Y = X merupakan kalimat-kalimat yang diprediksi 
    sebagai kalimat ber-sentiment positif, sedangkan yang berwarna merah diprediksi
    sebagai kalimat ber-sentiment negatif.
    """
    plt.clf()

    # Jika pos_score > neg_score maka masukan tuple ke dalam predicted as pos, begitupun sebaliknya
    predicted_as_pos = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score > neg_score]
    predicted_as_neg = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score < neg_score]

    # Memetakan bentuk di atas menjadi koordinat (terbagi menjadi positif dan negatif)
    x_pos_1 = [pos_score for (pos_score, _) in predicted_as_pos]
    y_pos_1 = [neg_score for (_, neg_score) in predicted_as_pos]
    x_pos_2 = [pos_score for (pos_score, _) in predicted_as_neg]
    y_pos_2 = [neg_score for (_, neg_score) in predicted_as_neg]

    # Melakukan inisiasi atribut plt.scatter
    plt.scatter(x_pos_1, y_pos_1, color = 'blue', s = 5)
    plt.scatter(x_pos_2, y_pos_2, color = 'hotpink', s = 5)

    plt.xlabel("Positive Score")
    plt.ylabel("Negative Score")
    plt.xlim(-0.1, 8)
    plt.ylim(-0.1, 8)
    plt.savefig("senti-plot.pdf")

    # Menampilkan grafik
    plt.show()

if __name__ == "__main__":

    # Memuat dictionary berisi kata dan nilai NDSI-nya
    word_ndsi = load_ndsi("ndsi.txt")

    # Hitung nilai
    pos_neg_scores = compute_score("sent-unknown-label.txt", word_ndsi)

    # Scatter plot yang menampilkan nilai positif dan negatif dari
    # Kalimat-kalimat yang ada di sent-unknown-label.txt;
    # Dokumen yang netral tidak diiukutsertakan.
    show_scatter_plot(pos_neg_scores)

    # Untuk setiap kalimat (setiap baris di sent-unknown-label.txt),
    # Jika nilai positif > nilai negatif --> predicted label: positif
    # Jika nilai positif < nilai negatif --> predicted label: negatif
    # Else --> predicted label: netral (hampir tidak ada sepertinya)
    for i, (pos_score, neg_score) in enumerate(pos_neg_scores):
        predicted_label = "neutral"
        if pos_score > neg_score:
            predicted_label = "pos"
        elif neg_score > pos_score:
            predicted_label = "neg"
        print(f"sentence {i+1} -- pos:{pos_score:6.3f}  neg:{neg_score:6.3f}  prediction:{predicted_label}")
