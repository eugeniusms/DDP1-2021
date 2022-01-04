MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24
HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]
MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] + JAM[9] + 40],
["ddp 1 a", HARI[2] + JAM[8] + 0, HARI[2] + JAM[9] + 40],
["ddp 1 b", HARI[1] + JAM[8] + 0, HARI[1] + JAM[9] + 40],
["manbis", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
["matdis 1 a", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["matdis 1 b", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40]
]
"""
Merepresentasikan jadwal “ddp 1 a” hari senin 08.00 sampai 09.40,
serta hari rabu jam 08.00 sampai 09.40
Jadwal “ddp 1 b” hari rabu jam 08.00 sampai 09.40
Jadwal “manbis” hari senin jam 09.00 sampai 10.40
Jadwal “matdis 1 a” hari rabu jam 09.00 sampai 10.40
Jadwal “matdis 1 b” hari rabu jam 09.00 sampai 10.40
"""
# kode Anda selanjutnya
# Menginisiasi list berisi mata kuliah yang akan disusun jadwalnya
matkul = []

def add(add_matkul):
    global MATKUL_TERSEDIA, matkul
    # Cek ketersediaan mata kuliah
    add_matkul = [MATKUL_TERSEDIA[x] for x in range(len(MATKUL_TERSEDIA)) if add_matkul == MATKUL_TERSEDIA[x][0]]
    if not add_matkul:
        print("Matkul tidak ditemukan")
    else:
        # Menambahkan matkul ke dalam daftar matkul yang disimpan
        matkul.extend(add_matkul)

def drop(drop_matkul):
    global matkul
    # Mengembalikan list mata kuliah yang tidak sama dengan drop_matkul
    matkul = [matkul[i] for i in range(len(matkul)) if matkul[i][0] != drop_matkul]

def ringkasan(matkul):
    waktu, indeks = [], []
    # Mencari nilai menit pada rentang waktu di setiap mata kuliahnya (bentuk set)
    for mata_kuliah in matkul:
        waktu.append(set([i for i in range(mata_kuliah[1], mata_kuliah[2] + 1)]))
    
    # Melakukan irisan pada setiap set yang ada, jika ada maka kembalikan nilai indeks i dan j
    for i in range(len(waktu)):
        for j in range(len(waktu)):
            x = waktu[i].intersection(waktu[j])
            # Ketika terdapat irisan dan bukan indeks yang sama catat nilai indeks
            if len(x) > 0 and i != j:
                # Selama tidak terdapat bentuk kebalikannya maka tambahkan (bentuk kebalikan sama saja mengembalikan nilai yang sama)
                if [j, i] not in indeks:
                    indeks.append([i,j])
            x.clear()

    # Jika indeks ada isinya maka kembalikan nama mata kuliah di indeks yang ada di dalam list indeks
    if len(indeks) == 0:
        print("Tidak ada mata kuliah yang bermasalah")
    else:
        for ij in indeks:
            print(f"    {matkul[ij[0]][0]} bentrok dengan {matkul[ij[1]][0]}")

def daftar_matkul(matkul):
    panjang = []
    nama_hari = ["Senin,  ", "Selasa, ", "Rabu,   ", "Kamis,  ", "Jumat,  ", "Sabtu,  ", "Minggu, "]

    # Mengurutkan mata kuliah berdasar waktunya (konsep bubble sort)
    n = len(matkul)
    for i in range(n):
        for j in range(n-1, i, -1):
            if matkul[i][1] > matkul[j][1]:
                dummy = matkul[j]
                matkul[j] = matkul[j-1]
                matkul[j-1] = dummy

    # Mengubah nilai angka menjadi tanggal
    for mata_kuliah in matkul:
        panjang.append(len(mata_kuliah[0]))

    for mata_kuliah in matkul:
        # Menata format nama mata kuliah
        print(f"    {mata_kuliah[0].upper():<{max(panjang) + 4}}", end = " ")
        for i in range(1,3):
            # Mengonversi nilai angka menjadi hari, jam, dan menit
            hari = int((mata_kuliah[i] / 60) // 24)
            jam = int((mata_kuliah[i] - (hari * 60 *24)) // 60)
            menit = int((mata_kuliah[i] - (hari * 60 *24) - (jam * 60)))
            # Menata bentuk sesuai format output
            print(f"{nama_hari[hari]} {jam:0>2}.{menit:0>2}   ", end = "")
            if i == 1:
                print("s/d", end = " ")
        print()

def main():
    global matkul
    # Menjalankan program utama untuk meminta input
    while True:
        print("=========== SUSUN JADWAL ===========\n1 Add matkul\n2 Drop matkul\n3 Cek ringkasan\n4 Lihat daftar matkul\n5 Selesai\n====================================\n")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            # Membuat pengabaian pada extra leading spaces maupun trailing spaces serta pengabaian sensitive-case
            add_matkul = input("Masukkan nama matkul: ")
            add(add_matkul.lower().strip())
        elif pilihan == "2":
            drop_matkul = input("Masukkan nama matkul: ")
            drop(drop_matkul.lower().strip())
        elif pilihan == "3":
            ringkasan(matkul)
        elif pilihan == "4":
            if len(matkul) == 0:
                print("Tidak ada matkul yang diambil")
            else:
                daftar_matkul(matkul)
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            # Berjalan jika input tidak ada yang sesuai
            print("Maaf, pilihan tidak tersedia")
        print()

main()
