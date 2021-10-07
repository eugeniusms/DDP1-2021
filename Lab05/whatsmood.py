
file_masukan = "percakapan2.txt"

# Membaca File
my_file = open(file_masukan)
isi_file = my_file.read()
my_file.close()

"""
if isi_file = "":
    print("File input ada tapi kosong :(")
else:
"""

isi_file = isi_file.split("\n")

isi_baru = []

# Membuat variabel list 2 dimensi
for baris in isi_file:
    isi_baru.append(baris.split())
    isi_baru.append("gantibaris")

isi_file = isi_baru

# Membuat 2 parameter fungsi untuk indeks kalimat dalam isi_file dan kata dalam kalimat
total_smile = 0
total_sad = 0
total_angry = 0

kalimat_cek = []

def smile(kalimat,kata):
    global total_smile , kalimat_cek
    isi_file[kalimat][kata] = "\U0001f603"
    if kalimat_cek[0] == "Pak" and kalimat_cek[1] == "Chanek:":
        total_smile += 1

def sad(kalimat,kata):
    global total_sad, kalimat_cek
    isi_file[kalimat][kata] = "\U0001f622"
    if kalimat_cek[0] == "Pak" and kalimat_cek[1] == "Chanek:":
        total_sad += 1

def angry(kalimat,kata):
    global total_angry, kalimat_cek
    isi_file[kalimat][kata] = "\U0001f621"
    if kalimat_cek[0] == "Pak" and kalimat_cek[1] == "Chanek:":
        total_angry += 1

for kalimat in isi_file:
    kalimat_cek = kalimat
    for kata in kalimat:
        if kata == "(smile)":
            smile(isi_file.index(kalimat),list(kalimat).index(kata))
        elif kata == "(sad)":
            sad(isi_file.index(kalimat),list(kalimat).index(kata))
        elif kata == "(angry)":
                angry(isi_file.index(kalimat),list(kalimat).index(kata))
        else:
            continue

for kalimat in isi_file:
    if kalimat == "gantibaris":
        print()
    else:
        kalimat = " ".join(str(kata) for kata in kalimat)
        print(kalimat, end = "")

def kesimpulan(happiness, sadness, anger):
    data = [happiness, sadness, anger]
    kesimpulan = ["bahagia", "sedih", "marah"]
    maks = max(data)
    indeks_maks = []

    for i in range(len(data)):
        if data[i] == maks:
            indeks_maks.append(i)
    
    print("\n##### Kesimpulan #####")
    if len(indeks_maks) == 1:
        print("Pak Chanek sedang {}".format(kesimpulan[indeks_maks[0]]))
    elif len(indeks_maks) == 2:
        print("Pak Chanek sedang {} atau {}".format(kesimpulan[indeks_maks[0]], kesimpulan[indeks_maks[1]]))
    else:
        print("Kesimpulan tidak ditemukan.")

def ukur():
    print("\nMengukur suasana hati....\n\n##### Hasil Pengukuran #####")
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

    print("Happiness = {} | Sadness = {} | Anger = {}".format(happiness, sadness, anger))
    kesimpulan(happiness, sadness, anger)

ukur()



# print(Happiness = 54 | Sadness = 74 | Anger = 39)
