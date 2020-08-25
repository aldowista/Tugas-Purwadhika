# Tugas 11 - Aldo Wista Fadhilah

# Soal 1 - Function Count Word
def countWords(Input_String):
    out= ''
    jmlhKata = len(Input_String.split(" "))
    out += "Banyaknya kata dalam Input yang dimasukan adalah " + str(jmlhKata)
    return(out)

# a= "Aldo Wista Fadhilah"
# print(countWords(a))

# Soal 2 - Function menghitung bilang di list dan di bandingkan dengan parameter
def smallEnough(list_Item, parameter):
    jmlhItem = len(list_Item)
    out = ''
    if jmlhItem < parameter:
        out+= "FALSE! Jumlah item KURANG dari parameter"
    else:
        out+= "TRUE! Jumlah item LEBIH dari parameter"
    return(out)

# print(smallEnough([20,30,31,11,22,33,57],5))

# Soal 3 - Function Remove Duplicate
def removeDuplicate(text):
    inputString = text.lower().split(" ")
    a = set(inputString)
    c= ''.join(a)
    return(c)

a= 'anugrah Nurhamid anugrah nurhamid nurhamid anugrah'
print(removeDuplicate(a))

def removeDuplicate2(Text):
    inputString = Text.lower().split(' ')
    temp = []
    for item  in inputString:
        if item not in temp:
            temp.append(item)
    a= ' '.join(temp)
    return(a)
print(removeDuplicate2(a))


# Soal 4 - Function Stringly
def stringly(num):
    a = "10"
    out = a * int(num)
    return(out)

# print(stringly(1))

# Soal 5 - Function Wave Text
def wave(text):
    temp= []
    out = []
    for item in text:
        temp.append(item)

    for i in range(len(text)):
        temp[i] = temp[i].capitalize()
        out.append(''.join(temp))
        temp[i] = temp[i].lower()
    
    return(out)

# a = "anugrah"
# print(wave(a))

