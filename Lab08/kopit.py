"""
Nama : Eugenius Mario Situmorang
NPM  : 2106750484
Asdos: LAH
Judul: kopit.py
Sebuah program yang diminta oleh Menteri Kesehatan negara yang dikunjungi Dek Depe
karena semua tenaga medis kewalahan dalam menghadapi persebaran virus KOPIT.
Program ini dimaksudkan untuk "tracking" penular dan orang yang tertular virus
dengan menganalisis sejumlah data yang diberikan di dalam input user.
"""

# Menginisiasi set dari data yang berisikan penyebaran virus
data_penyebaran = set()

def cek_orang(nama, penduduk):
    """
    Fungsi yang digunakan untuk mengecek identitas dan keberadaan orang tersebut di dalam
    data penduduk yang masuk ke dalam input. Identitas akan dicek menggunakan pencocokan nama
    di dalam set {penduduk} yang berisikan semua penduduk di dalam input. Jika ada maka kembalikan
    nilai True, sebaliknya jika tidak ada kembalikan nilai False.
    """
    if nama in penduduk:
        return True
    else:
        return False

def rantai_penularan(rantai, nama):
    """
    Fungsi rekursif yang mengumpulkan setiap data yang tertular Kopit, di sini
    saya menggunakan Teori Graph khususnya pendekatan Depth First Search (DFS). 
    Menggunakan implementasi ini saya dapat memanggil setiap kemungkinan sesuai 
    nama yang terhubung seperti di dalam sebuah sistem graph.
    """
    global data_penyebaran

    # Menambahkan setiap dari yang tertular oleh penular ke dalam set data_penyebaran
    data_penyebaran.add(nama)

    # BENTUK "REKURSIF"
    # Mengambil setiap nilai value di dalam key untuk selalu dipanggil sesuai konsep DFS
    for teman in rantai[nama]:
        # Jika sudah pernah ada akan dipass sehingga code dapat berhenti (tidak perulangan menerus)
        # Contoh case : {A : B, B : A} 
        if teman in data_penyebaran:
            pass
        else:
            # Jika belum ada lakukan pemanggilan fungsi kembali secara rekursif
            # Jika pengembalian fungsi adalah None maka pass fungsi (Base Case ujung tiap path)
            if rantai_penularan(rantai, teman) == None: 
                pass
            else:
                # Jika masih terdapat pengembalian fungsi maka panggil fungsi kembali (Recursion Case)
                rantai_penularan(rantai, teman)
def main():
    """
    Fungsi utama yang mengambil input dari pengguna tentang rantai penyebaran Kopit
    ke dalam program dengan susunan [nama_orang_1]<spasi>[nama_orang_2]... pada setiap
    barisnya (dipisahkan lalu diassign ke sebuah dictionary bernama rantai untuk dioperasikan)
    """
    global data_penyebaran

    # Menginisiasi beberapa variabel utama yang akan digunakan selama di dalam fungsi Main()
    nama = ["kosong"]
    rantai = {}
    penduduk = set()

    # Program mulai berjalan dengan mengambil data penduduk penular : tertular1, tertular2, ...
    print("Masukkan rantai penyebaran:")
    while True:
        # Mengambil input yang kemudian displit (Menjadi bentuk list)
        nama = input().split()

        # Pengumpulan orang akan berhenti ketika terdapat kata selesai
        if nama[0] == "selesai":
            break
        
        # Mengumpulkan semua orang yang termasuk di dalam list input nama 
        for doi in nama:
            penduduk.add(doi)

        # Mengumpulkan rantai penyebaran yang terjadi dengan dictionary
        orang = nama[0]
        nama_teman = nama.copy()
        nama_teman.pop(0)

        # Penentuan masukan data jika ada lebih dari sebaris berisi tertular dengan penular yang sama
        if orang in rantai.keys():
            rantai[orang] += nama_teman
        else:
            rantai.update({orang : nama_teman})

    # Jika seseorang belum pernah ada di dalam key dictionary maka inisiasikan
    # Agar program bisa menemukan ujung dengan batas kosong [] 
    for seseorang in penduduk:
        if seseorang not in rantai.keys():
            rantai.update({seseorang : []})

    # Membuat output perintah pada layar terminal
    print("\nList perintah:")
    print("1. RANTAI_PENYEBARAN")
    print("2. CEK_PENULARAN")
    print("3. EXIT")

    """
    Program mengambil input user (perintah) untuk diproses sesuai keinginan sesuai output
    pada layar terminal di atas. Gambaran besarnya adalah perinta berada di indeks ke-0 dalam
    list perintah (input string yang sudah displit menjadi bentuk list). Kemudian atribut
    seperti nama tertular dan penular berada pada indeks selanjutnya. Program akan selalu
    mengambil perintah (while True) sampai saat break jika perintah == "EXIT".
    """
    while True:
        # Mengambil masukan perintah (try-except untuk handle kasus input tidak valid)
        try:
            perintah = input("\nMasukkan perintah: ").split()

            # Jika perintah[0] adalah "RANTAI_PENYEBARAN" jalankan program ini
            if perintah[0] == "RANTAI_PENYEBARAN" and len(perintah) == 2:
                # Checking untuk nama apakah terdapat di dalam daftar penduduk
                if cek_orang(perintah[1], penduduk): 
                    # Jalankan fungsi rantai_penularan() untuk mencari siapa saja yang tertular {nama}
                    rantai_penularan(rantai, perintah[1]) 
                    print(f"Rantai penyebaran {perintah[1]}:")
                    for kontak in data_penyebaran:
                        print(f"- {kontak}")
                # Jika nama tidak terdaftar di daftar penduduk maka print sebagai berikut
                else:
                    print(f"Maaf, nama {perintah[1]} tidak ada dalam rantai penyebaran.")
        
        # Jika perintah[0] adalah "CEK_PENULARAN" jalankan program ini
            elif perintah[0] == "CEK_PENULARAN" and len(perintah) == 3:
                # Checking untuk nama apakah terdapat di dalam daftar penduduk
                cek_orang_1 = cek_orang(perintah[1], penduduk) 
                cek_orang_2 = cek_orang(perintah[2], penduduk)
                """
                Program akan memanggil fungsi hanya jika nama1 dan nama2 terdapat dalam daftar
                penduduk (pengecekan melalui operasi boolean True <and> True)
                """
                if cek_orang_1 and cek_orang_2:
                    # nama1 : <nama tertular> nama2 : <nama penular>
                    # Jalankan fungsi untuk mencari siapa saja yang tertular oleh penular
                    rantai_penularan(rantai, perintah[2])
                    # Jika nama1 terdapat di dalam daftar tertular maka print "YA", sebaliknya "TIDAK"
                    if perintah[1] in data_penyebaran:
                        print("YA")
                    else:
                        print("TIDAK")
                elif not cek_orang_1 and cek_orang_2:
                    print(f"Maaf, nama {perintah[1]} tidak ada dalam rantai penyebaran.")
                elif cek_orang_1 and not cek_orang_2:
                    print(f"Maaf, nama {perintah[2]} tidak ada dalam rantai penyebaran.")
                elif not cek_orang_1 and not cek_orang_2:
                    print(f"Maaf, nama {perintah[1]} dan {perintah[2]} tidak ada dalam rantai penyebaran.")
            
            # Jika perintah[0] adalah "EXIT" jalankan program ini
            elif perintah[0] == "EXIT" and len(perintah) == 1: # EXIT ADA ATRIBUT TETEP EXIT WKWK FIX IT
                print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
                break

            # Jika perintah tidak dikenali maka jalankan program ini
            else:
                print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")

        except:
            print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")
            continue

        # Data Penyebaran direset kosong dahulu setiap pengambilan input perintah
        data_penyebaran = set()

# Mulai untuk menjalankan program melalui pemanggilan fungsi main()
main()
