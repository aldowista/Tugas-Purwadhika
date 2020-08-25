# Tugas 9 - Aldo Wista Fadhilah

from datetime import datetime
import calendar

# Soal 1 - Function for Check Name

def check_name ():
    name = input("Masukan Nama yang akan di check: ")
    char = input("Masukan Char yang akan di check: ")
    s = 0
    out = ''
    for i in range(len(name)):
        if list(name)[i] == char:
            s+= 1
    if s > 0:
        out += "True"
    else:
        out += "Karakter tidak berada pada nama"
    return(out)

# Soal 2 - Function for Check Number Odd or Even

def evenOdd_Check():
    inputAngka = input("Masukan list angka (pisahkan angka dengan koma) : ")
    angka = list(inputAngka.split(','))
    genap = 0
    ganjil = 0
    for i in range(len(list(angka))):
        if int(angka[i]) %2 == 0:
            genap+= 1
        else :
            ganjil+=1
    out = "Jumlah angka ganjil ada " + str(ganjil) + " dan jumlah angka genap ada " + str(genap) 
    return(out)

# Soal 3 - Function for check Maximum Number

def checkMax_num ():
    inputAngka = input("Masukan List Angka: ")
    angka = list(inputAngka.split(','))
    for i in range(len(angka)-1, 0, -1):
        for j in range(0,i):
            if int(angka[j]) > int(angka[j+1]):
                angka[j], angka[j+1] = angka[j+1], angka[j]
    out = "Angka terbesar adalah " + str(angka[(len(angka)-1)]) + " dan angka terkecil adalah " + str(angka[0])
    return(out)

# Soal 4 - String Filter
def string_filter():
    inputSoal4 = input("Masukan kata yang akan di filter: ")
    inputan = list(inputSoal4)
    out = ''
    for i in range(len(inputan)):
        if inputan[i].isdigit() == True:
            out += str(inputan[i])
    hasil = "Outputnya adalah " + out
    return(hasil)

def string_filter2():
    inputSoal4 = input("Masukan kata yang akan di filter: ")
    hasil = ''.join([item for item in inputSoal4 if inputSoal4.isdigit()]) #Menggunakan List Comprehension, ''.join() merupakan atribut dari string, dimana akan menyatukan charakter pada list yang terpisah
    return(hasil) 

# Soal 5 - Function for Validation Plat Number
def plat_check():
    platNomor = input("Masukan Plat Nomor : ")
    angka = list(platNomor.split(' '))[1]
    genap = 0
    out = ""
    if int(angka) %2 == 0 :
        genap += 1
    
    # CAT : 
    # Senin, Rabu, Jumat : Hanya mobil genap yg boleh jalan
    # Selasa, Kamis, Sabtu : Hanya mobil ganjil yg boleh jalan
    # Minggu, kedua mobil boleh jalan
    now = datetime.now().weekday()
    hari = calendar.day_name[now]

    if hari == 'Sunday':
        out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " boleh lewat!"
    elif hari == 'Monday' and genap == 1:
        out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " boleh lewat!"
    elif hari == 'Tuesday' and genap == 0:
        out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " boleh lewat!"
    elif hari == 'Wednesday' and genap == 1:
        out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " boleh lewat!"
    elif hari == 'Thursday'and genap == 0:
        out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " boleh lewat!"
    elif hari == 'Friday' and genap == 1:
        out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " boleh lewat!"
    elif hari == 'Saturday'and genap == 0:
        out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " boleh lewat!"
    else :
       out += "Kendaraan anda dengan plat nomor " + str(platNomor) + " TIDAK boleh lewat!"
    
    return(out)

checkIn = False
inMenu = input("Pilih Menu : \n1) Cek Charakter dalam nama\n2) Cek jumlah angka genap dan ganjil\n3) Cek angka maksimum dan minimum\n4) Filter Text \n5) Validasi Plat Nomor : ")
if inMenu == '1':
    print(check_name())
elif inMenu == '2':
    print(evenOdd_Check())
elif inMenu == '3':
    print(checkMax_num())
elif inMenu == '4':
    print(string_filter())
elif inMenu == '5':
    print(plat_check())