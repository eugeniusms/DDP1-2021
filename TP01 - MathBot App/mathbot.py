import random

# Menginisiasi agar bisa break ketika input mode = 4
jenis_kuis = 0
print("Halo, selamat datang di Mathbot \nPilih Mode:")

# Melakukan perulangan selama program dipanggil, berguna saat ganti mode
while True:
    # Menyusun break saat akhiri program level 2
    if int(jenis_kuis) == 4:
        print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
        # Mengakhiri perulangan program
        break
    print("1. Penjumlahan \n2. Pengurangan \n3. Campur \n4. Akhiri program \n")

    # Input perintah untuk kuis
    perintah = input("Masukkan perintah: ")
    print()
    if perintah.isdigit():
        # Set perintah ke integer untuk di if
        perintah = int(perintah)
        if perintah == 1:
            print("Baik, pilih mode penjumlahan ya, sekarang pilih jenis kuis apa?")
        elif perintah == 2:
            print("Baik, pilih mode pengurangan ya, sekarang pilih jenis kuis apa?")
        elif perintah == 3:
            print("Baik, pilih mode campur ya, sekarang pilih jenis kuis apa?")
        elif perintah == 4:
            print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
            # Mengakhiri perulangan program
            break
        else:
            # Ketika input jenis_kuis tidak valid (digit selain 1 - 4) maka continue perulangan selanjutnya
            print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
            print()
            continue
    else:
        # Ketika input jenis_kuis tidak valid (not digit) maka continue perulangan selanjutnya
        print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
        print()
        continue

    # Selama benar != merujuk pada akhiri program maka jalankan program ini terus menerus
    while True:
        print("Pilih kuis:  \n1. Kuis Lepas \n2. Kuis 5 \n3. Ganti mode \n4. Akhiri Program \n")
        jenis_kuis = input("Masukkan jenis kuis: ")
        print()
        jawaban = ""

        # Digunakan untuk mengecek jenis kuis agar tidak ada input selain angka
        if not jenis_kuis.isdigit():
            print()
            print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
            print()
            continue

        # Masuk ke jenis "Kuis Lepas"
        if int(jenis_kuis) == 1:
            # Akhiri kuis ketika kita menulis jawaban = "akhiri kuis"
            while jawaban != "akhiri kuis":
                # Membuat angka random untuk penambahan dan pengurangan beserta kuncinya
                angka_penambahan1 = random.randint(0, 10)
                angka_penambahan2 = random.randint(0, 10) 
                kunci_penambahan = str(angka_penambahan1 + angka_penambahan2)
                angka_pengurangan1 = random.randint(0, 10)
                angka_pengurangan2 = random.randint(0, 10)
                # Selama angka pengurangan kedua lebih besar lakukan random agar hasil tidak negatif (sebelah kiri > kanan)
                while angka_pengurangan2 > angka_pengurangan1:
                    angka_pengurangan1 = random.randint(0, 10)
                    angka_pengurangan2 = random.randint(0, 10)
                kunci_pengurangan = str(angka_pengurangan1 - angka_pengurangan2)

                # Ketika dimasukkan di atas perintah = 1 (Penambahan)
                if perintah == 1:    
                    print("Berapa "+str(angka_penambahan1)+" + "+str(angka_penambahan2)+"?")
                    jawaban = input("Jawaban: ")
                    # Mencocokan jawaban dengan kunci jawaban
                    if jawaban.isdigit():
                        if jawaban == kunci_penambahan:
                            print("Hore benar!")
                        else:
                            print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_penambahan)
                    # Ketika input bukan suatu angka 
                    else:
                        # Ketika jawaban berisi "akhiri kuis" maka break perulangan kuis lepas dan masuk ke loop pilih kuis
                        if jawaban == "akhiri kuis":
                            break
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                # Ketika dimasukkan di atas perintah = 2 (Pengurangan)      
                elif perintah == 2:
                    print("Berapa "+str(angka_pengurangan1)+" - "+str(angka_pengurangan2)+"?")
                    jawaban = input("Jawaban: ")
                    # Mencocokan jawaban dengan kunci jawaban
                    if jawaban.isdigit():
                        if jawaban == kunci_pengurangan:
                            print("Hore benar!")
                        else:
                            print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_pengurangan)
                    # Ketika input bukan suatu angka 
                    else:
                        if jawaban == "akhiri kuis":
                            break
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                # Ketika dimasukkan di atas perintah = 3 (Campur)
                elif perintah == 3:
                    # Membuat 2 angka acak untuk mengacak operasi 0 : penambahan, 1 : pengurangan
                    angka_acak_operator = random.randint(0, 1)
                    # Ketika mendapat acak 0 maka lakukan pertanyaan penambahan
                    if angka_acak_operator == 0:
                        print("Berapa "+str(angka_penambahan1)+" + "+str(angka_penambahan2)+"?")
                        jawaban = input("Jawaban: ")
                        # Mencocokan jawaban dengan kunci jawaban
                        if jawaban.isdigit():
                            if jawaban == kunci_penambahan:
                                print("Hore benar!")
                            else:
                                print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_penambahan)
                        # Ketika input bukan suatu angka 
                        else:
                            if jawaban == "akhiri kuis":
                                break
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                    
                    # Ketika mendapat acak 1 maka lakukan pertanyaan pengurangan
                    else:
                        print("Berapa "+str(angka_pengurangan1)+" - "+str(angka_pengurangan2)+"?")
                        jawaban = input("Jawaban: ")
                        # Mencocokan jawaban dengan kunci jawaban
                        if jawaban.isdigit():
                            if jawaban == kunci_pengurangan:
                                print("Hore benar!")
                            else:
                                print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_pengurangan)
                        # Ketika input bukan suatu angka 
                        else:
                            if jawaban == "akhiri kuis":
                                break
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                    
                print()
            print()

            
        # Masuk ke jenis "Kuis 5"
        if int(jenis_kuis) == 2:
            # Menginisiasi untuk menghitung perulangan dan reset score
            hitung_program = 1
            skor = 0
        # Masuk ke jenis "Kuis Lepas"
            # Akhiri kuis ketika kita menulis jawaban = "akhiri kuis"
            while hitung_program <= 5:
                # Membuat angka random untuk penambahan dan pengurangan beserta kuncinya
                angka_penambahan1 = random.randint(0, 10)
                angka_penambahan2 = random.randint(0, 10) 
                kunci_penambahan = str(angka_penambahan1 + angka_penambahan2)
                angka_pengurangan1 = random.randint(0, 10)
                angka_pengurangan2 = random.randint(0, 10)
                # Selama angka pengurangan kedua lebih besar lakukan random agar hasil tidak negatif (sebelah kiri > kanan)
                while angka_pengurangan2 > angka_pengurangan1:
                    angka_pengurangan1 = random.randint(0, 10)
                    angka_pengurangan2 = random.randint(0, 10)
                kunci_pengurangan = str(angka_pengurangan1 - angka_pengurangan2)

                # Ketika dimasukkan di atas perintah = 1 (Penambahan)
                if perintah == 1:    
                    print("Pertanyaan "+str(hitung_program)+": Berapa "+str(angka_penambahan1)+" + "+str(angka_penambahan2)+"?")
                    jawaban = input("Jawaban: ")
                    # Mencocokan jawaban dengan kunci jawaban
                    if jawaban.isdigit():
                        if jawaban == kunci_penambahan:
                            print("Hore benar!")
                            skor += 20
                        else:
                            print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_penambahan)
                    # Ketika input bukan suatu angka 
                    else:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                # Ketika dimasukkan di atas perintah = 2 (Pengurangan)      
                elif perintah == 2:
                    print("Pertanyaan "+str(hitung_program)+": Berapa "+str(angka_pengurangan1)+" - "+str(angka_pengurangan2)+"?")
                    jawaban = input("Jawaban: ")
                    # Mencocokan jawaban dengan kunci jawaban
                    if jawaban.isdigit():
                        if jawaban == kunci_pengurangan:
                            print("Hore benar!")
                            skor += 20
                        else:
                            print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_pengurangan)
                    # Ketika input bukan suatu angka 
                    else:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                # Ketika dimasukkan di atas perintah = 3 (Campur)
                elif perintah == 3:
                    # Membuat 2 angka acak untuk mengacak operasi 0 : penambahan, 1 : pengurangan
                    angka_acak_operator = random.randint(0, 1)
                    # Ketika mendapat acak 0 maka lakukan pertanyaan penambahan
                    if angka_acak_operator == 0:
                        print("Pertanyaan "+str(hitung_program)+": Berapa "+str(angka_penambahan1)+" + "+str(angka_penambahan2)+"?")
                        jawaban = input("Jawaban: ")
                        # Mencocokan jawaban dengan kunci jawaban
                        if jawaban.isdigit():
                            if jawaban == kunci_penambahan:
                                print("Hore benar!")
                                skor += 20
                            else:
                                print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_penambahan)
                        # Ketika input bukan suatu angka 
                        else:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                    
                    # Ketika mendapat acak 1 maka lakukan pertanyaan pengurangan
                    else:
                        print("Pertanyaan "+str(hitung_program)+": Berapa "+str(angka_pengurangan1)+" - "+str(angka_pengurangan2)+"?")
                        jawaban = input("Jawaban: ")
                        # Mencocokan jawaban dengan kunci jawaban
                        if jawaban.isdigit():
                            if jawaban == kunci_pengurangan:
                                print("Hore benar!")
                                skor += 20
                            else:
                                print("Masih kurang tepat, ya. Jawabannya adalah "+kunci_pengurangan)
                        # Ketika input bukan suatu angka 
                        else:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                
                hitung_program += 1
                    
                print()
            print("Score kamu: "+str(skor))
            print()
        
        # Menyusun break saat ganti mode
        if int(jenis_kuis) == 3:
            break
        
        # Menyusun break saat akhiri program level 1
        if int(jenis_kuis) == 4:
            break
        
        # Ketika input jenis_kuis tidak valid maka continue perulangan selanjutnya
        if (int(jenis_kuis) < 1) or (int(jenis_kuis) > 4):
            print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
            print()
            continue

        
