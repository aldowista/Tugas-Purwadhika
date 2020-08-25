# Tugas 10 - Aldo Wista Fadhilah

import math

# Soal 1 - Remove Outlier List
def remove_outlier (list_input):
    nilaiError = 100 #Atur nilaiError untuk mengatur nilai Threshold
    b = math.floor((sum(list_input))/len(list_input))
    temp = []
    for i in range(len(list_input)):
        if -nilaiError <= (int(list_input[i]) - int(b)) <= nilaiError: 
            temp.append(list_input[i])
    return(temp)
     
# a = [60,61,62,63,64,65,70,66,64,100]
# c = [60,63,64,62,69,80,1,60,63,64,60]
# print(remove_outlier(a))
# print(remove_outlier(c))

#Remove Outlier Menggunakan IQR (Inter Quartile Range), Q3-Q1 (Cara Kedua)
def remove_outlier2(list_input2):
    list_input = sorted(list_input2)
    mid = math.floor(len(list_input)/2)
    data1 = (list_input[0:mid])
    data3 = (list_input[mid:])
    q1 = data1[len(data1)//2]/2 if len(list_input)%2 != 0 else (data1[len(data1)//2] + data1[len(data1)//2 - 1])/2
    q3 = data3[len(data3)//2]/2 if len(list_input)%2 != 0 else (data3[len(data3)//2] + data3[len(data3)//2 - 1])/2
    iqr = q3-q1
    batas_bawah = q1 - 1.5*iqr
    batas_atas = q3 + 1.5*iqr
    temp = []
    for i in range(len(list_input)):
        if batas_bawah < (int(list_input[i])) < batas_atas: 
            temp.append(list_input[i])

    print(q1)
    print(q3)
    print(data1)
    print(data3)
    return(temp)

# c = [60,63,64,62,69,80,1,60,63,64,60, 300]
# print(remove_outlier2(c))




#Soal 2 - Count Vowels in Text
def count_vowels(String):
    inputString = String.lower()
    totalVowels = 0
    for i in range(len(inputString)):
        if inputString[i] == 'a' or inputString[i] == 'i' or inputString[i] == 'u' or inputString[i] == 'e' or inputString[i] == 'o':
            totalVowels += 1
    out = "Jumlah huruf vokal nya ialah " + str(totalVowels)
    return(out)

# inputSoal2 = 'Misaki dan Tsubasa adalah legenda sepakbola Jepang'
# print(count_vowels(inputSoal2))


# Soal 3 - Sort many Element in List
def sort_list_2d (list_2d):
    a = len(list_2d)
    b = []
    for i in range(a):
        c = len(list_2d[i])
        for j in range(c):
            b.append(list_2d[i][j])
    d = sorted(b)
    return(d)

# list1 = [[3,4,2,1] , [1,2,3] , [5,4,3,1]]
# list2 = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]

# print(sort_list_2d(list1))
# print(sort_list_2d(list2))


# Soal 4 - Count Words
def countWords(String):
    print(String)
    inputString = String.lower().split(' ')
    a = set(inputString)
    c = []
    out = ''
    for i in range(len(a)):
        c.append(0)
        for j in range(len(inputString)):
            if list(a)[i] == inputString[j]:
                c[i] += 1
        out += "Jumlah kata " + str(list(a)[i] +" adalah " + str(c[i])) + "\n"
    return(out)

# string = "Kamu kamu kamu Lagi, Jangan dekati dekati aku lagi"
# print(countWords(string))