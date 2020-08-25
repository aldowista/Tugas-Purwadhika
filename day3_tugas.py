#Tugas 3 - Aldo Wista Fadhilah
hargaMenu1 = 25000
hargaMenu2 = 20000
hargaMenu3 = 15000

Menu1 = "Ayam Bakar"
Menu2 = "Ayam Penyet"
Menu3 = "Ayam Geprek"

belajar1 = "Luas Segitiga"
belajar2 = "Luas Trapesium"

rumus1 =  1/2 
rumus2 = 1/2

print("Pilih Menu")
print("1. Belanja")
print("2. Belajar")
print("3. Exit")
inMenu = (input("Pilih menu nomor: "))
if inMenu.isdigit == False or inMenu != "1" or inMenu != "2" or inMenu != "3":
    print("Input yang anda masukan salah")

if inMenu == "1" :
    print("Pilih Menu Belanja")
    print(f"1. {Menu1}  Rp {hargaMenu1} ")
    print(f"2. {Menu2}  Rp {hargaMenu2}")
    print(f"3. {Menu3}  Rp {hargaMenu3}")
    inBelanja = input("Pilih menu nomor: ")
    if inBelanja == "1":
             kuantitas = int(input("Masukan jumlah kuantitas yang akan dibeli: "))
             print(f"\nTerima Kasih \nJumlah biaya yang harus dibayar kan untuk {kuantitas} {Menu1}: Rp {str(kuantitas*hargaMenu1)},-")
    elif inBelanja == "2":
             kuantitas = int(input("Masukan jumlah kuantitas yang akan dibeli: "))
             print(f"\nTerima Kasih \nJumlah biaya yang harus dibayar kan untuk {kuantitas} {Menu2}: Rp {str(kuantitas*hargaMenu2)},- ")
    elif inBelanja == "3":
             kuantitas = int(input("Masukan jumlah kuantitas yang akan dibeli: "))
             print(f"\nTerima Kasih \nJumlah biaya yang harus dibayar kan untuk {kuantitas} {Menu3}: Rp {str(kuantitas*hargaMenu3)},- ")
    elif inBelanja.isdigit == False or inBelanja != 1 or inBelanja != 2 or inBelanja != 3:
             print("Input yang anda masukan salah")
if inMenu == "2" :
    print("Pilih Menu Belajar")
    print(f"1. {belajar1} ")
    print(f"2. {belajar2} ")
    
    inBelajar = input("Pilih menu nomor: ")
    if inBelajar == "1":
        inTinggiSegitiga = float(input("Masukan Tinggi Segitiga : "))
        inAlasSegitiga = float(input("Masukan Alas Segitiga : "))
        rumus1 *= inAlasSegitiga*inTinggiSegitiga
        print(f"Hasil Perhitungan: {str(round(rumus1,2))}")
    elif inBelajar == "2":
        inSisi1Trapesium = float(input("Masukan Panjang Sisi 1 Trapesium : "))
        inSisi2Trapesium = float(input("Masukan Panjang Sisi 2 Trapesium : "))
        inTinggiTrapesium = float(input("Masukan Tinggi Trapesium :"))
        rumus2 *= ((inSisi1Trapesium+inSisi2Trapesium)*inTinggiTrapesium)
        print(f"Hasil Perhitungan: {str(round(rumus2,2))}")
    elif inBelajar.isdigit == False or inBelajar != 1 or inBelajar != 2 :
             print("Input yang anda masukan salah")
if inMenu == "3" :
    print("Terimakasih")
