# Memasukkan library math ke dalam program Python
import math

# Menginisiasi masukan untuk perhitungan dengan tipe float agar bisa diinput nilai koma
radius = float(input("Masukkan radius lingkaran: "))

# Luas persegi = sisi * sisi, di mana sisi = 2 x radius
luas_persegi = (2 * radius) * (2 * radius)
# Luas lingkaran = pi * radius * radius, di mana radius sudah diketahui
luas_lingkaran = math.pi * radius * radius
# Luas segitiga = alas * tinggi / 2, di mana tinggi = radius dan alas = 2 x radius
luas_segitiga = radius * (2 * radius) / 2

# Lihat bahwa luas warna merah merupakan pengurangan dari luas persegi - luas lingkaran
luas_merah = str(round((luas_persegi - luas_lingkaran), 2))
# Lihat bahwa luas warna kuning merupakan pengurangan dari luas lingkaran - luas segitiga
luas_kuning = str(round((luas_lingkaran - luas_segitiga), 2))
# Lihat bahwa luas warna ungu hanya merupakan segitiga itu sendiri
luas_ungu = str(round((luas_segitiga), 2))

# Membuat keluaran dengan variabel di atas yang sudah bertipe string dan diround 2 di belakang koma
print("Luas daerah cat merah: "+luas_merah)
print("Luas daerah cat kuning: "+luas_kuning)
print("Luas daerah cat ungu: "+luas_ungu)
