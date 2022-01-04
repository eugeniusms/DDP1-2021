import tkinter as tk
import tkinter.messagebox as tkmsg

"""
Nama    : Eugenius Mario Situmorang
NPM     : 2106750484
Program : bakunglapak.py
Program ini berbasiskan GUI dengan alur layaknya pembelian barang pada toko. Disediakan beberapa menu utama
seperti melihat daftar barang dengan stok tersedia kemudian terdapat pula form pembelian dan terakhir 
adalah riwayat transaksi yang pembeli lakukan.
"""

class Product(object):
    # Class ini menginisiasi produk dengan objek dan atribut nama, harga, dan stok.

    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # Method mengambil nama produk dari object
    def get_nama(self):
        return self.__nama

    # Method mengambil harga produk dari object
    def get_harga(self):
        return self.__harga

    # Method mengambil stok produk dari object
    def get_stok(self):
        return self.__stok

    # Method mengurangi stok berdasarkan parameter jumlah (setter)
    def set_stok(self, jumlah):
        self.__stok -= jumlah

class Buyer(object):
    # Class menginisiasikan pembelian yang dilakukan oleh user

    def __init__(self):
        self.__daftar_beli = {}

    # Method untuk menambah daftar pembelian dengan parameter produk dan jumlah
    def add_daftar_beli(self, produk, jumlah):
        if produk in self.__daftar_beli:
          self.__daftar_beli[produk] += jumlah
        else :
          self.__daftar_beli[produk] = jumlah

    # Method mengambil daftar pembelian dari object
    def get_daftar_beli(self):
      return self.__daftar_beli

class WindowLihatBarang(tk.Toplevel):
    # Toplevel adalah sebuah class yang membuat frame baru terpisah dari frame sebelumnya
    # Class ini dipanggil ketika user ingin melihat barang yang tersedia di dalam toko

    def __init__(self, product_dict, master = None):
        super().__init__(master)
        self.product_dict = product_dict
        self.title("Daftar Barang")
        self.create_widgets()

    """
    Method digunakan untuk menampilkan tampilan GUI dari program, dengan cara memberi label pada setiap
    grid yang sesuai kemudian pada row selanjutnya akan dipanggil perulangan dari daftar produk yang
    sudah dimasukkan ke dalam program (bentuk object dictionary). Lalu diakhiri dengan tombol "EXIT"
    untuk keluar dari window ini.
    """
    def create_widgets(self):
        self.lbl_judul = tk.Label(self, text = 'Daftar Barang Yang Tersedia').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, text = 'Harga').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, text = 'Stok Produk').grid(row = 1, column = 2)

        i = 2
        for nama, barang in sorted(self.product_dict.items()):
            tk.Label(self, text = f"{nama}").grid(row = i, column= 0)
            tk.Label(self, text = f"{barang.get_harga()}").grid(row = i, column= 1)
            tk.Label(self, text = f"{barang.get_stok()}").grid(row = i, column= 2)
            i += 1

        self.btn_exit = tk.Button(self, text = "EXIT", command = self.destroy).grid(row = i, column=1)

class WindowBeliBarang(tk.Toplevel):
    # Class ini dipanggil ketika user ingin membeli barang yang tersedia di dalam toko

    def __init__(self, buyer, product_dict, master = None, nama_barang = "", jumlah = 0):
        super().__init__(master)
        self.ent_nama_barang = nama_barang
        self.ent_jumlah = jumlah
        self.buyer = buyer
        self.product_dict = product_dict
        self.wm_title("Beli Barang")
        self.geometry("400x140")
        self.create_widgets()

    """
    Method digunakan untuk menampilkan tampilan GUI dari program, dengan cara memberi label pada setiap
    grid yang sesuai kemudian mengambil entry input dari nama barang dan jumlahnya dan diproses di dalam
    method beli_barang. Terakhir, terdapat tombol "EXIT" untuk menutup window.
    """
    def create_widgets(self):
        self.lbl_form = tk.Label(self, text = 'Form Beli Barang').grid(row = 0, column = 1)
        self.lbl_barang = tk.Label(self, text = 'Nama Barang').grid(row = 1, column = 0)

        self.ent_nama_barang = tk.Entry(self, width = 25)
        self.ent_nama_barang.grid(row = 1, column = 1)

        self.lbl_jumlah= tk.Label(self, text = 'Jumlah').grid(row = 2, column = 0)

        self.ent_jumlah = tk.Entry(self, width = 25)
        self.ent_jumlah.grid(row = 2, column = 1)

        self.btn_beli = tk.Button(self, text = "BELI", command = self.beli_barang).grid(row = 3, column = 1)
        self.btn_exit = tk.Button(self, text = "EXIT", command = self.destroy).grid(row = 4, column = 1)

    """
    Method ini memproses pembelian barang sesuai entry yang ada di dalam program. Ada beberapa alert
    sebagai penanda validitas input yang diberikan oleh user. Pertama kali yang dicek adalah bentuk
    jumlah yang valid kemudian isian kosong, lalu dilanjutkan dengan respon ketika barang tak ada
    dalam daftar dan stok produk habis dan terakhir adalah respon ketika barang berhasil terbeli.
    """
    def beli_barang(self):
        nama_barang = self.ent_nama_barang.get()
        jumlah = self.ent_jumlah.get()
        if jumlah.isdigit() and int(jumlah) > 0:
            jumlah = int(self.ent_jumlah.get())
        elif not jumlah == "":
            tkmsg.showwarning("JumlahNotValid", f"Jumlah harus bilangan bulat")

        if nama_barang == "" and jumlah == "":
            tkmsg.showwarning("Nama Barang dan Jumlah Empty", f"Maaf, anda belum memasukkan nama dan jumlah barang yang anda beli.")
        elif nama_barang == "":
            tkmsg.showwarning("NamaBarangEmpty", f"Maaf, anda belum memasukkan nama barang yang anda beli.")
        elif jumlah == "":
            tkmsg.showwarning("JumlahEmpty!", f"Maaf, anda belum memasukkan jumlah barang yang anda beli.")
        elif nama_barang not in self.product_dict:
            tkmsg.showwarning("BarangNotFound", f"Barang dengan nama {nama_barang} tidak ditemukan dalam BakungLapak.")
        elif self.product_dict[nama_barang].get_stok() - jumlah < 0:
            tkmsg.showwarning("StokEmpty", f"Maaf, stok produk telah habis.")
        else :
            barang = self.product_dict[nama_barang]
            buyer.add_daftar_beli(barang, jumlah)
            barang.set_stok(jumlah)
            self.ent_nama_barang.delete(0, tk.END)
            self.ent_jumlah.delete(0, tk.END)
            tkmsg.showinfo("Berhasil!", f"Berhasil membeli {nama_barang}.")

class WindowCheckOut(tk.Toplevel):
    # Class ini dipanggil ketika user ingin melihat barang yang terbeli

    def __init__(self, buyer, master = None):
        super().__init__(master)
        self.wm_title("Daftar Barang")
        self.daftar_dibeli = buyer.get_daftar_beli()
        self.create_widgets()

    """
    Method digunakan untuk menampilkan tampilan GUI dari program, dengan cara memberi label pada setiap
    grid yang sesuai pada row selanjutnya akan dipanggil perulangan dari daftar produk yang
    sudah dibeli di dalam program (bentuk object dictionary). Lalu diakhiri dengan tombol "EXIT"
    untuk keluar dari window ini.
    """
    def create_widgets(self):
        self.lbl_judul = tk.Label(self, text = 'Keranjangku').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, text = 'Harga Barang').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, text = 'Jumlah').grid(row = 1, column = 2)

        if not self.daftar_dibeli:
            self.lbl_daftar = tk.Label(self, text = 'Belum ada barang yang dibeli:(').grid(row = 2, column = 1)
        else:
            i = 2
            for barang, jumlah in self.daftar_dibeli.items():
                tk.Label(self, text = f"{barang.get_nama()}").grid(row = i, column= 0)
                tk.Label(self, text = f"{barang.get_harga()}").grid(row = i, column= 1)
                tk.Label(self, text = jumlah).grid(row = i, column= 2)
                i += 1

        self.btn_exit = tk.Button(self, text = "EXIT", command = self.destroy).grid(row = i, column=1)

class MainWindow(tk.Frame):
    # Class ini menjadi pembuka dari program dengan menampilkan window utama

    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.pack()
        self.create_widgets()

    """
    Method digunakan untuk menampilkan tampilan GUI dari program, dengan cara memberi label dan button yang sesuai
    sebagai penunjuk arah menuju menu yang sesuai ketika nanti diklik oleh user (melalui method di dalam class).
    Terdapat 4 tombol yaitu : 
    1. LIHAT DAFTAR BARANG
    2. BELI BARANG
    3. CHECK OUT
    4. EXIT
    """ 
    def create_widgets(self):
        self.label = tk.Label(self, text = 'Selamat datang di BakungLapak. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_barang = tk.Button(self, text = "LIHAT DAFTAR BARANG", command = self.popup_lihat_barang)
        self.btn_beli_barang = tk.Button(self, text = "BELI BARANG", command = self.popup_beli_barang)
        self.btn_check_out = tk.Button(self, text = "CHECK OUT", command = self.popup_check_out)
        self.btn_exit = tk.Button(self, text = "EXIT", command = quit)

        self.label.pack()
        self.btn_lihat_daftar_barang.pack()
        self.btn_beli_barang.pack()
        self.btn_check_out.pack()
        self.btn_exit.pack()

    # Method memanggil class untuk menampilkan window dari semua barang yang dijual dalam toko
    def popup_lihat_barang(self):
        WindowLihatBarang(self.product_dict)

    # Method memanggil class untuk menampilkan window pembelian barang oleh user
    def popup_beli_barang(self):
        WindowBeliBarang(self.buyer, self.product_dict)

    # Method memanggil class untuk menampilkan window dari semua barang yang dibeli dari toko oleh user
    def popup_check_out(self):
        WindowCheckOut(self.buyer)

    # Method untuk melakukan penutupan window utama
    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    # Menginisiasikan buyer
    buyer = Buyer()
    # Menginisiasikan daftar produk yang ada di dalam toko
    product_dict = {"Kebahagiaan" : Product("Kebahagiaan", 999999, 1),
                    "Kunci TP3 SDA" : Product("Kunci TP3 SDA", 1000000, 660)}

    # Memulai program dengan pemanggilan MainWindow
    m = MainWindow(buyer, product_dict)
    m.master.title("BakungLapak")
    m.master.mainloop()
