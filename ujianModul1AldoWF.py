#Ujian Modul 1 - Aldo Wista Fadhilah

#Soal 1
def Hashtag(stringInput):
    inputSoal1 = stringInput.split(' ')
    listOut = []
    if len(inputSoal1) > 1:
        for item in inputSoal1:
            a = item.capitalize()
            listOut.append(a)
        out = '#'+''.join(listOut)
        if len(out) > 141:
            out = "False"
        else:
            out = '#'+''.join(listOut)
    elif len(inputSoal1) == 1 and inputSoal1[0] != "":
        a = inputSoal1[0].capitalize()
        out = '#'+ a
    else:
        out = "False"
    return(out)

#z = "Hello there how are you doing"
#z = "Hello World "
#z = "aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa aaaaaaaaaa a" #Input 141
#z= "a"
#z = ""
#print(Hashtag(z))


#Soal 2
def create_phone_number(number):
    listDigit = [0,1,2,3,4,5,6,7,8,9]
    errorCheck = 0
    out = ''
    if len(number) == 10:
        for item in number:
            if item not in listDigit:
                errorCheck += 1
            else:
                if item > 9 :
                    errorCheck += 1
                else:
                    errorCheck +=0
        if errorCheck ==0:
            out = "(" + str(number[0]) + str(number[1]) + str(number[2]) + ") " + str(number[3]) + str(number[4]) + str(number[5]) + "-" + str(number[6]) + str(number[7]) + str(number[8]) + str(number[9])
        else :
            out = "False"
    else :
        out = "Input harus 10 angka"
    return(out)

# y = [1,2,3,4,5,6,7,8,9,0] #Input Normal   
# y = [1,2,3,4,5,6,7,8,9,12] #Input Salah
# y = [1,2,3,4,5,6,7,8,9,"a"] #Input Salah
# y = [1,2,3,4,5,6,7,8,9]#Input Salah
# print(create_phone_number(y))

#Soal 3
def sort_odd_even(num):
    genap = []
    ganjil = []
    out = ''
    ganjilOut =[]
    genapOut = []
    print(len(num))
    if 1 < len(num) < 7 :
        for item in num:
            if item%2 == 0 or item == 0:
                genap.append(item)
            else :
                ganjil.append(item)
        genapOut = sorted(genap,reverse=True)
        ganjilOut = sorted(ganjil,reverse=False)
        out += str(ganjilOut[0]) +', ' + str(ganjilOut[1]) +', ' + str(genapOut[0]) +', ' + str(genapOut[1]) +', ' + str(ganjilOut[2]) +', ' + str(genapOut[2])
    elif len(num) == 1 and num[0] != "":
        out = str(num[0])
    else:
        out = "False"
    return(out)

# a = [5,3,2,8,1,4] 
# a = [15,3,22,8,1,4] 
# print(sort_odd_even(a))

#Soal 4
def hollowTriangle(height):
    kepala = ''
    bawah = ''

    # Kepala
    kepala = '_'*(height-1) + "#" + '_'*(height-1)
    print(kepala)

    # Body
    for i in range(height-2):
        print('_'*((height-2)-i)+'#'+'_'*((i*2)+1)+'#'+'_'*((height-2)-i))

    # Bawah 
    bawah = "#"*((height*2)-1)
    print(bawah)

print(hollowTriangle(1))