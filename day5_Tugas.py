# Tugas 5 - Aldo Wista Fadhilah

## Soal 1 Duplicate string 
# checkIn = False
# while checkIn == False:
#     inputanSoal1 = str(input("Masukan string: "))
#     replaceInputanSoal1 = inputanSoal1.replace(" ","")
#     print(replaceInputanSoal1)
#     if replaceInputanSoal1.isalpha() == True :
#         checkIn = True
#     else:
#         print("Inputan salah!")
#         checkIn = False

# def duplicate_string(a):
#     itemInputan = list(a.lower())
#     totalMasukan = len(itemInputan)
#     out = ""
#     for i in range(0,totalMasukan):
#         out += itemInputan[i]*int(i+1)
#     # print(f"Output: {out}")
#     return ("Output: " + out)

# print(duplicate_string(replaceInputanSoal1))

## Soal 2 Duplicate string strip
# checkIn = False
# while checkIn == False:
#     inputanSoal1 = str(input("Masukan string: "))
#     replaceInputanSoal1 = inputanSoal1.replace(" ","")
#     print(replaceInputanSoal1)
#     if replaceInputanSoal1.isalpha() == True :
#         checkIn = True
#     else:
#         print("Inputan salah!")
#         checkIn = False

# def duplicate_string_strip(a):
#     itemInputan = list(a)
#     totalMasukan = len(itemInputan)
#     out = ""
#     for i in range(0,totalMasukan):
#         out += "-"+ itemInputan[i].capitalize() + (itemInputan[i]*int(i)).lower()
#     #  print(f"Output: {out}")
#     return ("Output" + out)

# print(duplicate_string_strip(replaceInputanSoal1))


## Soal 3 Fungsi sort ascending Belum Selesai
# checkIn = False
# while checkIn == False:
#     inputMasukan = input("Masukan deret angka: ")
#     if inputMasukan.isdigit() == True:
#         checkIn = True
#     else :
#         print("Masukan inputan dalam bentuk deret Angka")

# def sort_ascending(a):
#     variabel1 = list(a)
#     # variabel1.sort()
#     for i in range(len(variabel1)):
#         for j in range(i+1, len(variabel1)):
#             if variabel1[i] > variabel1[j]:
#                 variabel1[i], variabel1[j] = variabel1[j], variabel1[i]
#     # print(variabel1)
#     return(variabel1)

# print(sort_ascending(inputMasukan))




#Soal Segitiga Terbalik
# out = ""
# for i in range(0,10):
#     for j in range(0,21):
#         if j >= 1+i and j <= 19 - i: 
#             out += " * "   
#         else:
#             out += '   '
#     out += '\n'
# print(out)

# Soal Belah Ketupat

out= ''
for i in range(0,5):
    # if i <=5 :
        for j in range(0,13):
            if j >= 6-i and j <= 6+i:
                out += " * "
            else:
                out += "   "
        out +='\n'
    # elif i >= 5:
for k in range(0,5):
        for l in range(0,13):
            if l >= 2+k and l<= 10-k:
                out += ' * '
            else:
                out += '   '
        out += '\n'
print(out)
