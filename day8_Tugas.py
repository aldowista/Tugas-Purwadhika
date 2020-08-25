# Tugas 6 - Aldo Wista Fadhilah

# Variabel
keyDictionary = ["Key1", "Key2"]
valueDictionary = ["Value1", "Value2"]

dicData = {
    keyDictionary[0]: valueDictionary[0],
    keyDictionary[1]: valueDictionary[1]   
    }

jumlahDictionary = 2



# Function
# Show Dictionary
def show_dictionary():
    out = " |   Key   |   Value   |\n\n" 
    for i in range(len(dicData)):
        out += str((i+1)) + ")   " + str(keyDictionary[i]) + "   |   " + str(valueDictionary[i]) +"   |\n"
    return(out)

# Add Dictionary
def add_dictionary(jmlh):
    for i in range (int(jmlh)):
        dicData[keyDictionary[int(jumlahDictionary)-int(jmlh)+int(i)]] = valueDictionary[int(jumlahDictionary)-int(jmlh)+int(i)]
    print("\n--- Data berhasil diinput. ---")
    return(show_dictionary())

# Search Dictionary
def search_dictionary(kata):
    out = ''
    for i in range(len(dicData)):
        if kata == str(keyDictionary[i]):
            out += str(i+1) + ')  ' + str(keyDictionary[i]) + '   |   ' + str(valueDictionary[i])
        elif kata == str(valueDictionary[i]):
            out += str(i+1) + ')  ' + str(keyDictionary[i]) + '   |   ' + str(valueDictionary[i])
    return(out)
            


# Program Utama
checkIn = False
while checkIn == False:
    inMenu = input("\nPilih Menu \n\n1) Menu Dictionary \n2) Add Dictionary \n3) Search Dictionary \n4) Exit \n\nMasukan input (1-4) : ")
    if inMenu.isdigit()==True and 1 <= int(inMenu) <= 4:
        checkIn = True
    else:
        print("Input Salah (1-4)\n\n")

# Menu 1
    if inMenu == '1':
        print(show_dictionary())
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
        print("\n\n--- Daftar Dictionary ---\n")
        print(show_dictionary())
        checkInMenu2 = False
        while checkInMenu2 == False:
            inMenu2_Jmlh = input("\nBerapa kali masukan dictionary : ")
            if inMenu2_Jmlh.isdigit() == True :
                checkInMenu2 = True
                checkIn = False
            else:
                print("\n--- Input salah, silahkan Input data kembali! ---")
        for i in range(int(inMenu2_Jmlh)):
            inMenu2_Type = input(f"Pilih tipe dictionary ke - {i+1}: \n  1) String \n  2) Number\nPilih : ")
            if inMenu2_Type == "1" :
                inMenu2_Key = input("Key: ")
                inMenu2_Value = input("Value: ")
                keyDictionary.append(str(inMenu2_Key))
                valueDictionary.append(str(inMenu2_Value))
            elif inMenu2_Type == "2":  
                inMenu2_Key = input("Key: ")
                inMenu2_Value = input("Value: ")
                if inMenu2_Key.isdigit() == True:
                    keyDictionary.append(int(inMenu2_Key))
                    valueDictionary.append(str(inMenu2_Value))
                else :
                    print("--- WARNING! ---\n Input Salah,\nINPUT AKAN TETAP DIPROSES DAN SECARA OTOMATIS DIRUBAH MENJADI 'STRING'!!")
                    keyDictionary.append(str(inMenu2_Key))
                    valueDictionary.append(str(inMenu2_Value))
 
        jumlahDictionary += int(inMenu2_Jmlh)
        print(add_dictionary(inMenu2_Jmlh))

        # Balik ke menu awal
        inMenu2_Back = input("Kembali ke menu awal (y/n): ").lower()
        if inMenu2_Back == 'y':
            print("\n\n")
            checkIn = False
        elif inMenu2_Back == 'n':
            print("Terima Kasih Telah Menggunakan Aplikasi Sederhana Ini.")
            checkIn = True
        else :
            print("Input Salah (y/n)")
            
   
# Menu 3
    if inMenu == '3':     
        inMenu3_Kata = input("Cari kata: ")
        print("--- Hasil Pencarian ---")
        print("   Key    |   Value   ")
        print(search_dictionary(inMenu3_Kata))
        
        inMenu3_Back = input("Kembali ke menu awal (y/n): ").lower()
        if inMenu3_Back == 'y':
            print("\n\n")
            checkIn = False
        elif inMenu3_Back == 'n':
            print("Terima Kasih Telah Menggunakan Aplikasi Sederhana Ini.")
            checkIn = True
        else :
            print("Input Salah (y/n)")

       
                      
# Menu 4
    if inMenu == '4':
        print("Terima Kasih Telah Menggunakan Aplikasi Sederhana Ini.")
        checkIn = True
