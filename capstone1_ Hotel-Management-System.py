from tabulate import tabulate
import sys

daftar_hotel = [
    {
        "id_hotel": "HT001",
        "nama_hotel": "Hotel Merdeka",
        "bintang": 4,
        "lokasi": "Jakarta",
        "harga": 850000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT002",
        "nama_hotel": "Grand Nusantara",
        "bintang": 5,
        "lokasi": "Bali",
        "harga": 1500000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT003",
        "nama_hotel": "Hotel Bintang Lima",
        "bintang": 5,
        "lokasi": "Surabaya",
        "harga": 1200000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT004",
        "nama_hotel": "Seaside Resort",
        "bintang": 5,
        "lokasi": "Lombok",
        "harga": 1750000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT005",
        "nama_hotel": "Mountain View Hotel",
        "bintang": 3,
        "lokasi": "Bandung",
        "harga": 700000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT006",
        "nama_hotel": "Luxury Stay",
        "bintang": 5,
        "lokasi": "Jakarta",
        "harga": 1400000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT007",
        "nama_hotel": "Budget Inn",
        "bintang": 2,
        "lokasi": "Yogyakarta",
        "harga": 350000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT008",
        "nama_hotel": "City Central Hotel",
        "bintang": 3,
        "lokasi": "Medan",
        "harga": 600000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT009",
        "nama_hotel": "Royal Palace",
        "bintang": 5,
        "lokasi": "Semarang",
        "harga": 2000000,
        "Sisa Kamar": 10
    },
    {
        "id_hotel": "HT010",
        "nama_hotel": "Sunrise Hotel",
        "bintang": 4,
        "lokasi": "Bali",
        "harga": 950000,
        "Sisa Kamar": 10
    }
]

voucher_list = [
    {"kode": "WELCOME10", "diskon": 10},
    {"kode": "HOTEL5", "diskon": 5},
    {"kode": "PAYDAY30", "diskon": 30},
    {"kode": "PROMO20", "diskon": 20},
    {"kode": "STUDENT15", "diskon": 15},
    {"kode": "FLASHSALE25", "diskon": 25}
]


cart=[]

#input role
role = input("Masukkan role (admin/pengunjung): ").lower()
while role!="admin" and role!="pengunjung":
    print("Error: Role hanya antara admin/pengunjung")
    role = input("Masukkan role (admin/pengunjung): ").lower()

#main function
def mainMenu():
    if role == "admin":
        admin()     
    elif role=="pengunjung":
        pengunjung() 

#main function admin        
def admin():
    while True:
        print(f"""Main Menu \n1. Ta mpilkan list Hotel \n2. Menambahkan list hotel \n3. Menghapus list hotel \n4. Mengedit list hotel \n5. Memesan kamar hotel \n6. Exit\n""")
        menu=input("Masukkan angka Menu yang ingin dijalankan: ")

        while menu.isdigit()==False:
            print("Error: Menu harus berupa angka")
            menu=input("Masukkan angka daftar yang ingin dijalankan: ")

        menu=int(menu)
        if menu==1:
            menu1()
        elif menu==2:
            menu2()
        elif menu==3:
            menu3()
        elif menu==4:
            menu4()
        elif menu==5:
            menu5()
        elif menu==6:
            print("Anda telah keluar dari program")
            sys.exit()

#main function pengunjung 
def pengunjung():
    while True:
        print(f"""Main Menu \n1. Tampilkan list Hotel \n2. Memesan kamar hotel \n3. Exit\n""")
        menu=input("Masukkan angka Menu yang ingin dijalankan: ")
        while menu.isdigit()==False:
            print("Error: Menu harus berupa angka")
            menu=input("Masukkan angka daftar yang ingin dijalankan: ")
        menu=int(menu)
        if menu==1:
            menu1()
        elif menu==2:
            menu5()
        elif menu==3:
            print("Anda telah keluar dari program")
            sys.exit()

#fungsi kembali ke menu utama
def exit(menu_function):
    while True:
        a = input("Ingin kembali ke menu utama? (y/n): ")
        if a.lower() == "y":
            mainMenu()
            return
        elif a.lower() == "n":
            menu_function()   
            return
        else:
            print("Input harus berupa y/n")
        print("\n")

#fungsi untuk menampilkan index berdasarkan id
def idxHotel(id):
    for idx,val in enumerate(daftar_hotel):
        if val['id_hotel'].lower() == id.lower():
            return idx

#fungsi read (menampilkan data)
def menu1():
    while True:
        #menampilkan daftar menu
        print(f"""Tampilkan daftar Hotel \n1. Tampilkan semua daftar Hotel \n2. Tampilkan daftar berdasarkan range harga \n3. Tampilkan daftar berdasarkan lokasi \n4. Tampilkan daftar berdasarkan bintang \n5. Tampilkan berdasarkan urutan harga \n6. Kembali ke menu utama\n""")
        while True:
            menu=input("Masukkan angka daftar yang ingin dijalankan: ")
            if menu.isdigit()==False:
                print("Error: Menu harus berupa angka")
                continue
            elif int(menu) not in [1,2,3,4,5,6]:
                print("Error: Menu tidak tersedia")
                continue
            else:
                break
        menu=int(menu)

        #menampilkan semua daftar hotel
        if menu==1:
            if len(daftar_hotel)!=0:
                print("Semua Daftar Hotel: ")
                print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
            elif len(daftar_hotel)==0:
                print("Daftar hotel masih kosong")
            print("\n")

        #menampilkan hotel berdasarkan range harga
        elif menu==2:
            while True:
                try:
                    min = int(input("Masukkan harga minimum: "))
                    max = int(input("Masukkan harga maksimum: "))

                    if min < 0 or max < 0:
                        print("Error: Harga tidak boleh negatif. Silakan coba lagi.")
                        continue
                    elif min > max:
                        print("Error: Harga minimum tidak boleh lebih besar dari harga maksimum. Silakan coba lagi.")
                        continue
                    break 
                except ValueError:
                    print("Error: Harga harus berupa angka. Silakan coba lagi.")

            FilteredHotel=list(filter(lambda hotel: min<=hotel['harga']<=max,daftar_hotel))
            if len(FilteredHotel)!=0:
                print(f"Daftar Hotel dengan range harga Rp.{min} - Rp.{max}:")
                print(tabulate(FilteredHotel, headers="keys", tablefmt="fancy_grid"))
            elif len(FilteredHotel)==0:
                print(f"Hotel dengan range harga Rp.{min} - Rp.{max} tidak ada")
            print("\n")
        
        #menampilkan daftar berdasarkan lokasi
        elif menu==3:
            loc=input("Masukkan lokasi hotel:")

            FilteredHotel=list(filter(lambda hotel: (loc.lower())==(hotel['lokasi'].lower()),daftar_hotel))
            if len(FilteredHotel)!=0:
                print(f"Daftar Hotel di {loc}:")
                print(tabulate(FilteredHotel, headers="keys", tablefmt="fancy_grid"))
            elif len(FilteredHotel)==0:
                print(f"Daftar hotel tidak ada")
            print("\n") 

        #menampilkan daftar berdasarkan bintang hotel
        elif menu==4:
            while True:
                try:
                    bintang = int(input("Hotel bintang berapa yang ingin dicari: "))

                    if bintang < 1 or bintang > 5:
                        print("Masukkan range angka 1-5")
                        continue
                    break 
                except ValueError:
                    print("Error: Nilai harus berupa angka. Silakan coba lagi.")

            FilteredHotel=list(filter(lambda hotel: bintang==hotel['bintang'],daftar_hotel))
            if len(FilteredHotel)!=0:
                print(f"Daftar Hotel dengan bintang {bintang}:")
                print(tabulate(FilteredHotel, headers="keys", tablefmt="fancy_grid"))
            elif len(FilteredHotel)==0:
                print(f"Hotel bintang {bintang} tidak tersedia")
            print("\n")

        #sorting daftar hotel berdasarkan harga tertinggi atau terendah
        elif menu==5:
            while True:
                sort=input("1. harga tertinggi \n2. harga terendah \nurutkan berdasarkan (1/2)?: ")
                if sort not in ["1", "2"]:
                    print("Error: Pilihan harus 1 atau 2.")
                    continue 

                if sort=="1":
                    FilteredHotel=sorted(daftar_hotel, key=lambda hotel: hotel['harga'], reverse=True)
                    if len(FilteredHotel)!=0:
                        print(f"Daftar Hotel dari urutan tertinggi - terendah:")
                        print(tabulate(FilteredHotel, headers="keys", tablefmt="fancy_grid"))
                    elif len(FilteredHotel)==0:
                        print(f"List hotel tidak ada")
                elif sort=="2":
                    FilteredHotel=sorted(daftar_hotel, key=lambda hotel: hotel['harga'])
                    if len(FilteredHotel)!=0:
                        print(f"Daftar Hotel dari urutan terendah - tertinggi:")
                        print(tabulate(FilteredHotel, headers="keys", tablefmt="fancy_grid"))
                    elif len(FilteredHotel)==0:
                        print(f"List hotel tidak ada")
                print("\n")
                break
        elif menu==6:
            exit(menu1)
            print("\n")

#Add data hotel
def menu2(): 
    while True:
        #menampilkan menu
        print(f"""Tambahkan list hotel \n1. Tambah Data \n2. Exit\n""")
        while True:
            menu=input("Masukkan angka daftar yang ingin dijalankan: ")
            if menu.isdigit()==False:
                print("Error: Menu harus berupa angka")
                continue
            elif int(menu) not in [1,2]:
                print("Error: Menu tidak tersedia")
                continue
            else:
                break

        menu=int(menu)

        if menu==1:
            #input id hotel
            id=input("Masukkan id Hotel: ").upper()

            #pengecekan id di list data
            for i in range(len(daftar_hotel)):
                if id.lower() == (daftar_hotel[i]['id_hotel']).lower():
                    print("id sudah ada, masukkan id lain")
                    id=input("Masukkan id Hotel: ").capitalize()

            #input nama hotel
            nama=input("Masukkan Nama Hotel: ").title()

            #input bintang hotel
            while True:
                try:
                    bintang = int(input("Masukkan Bintang Hotel (1-5): "))

                    if bintang < 1 or bintang > 5:
                        print("Masukkan range angka 1-5")
                        continue
                    break 
                except ValueError:
                    print("Error: Nilai harus berupa angka. Silakan coba lagi.")

            #input lokasi hotel
            lokasi=input("Masukkan Lokasi Hotel: ").capitalize()

            #input harga hotel
            while True:
                try:
                    harga=int(input("Masukkan Harga Hotel: "))
                    if harga<0:
                        print("Harga tidak boleh minus")
                        continue
                    break
                except ValueError:
                    print("Error: Nilai harus berupa angka. Silakan coba lagi.")

            #input stock kamar hotel
            while True:
                try:
                    stock = int(input("Masukkan Stock Kamar Hotel: "))

                    if stock < 0:
                        print("Angka tidak boleh negatif")
                        continue
                    break 
                except ValueError:
                    print("Error: Nilai harus berupa angka. Silakan coba lagi.")

            #penambahan data ke dalam list
            x=input("Save Data? y/n: ")
            if x.lower() == 'y':
                hotel={"id_hotel":id,"nama_hotel":nama,"bintang":bintang,"lokasi":lokasi,"harga":harga, "Sisa Kamar":stock}
                daftar_hotel.append(hotel)
                print("Hotel sudah ditambahkan")
                print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
            else:
                continue
            print("\n")

        elif menu==2:
            exit(menu2)
            print("\n")

#menu hapus list hotel
def menu3():
    #menampilkan menu hapus hotel
    while True:
        print(f"""Menghapus list hotel \n1. Hapus Data \n2. Exit\n""")
        while True:
            menu=input("Masukkan angka daftar yang ingin dijalankan: ")
            if menu.isdigit()==False:
                print("Error: Menu harus berupa angka")
                continue
            elif int(menu) not in [1,2]:
                print("Error: Menu tidak tersedia")
                continue
            else:
                break

        menu=int(menu)

        if menu==1:
            while True:
                found=False
                print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))

                #input id hotel yang ingin dihapus
                id=input("Masukkan id Hotel yang ingin dihapus: ")

                #pengecekan id di dalam list
                for hotel in daftar_hotel:
                    if id.lower() == (hotel['id_hotel']).lower():
                        found=True
                
                if found==True:
                    break
                else:
                    print("id hotel tidak ditemukan")
                    print("\n")
                    continue
            
            #mengambil index dari id yang telah diinput
            for idx,val in enumerate(daftar_hotel):
                if val['id_hotel'].lower() == id.lower():
                    index=idx

            #penghapusan data di list daftar_hotel
            x=input("Delete Data? y/n: ")
            if x.lower() == 'y':
                daftar_hotel.pop(index)
                print("Data hotel berhasil dihapus!")
                print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
            else:
                continue
            print("\n")

        elif menu==2:
            exit(menu3)
            print("\n")

#menu mengedit list hotel
def menu4():
    #menampilkan menu yang tersedia
    while True:
        print(f"""Mengedit list hotel \n1. Edit Data \n2. Exit\n""")
        while True:
            menu=input("Masukkan angka daftar yang ingin dijalankan: ")
            if menu.isdigit()==False:
                print("Error: Menu harus berupa angka")
                continue
            elif int(menu) not in [1,2]:
                print("Error: Menu tidak tersedia")
                continue
            else:
                break 
            
        menu=int(menu)
        if menu==1:
            #menampilkan dan memilih fitur dari data hotel yang akan diedit
            print(f"""Fitur yang ingin diedit \n1. Nama \n2. Bintang \n3. Lokasi \n4. Harga \n5. Sisa Kamar""")
            while True:
                fitur=input("Masukkan angka fitur yang ingin diedit: ")
                if fitur.isdigit()==False:
                    print("Error: Menu harus berupa angka")
                    continue
                elif int(fitur) not in [1,2,3,4,5]:
                    print("Error: Menu tidak tersedia")
                    continue
                else:
                    break

            fitur=int(fitur)

            found=False
            print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))

            #input id hotel yang akan dihapus
            id=input("Masukkan id Hotel yang ingin diedit: ")

            #mengecek id yang telah diinput di dalam list daftar_hotel
            for hotel in daftar_hotel:
                if id.lower() == (hotel['id_hotel']).lower():
                    found=True
                    break
            
            #memastikan pengguna untuk mengubah data
            if found==True:
                x=input(f"Continue update?(y/n): ")
                if x.lower()=="y":
                    pass
                elif x.lower()=="n":
                    continue
                else:
                    print("Input harus berupa y/n")
                    continue
            else:
                print("id hotel tidak ditemukan")
                continue
            
            #cek index bersadarkan id hotel yang telah diinput
            index=idxHotel(id)
            if index is None:
                print("ID Hotel tidak valid. Silakan coba lagi.")
                continue
            
            #menu edit nama hotel
            if fitur==1:
                nama=input("Masukkan nama hotel baru: ").title()

                while True:
                    a = input("Update Data? (y/n): ")
                    if a.lower() == "y":
                        daftar_hotel[index]["nama_hotel"]=nama
                        print("Nama Hotel berhasil diupdate")
                        print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
                        break
                    elif a.lower() == "n":
                        menu4()  
                    else:
                        print("Input harus berupa y/n")
                        continue
                    print("\n")
            
            #menu edit bintang hotel
            elif fitur==2:
                while True:
                    try:
                        bintang=int(input("Masukkan bintang hotel baru: "))
                        if bintang < 1 or bintang > 5:
                            print("Masukkan range angka 1-5")
                            continue

                        while True:
                            a = input("Update Data? (y/n): ")
                            if a.lower() == "y":
                                daftar_hotel[index]["bintang"]=bintang
                                print("Bintang Hotel berhasil diupdate")
                                print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
                                break
                            elif a.lower() == "n":
                                menu4() 
                            else:
                                print("Input harus berupa y/n")
                                continue
                    except ValueError:
                        print("Error: Nilai harus berupa angka. Silakan coba lagi.")

            #menu edit lokasi hotel
            elif fitur==3:
                lokasi=input("Masukkan lokasi hotel baru: ").title()
                while True:
                    a = input("Update Data? (y/n): ")
                    if a.lower() == "y":
                        daftar_hotel[index]["lokasi"]=lokasi
                        print("Lokasi Hotel berhasil diupdate")
                        print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
                        break
                    elif a.lower() == "n":
                        menu4()   
                    else:
                        print("Input harus berupa y/n")
                        continue
                    print("\n")

            #menu edit harga hotel
            elif fitur==4:
                while True:
                    try:
                        harga=int(input("Masukkan harga hotel baru: "))
                        if harga < 0:
                            print("Error: Harga tidak boleh negatif. Silakan coba lagi.")
                            continue
                        daftar_hotel[index]["harga"]=harga
                        print("Nama Hotel berhasil diupdate")
                        print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
                        break 
                    except ValueError:
                        print("Error: Harga harus berupa angka. Silakan coba lagi.")

            #menu edit sisa kamar hotel
            elif fitur==5:
                while True:
                    try:
                        stock=int(input("Masukkan stock sisa kamar baru: "))
                        if stock < 0:
                            print("Angka tidak boleh negatif")
                            continue

                        while True:
                            a = input("Update Data? (y/n): ")
                            if a.lower() == "y":
                                daftar_hotel[index]["Sisa Kamar"]=stock
                                print("Bintang Hotel berhasil diupdate")
                                print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
                                break
                            elif a.lower() == "n":
                                menu4() 
                            else:
                                print("Input harus berupa y/n")
                                continue
                    except ValueError:
                        print("Error: Nilai harus berupa angka. Silakan coba lagi.")
            
        
        elif menu == 2:
            exit(menu4)

#menu pemesanan kamar hotel dan menu untuk melihat status pemesanan
def menu5():
    #menampilkan menu yang tersedia
    while True:
        print(f"""Mengedit list hotel \n1. Memesan Kamar \n2. Melihat Status Pemesanan \n3. Exit\n""")
        menu=input("Masukkan angka daftar yang ingin dijalankan: ")

        if menu.isdigit()==False:
            print("Error: Menu harus berupa angka")
            continue
        elif int(menu) not in [1,2,3]:
            print("Error: Menu tidak tersedia") 
            continue

        menu=int(menu)

        #menu pemesanan kamar hotel
        if menu==1:
            p=True
            while p:
                print("Daftar Hotel:")
                print(tabulate(daftar_hotel, headers="keys", tablefmt="fancy_grid"))
                
                #input index kamar yang ingin dipesan
                idx=input("Masukkan index kamar yang ingin dipesan: ")

                #pengecekan index kamar pada list daftar_hotel
                id=idxHotel(idx)
                if id is None or id >= len(daftar_hotel):
                    print("Error: Index hotel tidak valid")
                    continue

                #input jumlah kamar yang ingin dipesan 
                try:
                    jumlah = int(input("Masukkan jumlah kamar yang ingin dipesan: "))
                except ValueError:
                    print("Error: Jumlah kamar harus berupa angka")
                    continue
                
                #pengecekan sisa kamar yang tersedia berdasarkan jumlah kamar yang ingin dipesan
                if jumlah<=daftar_hotel[id]["Sisa Kamar"]:
                    kamar={"nama":(daftar_hotel[id]["nama_hotel"]),"jumlah":jumlah,"total":((daftar_hotel[id]["harga"])*jumlah),'Status': 'Booked'}
                    cart.append(kamar)
                    daftar_hotel[id]["Sisa Kamar"] -= jumlah
                else:
                    print(f"Sisa kamar tidak cukup, stock {daftar_hotel[id]["nama_hotel"]} tinggal {daftar_hotel[id]["Sisa Kamar"]} kamar")

                print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))    

                #input penambahan pemesanan
                pesan=input("Mau kamar lain?(ya/tidak) = ").lower()
                if pesan=="tidak":
                    p=False

            #menghitung total harga yang harus dibayar
            total= 0
            index=0
            for i in cart:
                total+=i["total"]
                index+=1
            index=0

            print(f"Total yang harus dibayar {total}")
            print("\n")
            
            #menu input kode voucher
            vocUsed=False
            voc=input("Apakah anda ingin menggunakan kode voucher?(ya/tidak): ")

            #pengecekan apakah voucher telah digunakan sebelumnya atau tidak
            if voc.lower()=="ya":
                if vocUsed:
                    print("Voucher telah digunakan sebelumnya")
                else:
                    #pilihan menu pada kode voucher
                    while True:
                        print(f"""1. Tampilkan kode voucher yang tersedia \n2. Masukkan kode voucher \n3. Back\n""")
                        menu=input("Masukkan angka daftar yang ingin dijalankan: ")

                        if menu.isdigit()==False:
                            print("Error: Menu harus berupa angka")
                            continue
                        elif int(menu) not in [1,2,3]:
                            print("Error: Menu tidak tersedia")
                            continue

                        menu=int(menu)

                        #menampilkan kode voucher yang tersedia beserta besaran persentase diskon
                        if menu==1:
                            print("Kode Voucher yang tersedia:")
                            print(tabulate(voucher_list, headers="keys", tablefmt="fancy_grid")) 
                            continue

                        #menginput kode voucher yang akan digunakan
                        elif menu==2:
                            if vocUsed:
                                print("Anda sudah menggunakan voucher sebelumnya. Tidak dapat menggunakan lagi.")
                                continue

                            kode=input("Masukkan kode voucher: ").upper()
                            found=False #mengecek kode voc ada atau tidak di daftar

                            for i in voucher_list:
                                if kode.upper()== i["kode"]:
                                    total= int(total-(total*(i['diskon']/100)))
                                    print(f"Kode voucher {kode} berhasil digunakan")
                                    print(f"harga pesanan menjadi {total}")
                                    vocUsed= True
                                    found=True
                                    break

                            if found==False:
                                print(f"Kode voucher {kode} tidak ditemukan")
                        elif menu==3:
                            break

            print(f"Total yang harus dibayar {total}")

            #menu pembayaran
            while True:
                try:
                    uang = int(input("Masukkan jumlah uang: "))
                    if uang < total:
                        print(f"Transaksi dibatalkan. Uangnya kurang sebesar: {total - uang}")
                    else:
                        print("Terima kasih, Hotel berhasil dipesan!")
                        if uang > total:
                            print(f"Uang kembali anda: {uang - total}")
                        break
                except ValueError:
                    print("Error: Masukkan jumlah uang yang valid")
                    continue
                
            for item in cart:
                item["Status"] = "Paid"

        #menampilkan daftar kamar yang telah dipesan
        if menu==2:
            print("\nStatus pemesanan kamar:")
            print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))

        if menu==3:
            exit(menu5)

mainMenu()