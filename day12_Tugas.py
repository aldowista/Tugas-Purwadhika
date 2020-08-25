#Tugas 12 - Aldo Wista Fadhilah

#Soal 1 - Time Converter
def timeConverter(detik):
    jam = 0
    menit = 0
    if detik <= 359999:
        while detik >= 3600:
            detik -= 3600
            jam += 1
        while 60 <= detik <=3600:
            detik -= 60
            menit += 1

        if jam < 10 :
            if menit < 10 :
                if detik < 10 :
                    out = "0" + str(jam) + ":" + "0" + str(menit) +':'+ "0" + str(detik)
                else:
                    out = "0" + str(jam) + ":" + "0" + str(menit) +':'+ str(detik)
            else:
                if detik < 10 :
                    out = "0" + str(jam) + ":" + str(menit) +':'+ "0" + str(detik)
                else:
                    out = "0" + str(jam) + ":" + str(menit) +':'+ str(detik)
        else:
            if menit < 10 :
                if detik < 10 :
                    out =  str(jam) + ":" + "0" + str(menit) +':'+ "0" + str(detik)
                else:
                    out =  str(jam) + ":" + "0" + str(menit) +':'+ str(detik)
            else:
                if detik < 10 :
                    out =  str(jam) + ":" + str(menit) +':'+ "0" + str(detik)
                else:
                    out =  str(jam) + ":" + str(menit) +':'+ str(detik)
    else :
        out = "Invalid Input !"
    return(out)

# a = 359999
# print(timeConverter(a))


#Soal 2 - Spin Words
def spinWords(String):
    kata = String.split(' ')
    out = []
    for i in range (len(kata)):
        if len(kata[i]) >= 5:
            temp=[]
            for item in kata[i]:
                temp.append(item)
            temp2= []
            for j in range(len(kata[i])-1,-1,-1):
                temp2.append(temp[j])
            hasil = ''.join(temp2)
            out.append(hasil)
        else :
            out.append(kata[i])
    a = ' '.join(out)
    return(a)

# coba = "Hey fellow warriors"
# coba2 = 'halo halo haloo'
# print(spinWords(coba))

#Soal 3 - Move Zeros
def moveZeros(listInput):
    zero = 0
    out = []
    for i in range(len(listInput)):
        print(listInput[i])
        if str(listInput[i]) == '0':
            zero += 1
        else :
            out.append(listInput[i])

    while zero > 0:
        out.append(0)
        zero -= 1
    print(listInput)
    return(out)

# list1 = [False, 1, 0, 1, 2, 0, 1, 3, 'a']
# print(moveZeros(list1))
            