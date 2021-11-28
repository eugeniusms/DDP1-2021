# CHECK PUNCTUATION ALGORITHM AT ALL PROGRAMS

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import ast

# lengkapi fungsi berikut
def load_ndsi(ndsi_filename):
    word_ndsi = {}

    # Membaca file dan memasukkan isinya ke dalam variabel kemudian menutup file 
    my_file = open(ndsi_filename)
    word_ndsi = my_file.read()
    my_file.close()

    
    word_ndsi = ast.literal_eval(word_ndsi) 

    print(type(word_ndsi))
    return word_ndsi

# lengkapi fungsi berikut
def compute_score(filename, word_ndsi):
    # word_ndsi = dict(word_ndsi)

    # <DIVIDE PROBLEM BY ALPHABET> [['a',{apple : 0.5}, {america : 0.1}]]
    lst_alpha = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for chr in range(len(alpha)):
        lst_alpha.append([alpha[chr]])
        for k,v in word_ndsi.items():
            if k[0] == alpha[chr]:
                lst_alpha[chr].append(k)
                lst_alpha[chr].append(v)

    print(lst_alpha)

    # Membuka file
    pos_neg_scores = []
    my_file = open(filename, 'r')
    lines = my_file.readlines()
    my_file.close()

    # TANDA BACA DALAM KATA? USE SAME WITH NDSI PROGRAM
 
    count = 0
    for line in lines:
        count += 1
        line = line.split()
        pos = 0
        neg = 0
        # print(f"line : {line}")
        for word in line:
            if len(word) == 1:
                continue # (clear one char)
            ind = alpha.find(word[0])
            # print(f"word : {word}, index_alpha : {ind}")
            if word in lst_alpha[ind]:
                indeks = lst_alpha[ind].index(word)
                # print(f"word : {word}, indeks_lst : {indeks}")
                ndsi = float(lst_alpha[ind][indeks + 1])
                if ndsi > 0:
                    pos += ndsi
                elif ndsi < 0:
                    neg += abs(ndsi)
                # print(f"ada {word}")
                predict = pos - neg
        # return
        pos_neg_scores.append((pos, neg))

    return pos_neg_scores

# Fungsi sudah diberikan; tinggal digunakan saja
def show_scatter_plot(pos_neg_scores):
    plt.clf()

    predicted_as_pos = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score > neg_score]
    predicted_as_neg = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score < neg_score]

    x_pos_1 = [pos_score for (pos_score, _) in predicted_as_pos]
    y_pos_1 = [neg_score for (_, neg_score) in predicted_as_pos]
    x_pos_2 = [pos_score for (pos_score, _) in predicted_as_neg]
    y_pos_2 = [neg_score for (_, neg_score) in predicted_as_neg]

    plt.scatter(x_pos_1, y_pos_1, color = 'blue', s = 5)
    plt.scatter(x_pos_2, y_pos_2, color = 'hotpink', s = 5)

    plt.xlabel("Positive Score")
    plt.ylabel("Negative Score")
    plt.xlim(-0.1, 8)
    plt.ylim(-0.1, 8)
    plt.savefig("senti-plot.pdf")

    plt.show()

if __name__ == "__main__":

    # memuat dictionary berisi kata dan nilai NDSI-nya
    word_ndsi = load_ndsi("ndsi.txt")

    # hitung nilai
    pos_neg_scores = compute_score("sent-unknown-label.txt", word_ndsi)

    # scatter plot yang menampilkan nilai positif dan negatif dari
    # kalimat-kalimat yang ada di sent-unknown-label.txt;
    # dokumen yang netral tidak diiukutsertakan.
    show_scatter_plot(pos_neg_scores)

    # untuk setiap kalimat (setiap baris di sent-unknown-label.txt),
    # jika nilai positif > nilai negatif --> predicted label: positif
    # jika nilai positif < nilai negatif --> predicted label: negatif
    # else --> predicted label: netral (hampir tidak ada sepertinya)
    for i, (pos_score, neg_score) in enumerate(pos_neg_scores):
        predicted_label = "neutral"
        if pos_score > neg_score:
            predicted_label = "pos"
        elif neg_score > pos_score:
            predicted_label = "neg"
        print(f"sentence {i+1} -- pos:{pos_score:6.3f}  neg:{neg_score:6.3f}  prediction:{predicted_label}")
