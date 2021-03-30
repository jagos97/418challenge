
from itertools import product
from string import ascii_uppercase
import random
import string



ctxt = "HRXJREWTHM"
ctxt2 ="KEEZYNKGHHV"
ctxt3 = "HRXJREWTHMRLYOHXSLWTHWRFKIGCZALHXYREDYFIIAANZBFHJSHZJRHTXGSRJFBZKRWNGUJNKTACIGWEGSVNJMBMJVGNXRGYGRBHXFSTNLENFDBNJZGOGMNVDLVIDRLOTHVAVALNYRKPTWVPJAYNURDIUYINLEESUVNELCEGGSTNLEFSTNDBKPAYIRSNWJCHFGXMZGKEEZZALOMBVCDAGYKRNEGNYRFCTMJVFIPCCYLRTHJZATGYNQSTTUSBMTMBVCDAGYKFUOFJFFATBIENKLHHXNKIMMRALEGHREWMTCEFHOBHKRVTHQREVETLKUOIMBKUWALMZFLFKIDFEAEFKUJULNVEKNHMGNUEVLRSLHTMVIWRUYVAKOVFFFWTHMRGMRGSFHUAGNYVFKHZTNKSBHZNKTAYWVJSMMRGMRGJIBTELUZQDIGXRFHIEEVEUALMZAAPKIARUTLWZRFTBMKGZEBIENFDGYLGJAEGRFKSIYTGJOFYKRJWBFCNUTTMKUWNHMVBXTAYJCSCXWINXTWCIRUTESJNEPECETLHXWFZHOLCKVGNTHUFLRNWKHJEHZKUWAMGFFHHXLVFGMXNYVFGMBRGUAGNSRVOGYWEGMHLSVLSTCUUMNMYIJSIMYKRSMEYRQXOKNYRKPXWKEGMXNVEATPCCYSLLIZANELNZTSTXNYRJIGAINANIBVAGMXHFAVILWFIWRXXSLFALUJIGYTAVEEILMZBFIGNYRWAKFPAANXNVRFEBAYGAELQYRJEBNRCHETLVQLHTNKUWRBHXFOEKYINANBHXQGWGGRGWRBUCBFTAYGYSNXNRAVCTOJVFGVBRAYELCEGZETNDBKPAYIRLHXMGRUTKIDRLEKQZYDAMNVZHTMIZANELNZTSTXQYNLMTNVEAAECJSJOFNYRJIGAJNFDPBRGEAMYIVSLBMGNJTHZKUWAMGFFHHXLVOMTVIEGSCMQZYDQNCTXDYUYCBKTHHTRLHXMGNUEVLRSLEGNVEKSTNLEFSTNDBKPAYIRSTTBZTZSIYVQSBHOKGOOFCEHLELFRGWRVUJFANBQZYDBNLENFDWCJVFTXAINLEVIDCDEMYCLSNRNINUELIWVLWBFCZWLMXLRLOMBVUWAMUEQZIZBGEWSLOIRGFMBVTAAGNGYSNXNJUGSMCCRSTFIJCZEKYKUASPCCYDIDYCLZAIJVASRHOEQKIQNYVJTRUDRSSMYIALIFYWBJTAYJCSCXWINXTUOKTAVXHKUWTBGVVLTTEVFXOKNYRKIZHRYLOKYRPZETLKUOEPCCYJEVYZIWTAIJRDALNSVLSHZUNLACOJGTEYIIRWIZBKNELHHXNXTXLTNKSBHZVKGHHVGZELJRPWCKUWGKFBHRYKIZHRYOIEFSRDIDYRAWCAIJNADXUIYEABTVPSSLCEVHRHDVPLMTHRTWRBNNVDLKUUVSTXUTEGSLNYRKOEUIFQSMYDSGRGYREDYTHYBMRTHUNZAEZRSLEKWRFKIGCZGKEEZYNKGHHV"


##where we store the words and they possible word keys
allWords = []
wordKeys = []


##reads in all the words in the word file and adds them to all words and if it is of length 6 added to possible keys
file = open("words.txt", 'r')
line = file.readline().strip()
while True:
    if(len(line)== 6):
        wordKeys.append(line.upper())
    allWords.append(line.lower())
    line = file.readline().strip()
    if not line:
        break
file.close()

##shift the leters by the other letter
def shift(s, n):
    if(ord(s) - n < 65):
        return chr(ord(s) - n +26 )
    else:
        return chr(ord(s) -n)
            
##decrypt the given string with the key. Assumes str is at most as big as key
def decrypt(str, key):
    answer = ""
    for i in range(len(str)):
        answer = answer + shift(str[i], ord(key[i])- 65)
    return answer

##decrypts the entire ciphertext
def decryptAll(ctxt,key):
    m =""
    for i in range(0,len(ctxt), len(key)):
        m = m + decrypt(ctxt[i: i+ len(key)], key) 
    return m 

##checks if it contains a word. If the word found is only 2 letters long and length of string is at least 8 it will recurse to find another one after that word or see if it is part of another longer word
def containsWord(str):
    start = 0
    for i in range(2,len(str)):
        if(str[start:i] in allWords):
            if(i == 2 and len(str) >= 8):
                if(containsWord(str[2:])):
                    return True
                else:
                    continue
            return True
    if(str[0] == 'a' or str[0] == 'i'):
        start = 1
    
    for i in range(2,len(str)):
        if(str[start:i] in allWords):
            if(i == 2 and len(str) >= 8):
                if(containsWord(str[2:])):
                    return True
                else:
                    continue
            return True

    return False


##checks if the back contains a word longer than 1 charater
def containsWordback(str):
    for i in range(2, len(str) + 1):
        if(str[-i:] in allWords):
            return True
    return False

##tries all possible letter combo to see if a word is in there
def anyWord(str):
    length = len(str)
    for i in range(length-1):
        for j in range(length-1-i):
            if(str[i:-j] in allWords):
                return True
    return False


#checks if there are no q's without a u and contains a word
def possibleDecryption(str):
    length = len(str)
    for i in range(length):
        if(str[i] == 'q'):
            if(i < length - 1):
                if(str[i+1] != 'u'):
                    return False
    if not containsWord(str):
        return False
    
    return True

#checks if there are no q's without a u and contains a word at the back
def backPossibleDecryption(str):
    length = len(str)
    for i in range(length):
        if(str[i] == 'q'):
            if(i < length - 1):
                if(str[i+1] != 'u'):
                    return False
    if not containsWordback(str):
        return False
    
    return True

#checks that no q's are without a u
def easyCheck(str):
    length = len(str)
    for i in range(length):
        if(str[i] == 'q'):
            if(i < length - 1):
                if(str[i+1] != 'u'):
                    return False
    return True
    
#converts list
def convert(s):
    new = ""
    for x in s:
        new += x 
    return new

        
f = open("awesomekeys.txt", "w")

index = 0
for key in wordKeys:
    index += 1
    if(index % 5000 == 0):
        print("{}".format(key))
    check = decryptAll(ctxt, key).lower()
    if possibleDecryption(check):
        check2 = decryptAll(ctxt2, key).lower()
        if backPossibleDecryption(check2):
            check3 = decryptAll(ctxt3, key).lower()
            if easyCheck(check3):
                f.write("{} led to {} and {} and {} and no q's without a u\n".format(key,check,check2,check3))

f.close()