# Tugas 4 - Aldo Wista Fadhilah
exit = False
while exit == False:
    checkIn = False 
    while checkIn == False:
        menuUtama =  input("Pilih Menu : \n1) Segitiga Siku- Siku\n2) Segitiga Sama Kaki\n3) Persegi \n4) Keluar \nMasukan Input : ")
        if menuUtama.isdigit() == True :
            if int(menuUtama) > 0 and int(menuUtama) <= 4:
                checkIn = True
            else :
                print('Input Salah\n---------------------------------')
        else :
            print('Input Salah\n---------------------------------')
    # Proses bila menu 1 yang terpilih 
    if menuUtama == "1":
                checkInSiku = False
                while checkInSiku == False:
                        inSegitigaSiku = input("Pilih Siku :\n1) Siku Atas \n2) Siku Bawah \nMasukaan Inputan : ")
                        if inSegitigaSiku.isdigit() == True:
                                if int(inSegitigaSiku)>= 0 and int(inSegitigaSiku)<=2:
                                        checkInSiku = True
                                else:
                                        print('Input salah')
                        else:
                                print("Input Salah")
                if int(inSegitigaSiku) == 1: 
                        # Siku Atas
                        num = 6
                        for i in range(num,0,-1):
                                print('* '* i + ' '*(num-i)) 
                        exit = True                       
                if int(inSegitigaSiku)== 2:
                        # siku bawah
                        num = 6
                        for i in range(1,num+1):
                                print(' '*(num-i)+ '*'*i)
                        exit = True
    elif menuUtama == "2":
            checkInSegitigaSiku = False
            while checkInSegitigaSiku == False:
                        inSegitigaSamaKaki = input("Berapa Panjang Rows (1-10) :")
                        if inSegitigaSamaKaki.isdigit() == True:
                                checkInSegitigaSiku = True
                        else :
                                print("Input Harus Berupa Angka")
             # siku bawah
            for i in range(0,(int(inSegitigaSamaKaki)+1), 1):
                print(' '*((int(inSegitigaSamaKaki)+1)-i)+'* '*i)
            exit = True
    elif menuUtama == "3":
            checkInPersegi = False
            while checkInPersegi == False:
                inPersegi1 = input("Masukan input sisi 1 persegi : ")
                inPersegi2 = input("Masukan input sisi 2 persegi : ")
                if inPersegi1.isdigit() and inPersegi2.isdigit():
                        checkInPersegi = True
                else :
                        print("Input Salah, Masukan angka!")
            z = ''
            for item in range(0,int(inPersegi1)):
                    z += (' * ' * int(inPersegi2) + '\n')
            print(z)       
            exit = True
    elif menuUtama == "4":
            exit = True
print("--------Terimakasih.---------")