# Tugas 6 - Aldo Wista Fadhilah

# Variabel
produkBuah = ['Jeruk', 'Kiwi', 'Apel']
hargaProduk = [1000, 2000, 3000]
jumlahProduk = 3

# Function
# Show Produk
def show_product(itemList, hargalist):
    out = ''
    for i in range(0,len(itemList)):
        out += str(i+1) + ". " + str(itemList[i]) + "    Rp " + str(hargalist[i]) + "\n"
    return(out)

# Tambah Produk
def tambah_produk(index,produk,harga):
    produkBuah.insert((int(index)-1),produk)
    hargaProduk.insert((int(index)-1),int(harga))
    out = "\n--- Produk dan Harga telah ditambahkan ---\n\nBerikut adalah list produk baru:\n" + show_product(produkBuah,hargaProduk)
    return(out)

# Update Harga
def update_harga(index,harga):
    hargaProduk[int(index)-1] = int(harga)
    out = "Harga telah di update, berikut list produk baru: \n\n" + show_product(produkBuah,hargaProduk)
    return(out)

# Hapus Produk
def hapus_produk(index):
    produkBuah.pop((int(index)-1))
    hargaProduk.pop((int(index)-1))
    out = "Produk telah di update \n" + show_product(produkBuah,hargaProduk)
    return(out)


# Program Utama
checkIn = False
while checkIn == False:
    inMenu = input("\nMenu \n\n1) Show Produk \n2) Tambahkan Produk \n3) Update Harga \n4) Hapus Produk \n5) Exit\n\nMasukan input (1-4) : ")
    if inMenu.isdigit()==True and 1 <= int(inMenu) <= 5:
        checkIn = True
    else:
        print("Input Salah (1-5)\n\n")

# Menu 1
    if inMenu == '1':
        print(show_product(produkBuah,hargaProduk))
        checkInMenu1 = False
        while checkInMenu1 == False:
            inMenu1 = input("Kembali ke menu awal (y/n): ").lower()
            if inMenu1 == 'y' or inMenu1 == 'n':
                checkInMenu1 = True
            else :
                print("Input Salah (y/n)")

            if inMenu1 == 'y':
                print("\n\n")
                checkIn = False
            elif inMenu1 == 'n':
                checkInMenu1 = False

# Menu 2
    if inMenu == '2' :
    
        checkInMenu2 = False
        while checkInMenu2 == False:
            inMenu2_Index = input("\n--- Silahkan Masukan Menu yang akan dimasukan --- \nPilih nomor menu: ")
            inMenu2_Produk = input("Masukan nama produk: ").capitalize()
            inMenu2_Harga = input("Masukan harga produk: ")
            if inMenu2_Index.isdigit() == True and inMenu2_Produk.isalpha() == True and inMenu2_Harga.isdecimal() == True and 1 <= int(inMenu2_Index) <= (jumlahProduk+1)  :
                checkInMenu2 = True
                print(tambah_produk(inMenu2_Index,inMenu2_Produk,inMenu2_Harga))
                jumlahProduk+= 1
                checkIn = False
            else:
                print("\n--- Input salah, silahkan Input data kembali! ---")
                print("Pastikan nomor menu sesuai! (rentang 1 - menu terakhir)\n\n")
   

# Menu 3
    if inMenu == '3':
        print("--- Daftar Menu ---")
        print(show_product(produkBuah,hargaProduk))
        checkInMenu3 = False
        while checkInMenu3 == False:
            inMenu3_Index = input("Pilih nomor menu yang akan diupdate harganya: ")
            if inMenu3_Index.isdigit() == True:
                checkInMenu3 = True 
            else:
                print("\nInput Salah!\n")
        checkInMenu3_Harga = False
        while checkInMenu3_Harga == False:
            inMenu3_Harga = input("Masukan harga baru: ")
            if inMenu3_Harga.isdecimal()== True:
                checkInMenu3_Harga = True
            else :
                print("Input Salah")
        print(update_harga(inMenu3_Index, inMenu3_Harga))
        checkIn = False
                      

# Menu 4 
    if inMenu == '4':
        print("--- Daftar Menu ---")
        print(show_product(produkBuah,hargaProduk))
        checkInMenu4 = False
        while checkInMenu4 == False:
            inMenu4_Hapus = input("Masukan nomor produk yang akan dihapus: ")
            if inMenu4_Hapus.isdigit() == True and 1 <= int(inMenu4_Hapus) <= jumlahProduk:
                print(hapus_produk(inMenu4_Hapus))
                checkInMenu4 = True
                jumlahProduk-= 1
            else:
                print("Input Salah")
        checkIn = False

# Menu 5
    if inMenu == '5':
        print("Terima Kasih")
        checkIn = True
