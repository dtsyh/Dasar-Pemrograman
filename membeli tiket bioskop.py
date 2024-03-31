list_film = ['Action', 'Horor', 'Drama', 'Comedy', 'Anime']
days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'] 

for film in list_film:
    print(f"Daftar film : {film}")

choice_genre = input("Pilih Genre: ")

if choice_genre.lower() == 'action':
    print("Pilihan film Action :")
    print("1. Lift Movie")
    print("2. Train To Busan")
    print("3. Alive")

    choice_film = int(input("Pilih Film: "))
    if choice_film == 1 or choice_film == 2 or choice_film == 3:
        name = input("Masukkan Nama: ")
        age = int(input("Masukkan Umur: "))
        num_people = int(input("Masukkan Jumlah Tiket: "))
        hari = input("Masukkan hari (Senin-Minggu) : ").capitalize()
        if hari in days[:5]:
            harga_tiket = 35000
        elif hari == 'sabtu':
            harga_tiket = 40000
        elif hari == 'minggu':
            harga_tiket = 50000
        else:
            print("Hari tidak valid")
            exit()
        total_harga = num_people * harga_tiket
        if age >= 17:
            print (f"{name}, Anda diperbolehkan untuk menonton film ini.")
        else:
            print(f"{name}, Anda tidak diperbolehkan untuk menonton film ini karena usia Anda belum mencapai 17 tahun.")
    else: 
        print("Pilihan film tidak tersedia.")
    
elif choice_genre.lower() == 'horor':
    print("Pilihan film Horor :")
    print("1. Annabelle")
    print("2. The Conjuring")
    print("3. Pengabdi Setan")

    choice_film = int(input("Pilih Film: "))
    if choice_film == 1 or choice_film == 2 or choice_film == 3:
        name = input("Masukkan Nama: ")
        age = int(input("Masukkan Umur: "))
        num_people = int(input("Masukkan Jumlah Tiket: "))
        hari = input("Masukkan hari (Senin-Minggu) : ").capitalize()
        if hari in days[:5]:
            harga_tiket = 35000
        elif hari == 'sabtu':
            harga_tiket = 40000
        elif hari == 'minggu':
            harga_tiket = 50000
        else:
            print("Hari tidak valid")
            exit()
        total_harga = num_people * harga_tiket
        if age >= 17:
            print (f"{name}, Anda diperbolehkan untuk menonton film ini.")
        else:
            print(f"{name}, Anda tidak diperbolehkan untuk menonton film ini karena usia Anda belum mencapai 17 tahun.")
    else: 
        print("Pilihan film tidak tersedia.")

elif choice_genre.lower() == 'drama':
    print("Pilihan film Drama :")
    print("1. 20th Century Girl")
    print("2. Miracle In Cell No. 7")
    print("3. Dilan 1990")

    choice_film = int(input("Pilih Film: "))
    if choice_film == 1 or choice_film == 2 or choice_film == 3:
        name = input("Masukkan Nama: ")
        age = int(input("Masukkan Umur: "))
        num_people = int(input("Masukkan Jumlah Tiket :"))
        hari = input("Masukkan hari (Senin-Minggu) : ").capitalize()
        if hari in days[:5]:
            harga_tiket = 35000
        elif hari == 'sabtu':
            harga_tiket = 40000
        elif hari == 'minggu':
            harga_tiket = 50000
        else:
            print("Hari tidak valid")
            exit()
        total_harga = num_people * harga_tiket
        if age >= 17:
            print (f"{name}, Anda diperbolehkan untuk menonton film ini.")
        else:
            print(f"{name}, Anda tidak diperbolehkan untuk menonton film ini karena usia Anda belum mencapai 17 tahun.")
    else: 
        print("Pilihan film tidak tersedia.")

elif choice_genre.lower() == 'comedy':
    print("Pilihan film Comedy :")
    print("1. Agak Laen")
    print("2. Cek Toko Sebelah")
    print("3. Hello Ghost")

    choice_film = int(input("Pilih Film: "))
    if choice_film == 1 or choice_film == 2 or choice_film == 3:
        name = input("Masukkan Nama: ")
        age = int(input("Masukkan Umur: "))
        num_people = int(input("Masukkan Jumlah Tiket: "))
        hari = input("Masukkan hari (Senin-Minggu) : ").capitalize()
        if hari in days[:5]:
            harga_tiket = 35000
        elif hari == 'sabtu':
            harga_tiket = 40000
        elif hari == 'minggu':
            harga_tiket = 50000
        else:
            print("Hari tidak valid")
            exit()
        total_harga = num_people * harga_tiket
        if age >= 17:
            print (f"{name}, Anda diperbolehkan untuk menonton film ini.")
        else:
            print(f"{name}, Anda tidak diperbolehkan untuk menonton film ini karena usia Anda belum mencapai 17 tahun.")
    else:
        print("Pilihan film tidak tersedia.")

elif choice_genre.lower() == 'anime':
    print("Pilihan film Anime :")
    print("1. Demon Slayer")
    print("2. One Piece")
    print("3. Naruto")

    choice_film = int(input("Pilih Film: "))
    if choice_film == 1 or choice_film == 2 or choice_film == 3:
        name = input("Masukkan Nama: ")
        age = int(input("Masukkan Umur: "))
        num_people = int(input("Masukkan Jumlah Tiket: "))
        hari = input("Masukkan hari (Senin-Minggu) : ").capitalize()
        if hari in days[:5]:
            harga_tiket = 35000
        elif hari == 'sabtu':
            harga_tiket = 40000
        elif hari == 'minggu':
            harga_tiket = 50000
        else:
            print("Hari tidak valid")
            exit()
        total_harga = num_people * harga_tiket
        if age >= 17:
            print (f"{name}, Anda diperbolehkan untuk menonton film ini.")
        else:
            print(f"{name}, Anda tidak diperbolehkan untuk menonton film ini karena usia Anda belum mencapai 17 tahun.")
    else:
        print("Pilihan film tidak tersedia.")

else:
    print("Pilihan genre tidak tersedia.")

# Menampilkan struk pembelian tiket
print("\n================= Struk Pembelian Tiket =================")
print(f"Genre Film : {choice_genre}")
if choice_film == 1:
    if choice_genre.lower() == 'action':
        print("Judul Film: Lift Movie")
elif choice_film == 2:
    if choice_genre.lower() == 'action':
        print("Judul Film: Train To Busan")
elif choice_genre.lower() == 'horor':
            print("Judul Film: The Conjuring")
elif choice_film == 3:
        if choice_genre.lower() == 'action':
            print("Judul Film: Alive")
        elif choice_genre.lower() == 'horor':
            print("Judul Film: Pengabdi Setan")
        elif choice_genre.lower() == 'drama':
            print("Judul Film: Dilan 1990")
        elif choice_genre.lower() == 'comedy':
            print("Judul Film: Hello Ghost")
        elif choice_genre.lower() == 'anime':
            print("Judul Film: Naruto")
print(f"Jumlah tiket : {num_people}")
print(f"Hari : {hari}")
print(f"Total Harga : {total_harga}")
print("=========================================================")