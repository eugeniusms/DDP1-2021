"""
Nama    : Eugenius Mario Situmorang
NPM     : 2106750484
Asdos   : LAH / Kelas-C
Program : dekdepedia.py
Aplikasi/program ini adalah program yang memiliki model marketplace dengan beberapa
fitur sederhana. Beberapa fitur dan poin penting mengenai program ini adalah pemodelan
server yang terbagi menjadi sisi pembeli, penjual, dan publik. Hal itu berkaitan dengan
fitur seperti tampilan laman barang jualan dan barang belian kemudian juga dengan toko
yang ditampilkan. Fitur ini mendukung adanya sistem terintegrasi antara satu event dengan
event lainnya di dalam aplikasi sehingga memudahkan user dalam melakukan manajemen data.
"""
# Inisiasi beberapa variabel global yang digunakan untuk menyimpan object address
list_user = {}
lst_toko = []
lst_sel = []

class User() :
    """
    Class berisi data setiap pengguna aplikasi, berisikan nama dan tipe yang berada
    dalam private variable sehingga tidak mudah untuk dilakukan perubahan dari luar.
    Untuk merubah dan membaca atribut digunakan getter dan setter dari decorator property.
    """
    def __init__(self, user_name, tipe):
        self.__user_name = user_name
        self.__tipe = tipe
      
    @property
    def user_name(self):
        pass

    @property
    def tipe(self):
        pass
    
    # Digunakan untuk mengambil data nama dari pengguna
    @user_name.getter
    def get_name(self): 
        return self.__user_name

    # Digunakan untuk mengambil data tipe dari pengguna
    @tipe.getter
    def get_tipe(self): 
        return self.__tipe

class Seller(User) : 
    """
    Class turunan dari User yang berisikan data yang dimiliki oleh Seller sebagai User
    aplikasi itu sendiri. Kemudian terdapat atribut pemasukan dan list barang jualan 
    yang mana pemasukan bersifat private sehingga digunakan getter dan setter sedangkan
    list barang jualan bersifat public untuk memudahkan pembacaan ke homepage (terminal).
    Terdapat pula beberapa method yang berfungsi untuk :
    1. Menambah Produk yang dijual
    2. Mengurangi Stok Barang
    3. Tampilan Barang yang dijual Penjual
    4. Tampilan Menu Seller
    """

    # Menginisiasikan object turunan dan baru
    def __init__(self, user_name, pemasukan, list_barang_jual):
        super().__init__(user_name, "SELLER")
        self.__pemasukan = pemasukan
        self.list_barang_jual = list_barang_jual

    # Getter dan Setter untuk pemasukan
    @property
    def pemasukan(self): 
        pass

    @pemasukan.getter
    def get_pemasukan(self):
        return self.__pemasukan

    @pemasukan.setter
    def set_pemasukan(self, input):
        self.__pemasukan = input 
    

    # Method untuk menambah produk yang dijual
    def tambah_product(self, data_produk) :
        self.list_barang_jual.append(data_produk)

    # Method untuk mengurangi stok barang jika terbeli
    def kurangi_product(self, produk_dibeli):
        # Pencarian barang sesuai permintaan operasi
        for i in range(len(self.list_barang_jual)): 
            nama_produk = self.list_barang_jual[i][0]
            # Saat barang didapati, kurangi stock (Keterangan : Index[2] adalah stock barang)
            if nama_produk == produk_dibeli:
                self.list_barang_jual[i][2] -= 1 

    # Method untuk memunculkan tampilan kepada user penjual tentang dagangannya (a-z)
    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        # Pemanggilan berulang barang dengan string-formatting agar didapati bentuk rapi
        for product in self.list_barang_jual: 
            nama_produk = product[0]
            harga = product[1]
            stock = product[2]
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(f"{nama_produk:<16}|{harga:<11}|{stock:<7}")
        print("-------------------------------------")

    # Method untuk menampilkan tampilan menu dari user dengan tipe penjual
    def menu(self) : 
        print(f"Selamat datang {self.get_name},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")

class Buyer(User) : 
    """
    Class turunan dari User yang berisikan data yang dimiliki oleh Buyer sebagai User
    aplikasi itu sendiri. Kemudian terdapat atribut saldo dan list barang yang akan dibeli
    yang mana saldo bersifat private sehingga digunakan getter dan setter sedangkan list
    barang yang akan dibeli bersifat public untuk memudahkan pembacaan ke homepage (terminal).
    Terdapat pula beberapa method yang berfunsgi untuk :
    1. Menambah Produk yang dibeli
    2. Tampilan Barang yang dibeli Pembeli
    3. Tampilan Menu Buyer
    """

    # Menginisiasikan object turunan dan baru
    def __init__(self, user_name, saldo, list_barang_beli):
        super().__init__(user_name, "BUYER")
        self.__saldo = saldo
        self.list_barang_beli = list_barang_beli

    # Getter dan Setter untuk saldo
    @property
    def saldo(self): 
        pass

    @saldo.getter
    def get_saldo(self):
        return self.__saldo

    @saldo.setter
    def set_saldo(self, input):
        self.__saldo = input 
    
    # Method untuk menambah daftar barang yang dibeli
    def beli_product(self, data_produk) :
        self.list_barang_beli.append(data_produk)

    # Method untuk menampilkan setiap produk yang dibeli Pembeli (a-z)
    def lihat_produk_saya_beli(self) : 
        print("\nBerikut merupakan barang yang saya beli")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Penjual ")
        print("-------------------------------------")
        # Pemanggilan berulang barang dengan string-formatting agar didapati bentuk rapi
        for product in self.list_barang_beli: 
            nama_produk = product[0]
            harga = product[1]
            seller= product[2]
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(f"{nama_produk:<16}|{harga:<11}|{seller:<7}")
        print("-------------------------------------")

    # Method untuk menampilkan tampilan menu dari user dengan tipe pembeli
    def menu(self):
        print(f"Selamat datang {self.get_name},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA")
        print("4. LOG_OUT")

class Product() :
    """
    Class independen yang menjembatani antara User Pembeli dan Penjual dalam melakukan
    transaksi. Terdapat inisiasi barang berdasarkan nama, harga, stock, dan penjualnya.
    Kemudian terdapat pula beberapa method untuk :
    "Melihat Isi Toko (Pertemuan Hasil Dagang Semua Penjual)"
    """
    global lst_toko 
    
    # Menginisasi object dalam class Product 
    def __init__(self, nama, harga, stock, seller):
        self.nama = nama
        self.harga = harga
        self.stock = stock
        self.seller = seller

    # Method untuk menampilkan toko secara keseluruhan (Dekdepedia)
    def toko_view(self):
        global lst_toko
        print("\nBerikut merupakan daftar product di Dekdepedia")
        print("------------------------------------------------")
        print("  Nama Product  |   Harga   | Stock |  Penjual")
        print("------------------------------------------------")
        # Pemanggilan berulang barang dengan string-formatting agar didapati bentuk rapi
        for product in lst_toko: 
            nama_produk = product.nama
            harga = product.harga
            stock = product.stock
            seller = product.seller
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(f"{nama_produk:<16}|{harga:<11}|{stock:<7}|{seller}")
        print("------------------------------------------------")

# Mengurutkan isi barang berdasarkan abjad
def sorting_lst(lst_obj):
    """
    Fungsi yang digunakan untuk mengurutkan isi list. Terdapat dua mode dalam fungsi :
    1. Mengurutkan list biasa berisikan object
    2. Menurutkan list object berisikan data biasa
    """
    # Menginisiasikan new_lst untuk pemrosesan dan send_lst untuk list yang dikembalikan
    new_lst = []
    send_lst = []
    # Mode 1 - Pengurutan list biasa berisikan object
    try:
        # Mengeluarkan bentuk obj dahulu menjadi bentuk data biasa
        for obj in lst_obj:
            new_lst.append([obj.nama, obj.harga, obj.stock, obj.seller])
        # Mengurutkan isi lst 2d dengan index = 0 (nama) sebagai patokan
        new_lst = sorted(new_lst,key=lambda l:l[0])

        # Mengembalikan isi list menjadi bentuk object kembali
        for nonobj in new_lst:
            isi = Product(nonobj[0], nonobj[1], nonobj[2], nonobj[3])
            send_lst.append(isi)

    except AttributeError:
        # Mode 2 - Pengurutan list object berisikan data biasa
        # Mengurutkan isi lst 2d dengan index = 0 (nama) sebagai patokan
        send_lst = sorted(lst_obj,key=lambda l:l[0])
    
    # Mengirimkan kembali hasil pengurutan
    return send_lst

def get_user(name, lst_obj):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in lst_obj:
        if user.get_name == name:
            return user

def get_product(name, lst_toko):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in lst_toko:
        if product.nama == name:
            return product

def sign_up(banyak_user):
    """
    Fungsi yang berjalan untuk mendaftarkan user yang baru bergabung, di fungsi ini terletak banyak
    validasi dari input yang dimasukkan oleh user. Kemudian dari data yang sudah divalidasi
    akan ditambahkan ke dalam sebuah struktur dictionary dengan key = nama dan value
    adalah bentuk list dari argumennya.
    """
    global list_user
    for i in range (banyak_user) : 
            data_user = input(str(i+1)+". ").split()
            # Membuat variabel untuk memudahkan maintain user dan validasi ketika index tidak ditemukan 
            try:
                tipe_user = data_user[0]
                nama_user = data_user[1]
            except:
                print("Akun tidak valid.")
                continue

            # Membuat validasi tipe user
            if tipe_user == "BUYER" or tipe_user == "SELLER":
                # Membuat validasi format input
                if (tipe_user == "BUYER" and len(data_user) != 3) or (tipe_user == "SELLER" and len(data_user) != 2):
                    print("Akun tidak valid.")
                    continue
                elif tipe_user == "BUYER": # Inisiasi saldo jika tipe user == BUYER
                    # Harus float lebih luas (kalau langsung integer tidak dapat validasi integer nanti)
                    try:
                        saldo_user = float(data_user[2])
                    except:
                        # Validasi jika terdapat input bukan bagian dari aritmetika
                        print("Akun tidak valid.")
                        continue

                    # Validasi saldo bilangan digit bulat jika terdapat sisa jika dibagi 1 (artinya belakang koma)
                    if saldo_user % 1 != 0 or saldo_user < 0:
                        print("Akun tidak valid.")
                        continue

                # Membuat validasi username
                for char in nama_user:
                    if char.isalnum() or char == "-" or char == "_":
                        nama_valid = True
                    else:
                        print("Akun tidak valid.")
                        continue

                # Validasi akun pernah terdaftar
                if nama_user in list_user.keys():
                    print("Username sudah terdaftar.")
                    continue

                # KETIKA SAMPAI DI SINI BERARTI AKUN VALID (TIDAK TERKENA CONTINUE)
                if tipe_user == "BUYER":
                    list_user[nama_user] = [tipe_user, saldo_user]
                elif tipe_user == "SELLER":
                    list_user[nama_user] = [tipe_user]

            else:
                # Ketika tipe user tidak valid
                print("Akun tidak valid.")
                continue

    print()
    # Mengembalikan list_user yang berbentuk dictionary dengan spesifikasi pada detail fungsi
    return list_user

def seller_menu(user_logged_in):
    """
    Fungsi yang mengatur menu pada user bertipe seller. Fungsi akan diawali dengan pemanggilan
    bentuk menu kemudian dilanjutkan perulangan untuk menampilkan pemasukan dan mengambil input
    pengguna. Selanjutnya terdapat beberapa input angka yang bisa dipilih :
    1. Memasukkan Data Produk Baru (Beserta Validasinya)
    2. Melihat Produk yang dijual
    3. Log Out dari Akun
    """
    global lst_toko
    # Memanggil method menu dari class seller
    Seller.menu(user_logged_in)

    # Perulangan untuk menampilkan pemasukan dan mengambil input user
    while True:
        # Penampilan pemasukan
        print(f"\nPemasukan anda {user_logged_in.get_pemasukan},")
        # Pengambilan input user
        perintah = input("Apa yang ingin Anda lakukan? ")

        if perintah == "1":
            # Data produk akan diambil dan displit menjadi bentuk list
            data_produk = input("Masukkan data produk : ").split()
            # Cek apakah produk pernah terdaftar belum, jika sudah dicontinue
            nama_produk = data_produk[0]
            cek_terdaftar = 0
            for produk in lst_toko:  
                if nama_produk == produk.nama:
                    print("Produk sudah pernah terdaftar.\n")
                    cek_terdaftar += 1 
            if cek_terdaftar > 0:
                continue

            # Membuat stock dan harga dari string menjadi integer agar bisa dioperasikan
            data_produk[1] = int(data_produk[1])
            data_produk[2] = int(data_produk[2])

            # Dikirim ke seller class untuk ditambahkan daftar produknya ke kolom penjual
            user_logged_in.tambah_product(data_produk)

            # Dikirim ke product class untuk ditambahkan daftar produknya ke kolom toko
            harga = int(data_produk[1])
            stock = int(data_produk[2])
            seller = user_logged_in.get_name
            # Menginiasi bentuk pengiriman (object)
            new_product = Product(nama_produk, harga, stock, seller)
            lst_toko.append(new_product)

        elif perintah == "2":
            # Mengurutkan isi dari list barang yang dijual sesuai abjad
            user_logged_in.list_barang_jual = sorting_lst(user_logged_in.list_barang_jual)
            # Memanggil method untuk menampilkan semua produk jualan 
            user_logged_in.lihat_produk_jualan_saya()

        elif perintah == "3":
            # Perintah untuk keluar dari akun (log out) dengan break perulangan
            print(f"Anda telah keluar dari akun {user_logged_in.get_name}\n")
            break

def buyer_menu(user_logged_in):
    """
    Fungsi yang mengatur menu pada user bertipe buyer. Fungsi akan diawali dengan pemanggilan
    bentuk menu kemudian dilanjutkan perulangan untuk menampilkan pemasukan dan mengambil input
    pengguna. Selanjutnya terdapat beberapa input angka yang bisa dipilih :
    1. Menampilkan Semua Isi Pada Toko
    2. Mengambil Masukan untuk Memilih Barang yang Ingin dibeli beserta Validasinya
    3. Menampilkan Riwayat Pembelian User 
    4. Log Out dari Akun
    """
    global lst_toko, lst_sel
    # Memanggil method menu dari class buyer
    Buyer.menu(user_logged_in)

    # Perulangan untuk menampilkan pemasukan dan mengambil input user
    while True:
        # Menampilkan isi saldo pengguna pada setiap perulangan
        print(f"\nSaldo anda {user_logged_in.get_saldo},")
        # Mengambil input perintah dari user
        perintah = input("Apa yang ingin Anda lakukan? ")

        if perintah == "1":
            # Melakukan pengurutan sesuai abjad untuk semua barang pada toko kemudian menampilkannya
            lst_toko = sorting_lst(lst_toko)
            Product.toko_view(lst_toko)

        elif perintah == "2":
            # Mengambil nama produk yang dibeli
            barang_beli = input("Masukkan barang yang ingin dibeli : ")

            # Cek validasi keterdaftaran barang
            cek_terdaftar = 0
            # Mengecek keberadaan barang
            for produk in lst_toko:  
                if barang_beli == produk.nama:
                    cek_terdaftar += 1 
            # Ketika barang tidak terdaftar (cek_terdaftar tetap 0)
            if not cek_terdaftar:
                print(f"Barang dengan nama {barang_beli} tidak ditemukan dalam Dekdepedia.")
                continue
            
            # Pemanggilan produk dan melakukan inisiasi variabel agar memudahkan pembacaan
            barang_beli = get_product(barang_beli, lst_toko)
            nama = barang_beli.nama
            harga = barang_beli.harga
            stock = barang_beli.stock
            seller = barang_beli.seller
            
            # Validasi ketika stok == 0 atau berarti sudah habis 
            if not stock:
                print("Maaf, stok produk telah habis.")
                continue
            # Validasi ketika saldo pengguna tidak mencukupi harga barang
            elif harga > user_logged_in.get_saldo:
                print(f"Maaf, saldo Anda tidak cukup untuk membeli {nama}")
                continue
            # Ketika didapati valid maka masuk ke dalam else di bawah
            else:
                # Mengurangi saldo user
                user_logged_in.set_saldo = user_logged_in.get_saldo - harga

                # Mengurangi stock jualan di akun penjual
                user_seller_in = get_user(seller, lst_sel)
                user_seller_in.kurangi_product(nama)

                # Mengurangi stock jualan di marketplace
                barang_beli.stock -= 1

                # Mengirimkan uang ke rekening penjual
                user_seller_in.set_pemasukan = user_seller_in.get_pemasukan + harga
                
                # Print berhasil membeli barang
                print(f"Berhasil membeli {nama} dari {seller}")
                
                # Memasukkan dalam catatan riwayat beli
                data_produk = [nama, int(harga), seller]
                # Kemudian dikirim ke buyer class
                user_logged_in.beli_product(data_produk)


        elif perintah == "3": 
            # Mengurutkan list barang yang dibeli user 
            user_logged_in.list_barang_beli = sorting_lst(user_logged_in.list_barang_beli)
            # Menampilkan riwayat pembelian
            user_logged_in.lihat_produk_saya_beli()

        elif perintah == "4":
            # Ketika user keluar dari akun dengan perintah == "4"
            print(f"Anda telah keluar dari akun {user_logged_in.get_name}\n")
            break

def main():
    """
    Fungsi utama yang berjalan di aplikasi. Kegunaan utama dari fungsi ini adalah menjembatani
    setiap perintah dan menu serta inisiasi pada awal aplikasi dijalankan. Adanya fungsi
    ini memudahkan transfer antar-data pengguna. Terdapat beberapa fitur di dalam
    fungsi ini sebagai berikut :
    """
    global lst_sel

    # Perulangan selama aplikasi/program dijalankan
    while True:
        # Penampilan dari menu perintah dalam program utama
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        # Pengambilan dan validasi input perintah adalah berupa digit
        pilih = input("Pilihan Anda: ")
        if not pilih.isdigit():
            print()
            continue

        if pilih == "1":
            # Ketika perintah pilih == "1" maka perlakukan pengambilan data user baru
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
            print("Data akun: ")

            # Jalankan fungsi sign_up untuk memproses pengambilan data baru dengan pengembalian list_user
            list_user = sign_up(banyak_user)

            # Inisiasi list object (obj = keseluruhan, sel = hanya akun seller, buy = hanya akun buyer)
            lst_obj = []
            lst_sel = []
            lst_buy = []
            # Penginisiasian user dan data menggunakan list_user yang sudah diolah
            for user, data in list_user.items():
                user_tipe = data[0]
                # Pengisian lst_obj
                lst_obj.append(User(user, user_tipe))
                if user_tipe == "SELLER":
                    # Pengisian lst_sel
                    lst_sel.append(Seller(user, 0, [])) #user_name, pemasukan, listbarang
                elif user_tipe == "BUYER":
                    saldo_buyer = int(data[1])
                    # Pengisian lst_buy
                    lst_buy.append(Buyer(user, saldo_buyer, []))

        elif (pilih == "2"):
            # Ketika perintah == "2" maka lakukan login pada aplikasi berdasar data sign up 
            user_name_login = input("user_name : ")

            # Ketika user login ada di dalam akun list_user
            if user_name_login in list_user.keys():
                
                # Mengambil user address object
                user_logged_in = get_user(user_name_login, lst_obj)
                print(f"Anda telah masuk dalam akun {user_logged_in.get_name} sebagai {user_logged_in.get_tipe}\n")
                
                # Validasi data dan tipe pengguna
                if user_logged_in.get_tipe == "SELLER":
                    # Mengambil address object seller dari lst_sel
                    user_logged_in = get_user(user_name_login, lst_sel)

                    # Aplikasi beralih ke menu seller
                    seller_menu(user_logged_in)

                elif user_logged_in.get_tipe == "BUYER":
                    # Mengambil address object buyer dari lst_buy
                    user_logged_in = get_user(user_name_login, lst_buy)

                    # Aplikasi beralih ke menu seller
                    buyer_menu(user_logged_in)

            else:
                # Ketika akun tidak ditemukan di dalam list_user
                print(f"Akun dengan user_name {user_name_login} tidak ditemukan\n")

        elif pilih == "3": 
            # Ketika input user == "3" maka akhiri aplikasi dengan mengucapkan terima kasih
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()

# Menjalankan program diinisiasi dari fungsi main()
if __name__ == "__main__":
    main()
