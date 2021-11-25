lst_toko = []

class User() :
    def __init__(self, user_name, tipe):
        self.__user_name = user_name
        self.__tipe = tipe
        # TODO : Tambahkan kode untuk inisiasi atribut lainnya

    # TODO : lengkapi method getter
    @property
    def user_name(self):
        pass

    @property
    def tipe(self):
        pass

    @user_name.getter
    def get_name(self): 
        return self.__user_name

    @tipe.getter
    def get_tipe(self): 
        return self.__tipe

class Seller(User) : 
    
    def __init__(self, user_name, pemasukan, list_barang_jual):
        super().__init__(user_name, "SELLER")
        self.__pemasukan = pemasukan
        self.list_barang_jual = list_barang_jual
        # TODO : implementasikan constructor dari class Seller

    # TODO : lengkapi getter dan setter
    @property
    def pemasukan(self): 
        pass

    @pemasukan.getter
    def get_pemasukan(self):
        return self.__pemasukan

    @pemasukan.setter
    def set_pemasukan(self, input):
        self.__pemasukan = input 
 
    # TODO : implementasikan method untuk tambahkan_produk dan lihat_daftar_produk_saya
    # Anda boleh memodifikasi ataupun menambahkan method sesuai dengan kebutuhan
    def tambah_product(self, data_produk) :
        self.list_barang_jual.append(data_produk)

    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        for product in self.list_barang_jual : 
            nama_produk = product[0]
            harga = product[1]
            stock = product[2]
            # TODO : cetak tiap product dengan urutan alphabetical
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(f"{nama_produk:<16}|{harga:<11}|{stock:<7}")

        print("-------------------------------------\n")

    def menu(self) : 
        # TODO : implementaiskan menu untuk tipe user seller
        print(f"Selamat datang {self.get_name},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")
        print()
        print(f"Pemasukan anda {self.get_pemasukan},")


# TODO : implementasikan class Buyer
class Buyer(User) : 

    def __init__(self, user_name, saldo, list_barang_beli):
        super().__init__(user_name, "BUYER")
        self.__saldo = saldo
        self.list_barang_beli = list_barang_beli

    @property
    def saldo(self): 
        pass

    @saldo.getter
    def get_saldo(self):
        return self.__saldo

    @saldo.setter
    def set_saldo(self, input):
        self.__saldo = input 
    
    def beli_product(self, data_produk) :
        self.list_barang_beli.append(data_produk)

    def menu(self):
        print(f"Selamat datang {self.get_name},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA")
        print("4. LOG_OUT")
        print()
        print(f"Saldo anda {self.get_saldo},")


# TODO : implementasikan class Product
class Product() :
    global lst_toko 
    
    def __init__(self, nama, harga, stock, seller):
        self.nama = nama
        self.harga = harga
        self.stock = stock
        self.seller = seller

    def toko_view(self):
        global lst_toko
        print("Berikut merupakan daftar product di Dekdepedia")
        print("------------------------------------------------")
        print("------------------------------------------------")
        print("  Nama Product  |   Harga   | Stock |  Penjual")
        print("------------------------------------------------")
        for product in lst_toko: 
            nama_produk = product.nama
            harga = product.harga
            stock = product.stock
            seller = product.seller
            # TODO : cetak tiap product dengan urutan alphabetical
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(f"{nama_produk:<16}|{harga:<11}|{stock:<7}|{seller}")

        print("------------------------------------------------\n")



# method get_user dan get_product tidak perlu diubah, 
# silakan manfaatkan method ini untuk mendapatkan user dan produk yang dibutuhkan
def get_user(name, lst_obj):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in lst_obj:
        if user.get_name == name:
            return user

def get_product(name):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

list_user = []
list_product = []

def sign_up(banyak_user):
    """
    Fungsi yang berjalan untuk mendaftarkan user yang baru bergabung, di fungsi ini terletak banyak
    validasi dari input yang dimasukkan oleh user.
    """
    list_user = {}
    for i in range (banyak_user) : 
            data_user = input(str(i+1)+". ").split()
            # TODO : implementasikan sign up

            # Membuat variabel untuk memudahkan maintain user
            # Membuat validasi ketika index tidak ditemukan 
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

                # KETIKA SAMPAI DI SINI BERARTI AKUN VALID (TIDAK KENA CONTINUE)
                if tipe_user == "BUYER":
                    list_user[nama_user] = [tipe_user, saldo_user]
                elif tipe_user == "SELLER":
                    list_user[nama_user] = [tipe_user]

            else:
                # Ketika tipe user tidak valid
                print("Akun tidak valid.")
                continue

    return list_user

def seller_menu(user_logged_in):
    global lst_toko
    while True:
        # Memanggil method menu dari class seller
        Seller.menu(user_logged_in)
        
        perintah = input("Apa yang ingin Anda lakukan? ")
        if perintah == "1":
            data_produk = input("Masukkan data produk : ").split() # azuz 10000 1
            # Dikirim ke seller class
            user_logged_in.tambah_product(data_produk)
            # Dikirim ke product class
            nama_produk = data_produk[0]
            harga = int(data_produk[1])
            stock = int(data_produk[2])
            seller = user_logged_in.get_name
            new_product = Product(nama_produk, harga, stock, seller)
            lst_toko.append(new_product)

        elif perintah == "2":
            user_logged_in.lihat_produk_jualan_saya()
        elif perintah == "3":
            print(f"Anda telah keluar dari akun {user_logged_in.get_name}\n")
            break

    # Address isi toko
    print(lst_toko)

def buyer_menu(user_logged_in):
    global lst_toko
    while True:
        # Memanggil method menu dari class seller
        Buyer.menu(user_logged_in)
        
        perintah = input("Apa yang ingin Anda lakukan? ")
        if perintah == "1":
            Product.toko_view(lst_toko)
        elif perintah == "2":
            user_logged_in.lihat_produk_jualan_saya()
        elif perintah == "4":
            print(f"Anda telah keluar dari akun {user_logged_in.get_name}\n")
            break

def main():
    while True:
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        pilih = input("Pilihan Anda: ")

        if (pilih == "1") : 
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
            
            print("Data akun: ")
            list_user = sign_up(banyak_user)
            print(list_user)
            # Inisiasi object berdasarkan list
            lst_obj = []
            lst_sel = []
            lst_buy = []
            for user, data in list_user.items():
                user_tipe = data[0]
                lst_obj.append(User(user, user_tipe))
                if user_tipe == "SELLER":
                    lst_sel.append(Seller(user, 0, [])) #user_name, pemasukan, listbarang
                elif user_tipe == "BUYER":
                    lst_buy.append(Buyer(user, 0, []))


            # ADA 3 LST OBJECT USER, SELLER, BUYER
            print(lst_obj)
            print(lst_sel)
            print(lst_buy)

        elif (pilih == "2") : 
            user_name_login = input("user_name : ")
            if user_name_login in list_user.keys():
                
                # Mengambil address object User
                user_logged_in = get_user(user_name_login, lst_obj)
                print(user_logged_in)

                # Validasi data pengguna
                print(f"Anda telah masuk dalam akun {user_logged_in.get_name} sebagai {user_logged_in.get_tipe}\n")
                
                # user_logged_in masih dalam User class
                if user_logged_in.get_tipe == "SELLER":
                    # Mengambil address object Seller
                    user_logged_in = get_user(user_name_login, lst_sel)
                    print(user_logged_in)

                    # BUAT NGECEK DOANG (masih di User classnya)
                    print(user_logged_in.get_name)
                    print(user_logged_in.get_tipe)
                    # obj = lst_obj
                    # user_logged_in = Seller(user_name_login, )

                    # Ke menu seller
                    seller_menu(user_logged_in)

                elif user_logged_in.get_tipe == "BUYER":
                    # Mengambil address object Seller
                    user_logged_in = get_user(user_name_login, lst_buy)
                    print(user_logged_in)

                    buyer_menu(user_logged_in)

                    


            else:
                print(f"Akun dengan user_name {user_name_login} tidak ditemukan\n")

        elif (pilih == "3") : 
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()

if __name__ == "__main__":
    main()
