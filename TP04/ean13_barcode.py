from tkinter import *
import tkinter.messagebox as tkmsg

"""
Nama : Eugenius Mario Situmorang
NPM  : 2106750484
Program : barcode_generator.py
Program ini dirancang untuk membuat bentuk barcode EAN-13 dengan menggunakan input user.
Sebanyak 12 angka akan diubah menjadi bentuk barcode dan kemudian disimpan ke dalam
sebuah file. Pengguna lain dapat melakukan pengecekan barcode dengan gawainya.
"""

def manipulate(binary):
    """
    Fungsi ini digunakan untuk memanipulasi nilai binary yang didapatkan dalam program
    setelah melalui encoding L-G-R. Binary akan dimodifikasi sesuai keperluan yaitu
    membentuk SXXXXXXMYYYYYYE dengan S = Start, M = Middle, E = End (Setiap indeks
    huruf mewakili 7 bit dalam encoding L-G-R). Pada akhirnya fungsi ini akan
    menyisipkan S,M, dan E ke dalam binary. (Panjang binary = 7 * 12 = 84) maka 
    manipulasi akan dilakukan di indeks ke 0, 41, 84.
    """
    # Start dan End bernilai = 101
    strend = "101"
    # Middle bernilai = 01010
    mid = "01010"
    
    new_binary = strend + binary[:42] + mid + binary[42:] + strend
    return new_binary


def create_bar(start, number, binary, canvas):
    """
    Fungsi untuk membentuk output gambar dalam canvas menggunakan info yang sudah diberikan
    dalam argumen fungsi. Sebelum dilakukan penggambaran canvas, perlu dilakukan manipulasi
    binary terlebih dahulu agar mendapat sisipan S M E yang dijelaskan dalam fungsi
    manipulate(). Setelah dimanipulasi, program akan memulai menggambarkan tulisan dan
    barcode sesuai dengan konsep EAN-13
    """
    # Manipulasi binary
    binary = manipulate(binary)

    # Melakukan pencetakan teks "EAN-13 Barcode:"
    canvas.create_text(175, 75, font = "Helvetica 20 bold", text = "EAN-13 Barcode:")

    # Menginisiasi koordinat awal x dan penghitungan
    pos_x = 50
    count = 0
    # Melakukan perulangan untuk setiap bit dalam binary agar dilakukan penyesuaian
    for bit in binary:
        # Jika bit bernilai 1 maka lakukan pencetakan canvas (rectangle/bar)
        if bit == "1":
            # Pada saat indeks [0:3], [45:50] dan [91:] akan diberikan warna orange dan bar lebih panjang (SME)
            if (count < 3) or (count > 44 and count < 50) or (count > 90):
                canvas.create_rectangle(
                    pos_x, 100, pos_x + 1.5, 260,
                    outline="#FF8141",
                    fill="#FF8141")
            else:
                # Sedangkan pada bar normal (bukan SME) akan diberikan warna biru muda
                canvas.create_rectangle(
                    pos_x, 100, pos_x + 1.5, 250,
                    outline="#00C4FF",
                    fill="#00C4FF")

        # Pada setiap kali perulangan, bar yang baru akan dibentuk dengan jarak antar koordinat (2.5)
        pos_x += 2.5
        count += 1

    # Melakukan penyetelan bentuk string pada string digit pada setiap binary
    style_number = ""
    number = start + number
    for i in range(len(number)):
        if i == 0 or i == 6:
            style_number += number[i] + "   "
        else:
            style_number += number[i] + "  "

    # Melakukan pencetakan teks digit yang sudah disesuaikan
    canvas.create_text(165, 271, fill = "#1E5C9A", font = "Helvetica 17 bold", text = style_number)

    # Menentukan bahwa Check Digit adalah digit terakhir (number[-1]), kemudian lakukan pencetakan pada canvas
    end = number[-1]
    canvas.create_text(168, 295, font = "Helvetica 20 bold", text = "Check Digit: {}".format(end))
    
def processing(start, first_group, last_group, end, canvas):
    """
    Fungsi ini akan melakukan pemrosesan data yang diberikan di dalam fungsi main() dengan atribut
    yang sudah terbagi menjadi 5. Fungsi akan memproses struktur dan digit encoding L-G-R dengan
    cara melakukan pengecekan dari digit awal (Start) untuk menentukan bentuk struktur 6 digit
    selanjutnya. Sedangkan, pada 6 digit kedua akan selalu berbentuk RRRRRR sehingga hanya perlu
    ditambahkan bentuk string RRRRRR. Setelah didapati bentuk structure, program akan melakukan
    encoding secara binary dengan tipe L-G-R sesuai digit dan indeks structure. Jika sudah didapati
    bentuk binary secara keseluruhan, maka lakukan pemanggilan fungsi create_bar().
    """
    # Penentuan struktur dipengaruhi oleh digit pertama (start)
    first_structure = {
        "0" : "LLLLLL",
        "1" : "LLGLGG",
        "2" : "LLGGLG",
        "3" : "LLGGGL",
        "4" : "LGLLGG",
        "5" : "LGGLLG",
        "6" : "LGGGLL",
        "7" : "LGLGLG",
        "8" : "LGLGGL",
        "9" : "LGGLGL"
    }

    # Melakukan penyusunan struktur secara keseluruhan 12 digit
    structure = first_structure[start] + "RRRRRR"
    number = first_group + last_group + str(end)

    # Menyusun bentuk binary dari setiap tipe L-G-R dengan menggunakan digit = list by index
    digit_encoding = {
        "L" : ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"],
        "G" : ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"],
        "R" : ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
    }

    # Melakukan kompilasi dari struktur dan digit yang didapati menjadi bentuk binary
    binary = ""
    count = 0
    for lgr in structure:
        num = number[count]
        cod = digit_encoding[lgr]
        binary += cod[int(num)]
        count += 1

    # Memanggil fungsi untuk menggambarkan bar ke dalam canvas
    create_bar(start, number, binary, canvas)

def main():
    """
    Fungsi ini berlaku sebagai fungsi utama selama program berjalan. Diberikan bentuk frame dengan
    dua entry field yaitu nama file untuk menyimpan file gambar hasil barcode dan juga kolom untuk
    memasukkan angka barcode itu sendiri. Kemudian disediakan canvas untuk melakukan pencetakan
    gambar sesuai dengan prosedur program. Gambar dan penyimpanan file akan dilakukan jika user
    menekan [ENTER]. Namun, ada pengecualian ketika masukan user kurang sesuai dan tidak valid.
    Pada kasus tersebut, program akan menampilkan peringatan.
    """
    # Melakukan penyetelan posisi dan inisiasi form serta canvas
    root.geometry("450x540")
    welcome = Label(root, text = 'Save barcode to PS file [eg: EAN13.eps]:')
    save = Entry(root, width = 25)
    enter = Label(root, text = 'Enter code (first 12 decimal digits):')
    code = Entry(root, width = 25)
    
    welcome.place(x = 95, y = 10)
    save.place(x = 100, y = 40)
    enter.place(x = 108, y = 70)
    code.place(x = 100, y = 100)

    canvas = Canvas(
        root,
        height=350,
        width=350,
        bg="#fff"
        )
    canvas.place(x = 43, y = 140)

    def func(event):
        """
        Fungsi ini akan berjalan ketika user menekan [ENTER] setelah mengisi form.
        Di dalam fungsi ini, masukan user akan diambil. Untuk angka masukan akan
        dilakukan pengecekan validasi seperti jumlah angka yang diberikan (12 digit).
        Kemudian untuk kolom nama file simpan akan dilakukan pembuatan file setelah
        canvas telah tergambar dengan baik.
        """
        # Membersihkan canvas setiap kali [ENTER]
        canvas.delete("all")
        # Melakukan pengambilan entry user
        check_number = code.get()
        filename = save.get()
        
        # Validasi angka masukan
        try:
            # Validasi angka harusnya 12 digit panjangnya
            if len(check_number) == 12:
                start = check_number[0]
                first_group = check_number[1:7]
                last_group = check_number[7:13]
                
                # End bertindak sebagai check digit di mana didapati dari perkalian 3 jumlah indeks ganjil dan 
                # perkalian 1 jumlah indeks genap, kemudian cari sisa bagi 10 dan sisa bagi tersebut dilakukan
                # pengurangan dari 10, jika sisa bagi 0 maka end = 0
                end = 0
                for digit in range(len(check_number)):
                    if digit % 2:
                        end += 3 * int(check_number[digit])
                    else:
                        end += 1 * int(check_number[digit])
                end %= 10
                if end != 0:
                    end = 10 - end
                else:
                    end = end

                # Validasi nama file keluaran (huruf, angka, "-", "_", ".", " "<spasi>)
                valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_. "
                invalid = 0
                for char in filename:
                    if char not in valid_char:
                        invalid += 1
                if invalid == 0:
                    # Melakukan penggambaran canvas saat tidak ditemukan error
                    processing(start, first_group, last_group, end, canvas)
                    # Proses menyimpan file ke dalam local storage dilakukan saat invalid == 0
                    canvas.postscript(file = filename, colormode='color')
                else:
                    # Saat terdapat karakter invalid
                    tkmsg.showwarning("Invalid name!", "Please enter valid input name.")

            else:
                # Saat input yang diberikan user ke dalam program tidak valid
                tkmsg.showwarning("Wrong input!", "Please enter correct input code.")
        except:
            # Ketika terdapat error pada input user seperti penggunaan huruf
            tkmsg.showwarning("Wrong input!", "Please enter correct input code.")

    # Pemanggilan fungsi func saat user menekan enter
    root.bind('<Return>', func)


if __name__ == "__main__":
    # Menginisiasi dan memulai program dengan memanggil object root Tkinter, judul, dan perulangan layar
    root = Tk()
    root.title("EAN-13 [EugeniusMS]")
    main()
    root.mainloop()
