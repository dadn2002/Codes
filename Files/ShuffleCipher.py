import sys
import itertools
import random
import codecs
from random import seed
from io import StringIO
from random import randint
from datetime import datetime
from FrequencySymbolsTable import FreqSymEng
from FrequencySymbolsTable import EngList
from FrequencySymbolsTable import Letters
from nltk.corpus import words

Eng = FreqSymEng
dt = datetime.now()
ts = datetime.timestamp(dt)
word_list = words.words()


def search(xlist, platform):
    for i1 in range(len(xlist)):
        if xlist[i1] == platform:
            return i1
    return -1


print("You want Encrypt[e] or Decrypt[d] your message?")
x = input()
x = x.lower()

if x == 'e':
    print("What kind of Encryption Rule you want?")
    print("[1] Random Permutation |k|=26!")
    print("[2] Caesar Shift |k|=26")
    x1 = input()
    ascii_values = []
    textplain = str
    if x1 == '1':
        temp = str(input("Want to Encrypt a File[y]/[n]?"))
        if temp == 'y':
            temp1 = str(input("What's the .txt file name?"))
            with open(temp1 + ".txt", "r", encoding='utf-8') as f:
                textplain = str(f.read().replace('\n', '')).lower()
        else:
            textplain = str(input("Insert your text (Only Letters): ")).lower()
        # print("test", ord(textplain)) # important debug
        for character in textplain:
            ascii_values.append(ord(character))
        while search(ascii_values, 32) != -1:  # #
            del (ascii_values[search(ascii_values, 32)])
        while search(ascii_values, 33) != -1:  # ! #
            del (ascii_values[search(ascii_values, 33)])
        while search(ascii_values, 39) != -1:  # ' #
            del (ascii_values[search(ascii_values, 39)])
        while search(ascii_values, 44) != -1:  # , #
            del (ascii_values[search(ascii_values, 44)])
        while search(ascii_values, 46) != -1:  # . #
            del (ascii_values[search(ascii_values, 46)])
        while search(ascii_values, 58) != -1:  # : #
            del (ascii_values[search(ascii_values, 58)])
        while search(ascii_values, 231) != -1:  # ç #
            ascii_values[search(ascii_values, 231)] = 99
        while search(ascii_values, 233) != -1:  # é #
            ascii_values[search(ascii_values, 233)] = 101
        while search(ascii_values, 227) != -1:  # ã #
            ascii_values[search(ascii_values, 227)] = 97
        while search(ascii_values, 226) != -1:  # â #
            ascii_values[search(ascii_values, 226)] = 97
        while search(ascii_values, 244) != -1:  # ô #
            ascii_values[search(ascii_values, 244)] = 111
        # print(ascii_values)
        for i in range(len(ascii_values)):
            ascii_values[i] = ascii_values[i] - 96
        # print(ascii_values)
        key = repr(ts)[-1] + repr(ts)[-2]
        while repr(ts)[-1] + repr(ts)[-2] == '00':
            key = repr(ts)[-1] + repr(ts)[-2]
        seed(int(key))
        Base = list(range(1, 27))
        Encp = random.sample(Base, len(Base))
        #  print(Encp)
        textcyphe = ""
        textcyphe = StringIO()
        for i in range(len(list(ascii_values))):
            #  print(Encp[int(ascii_values[i])-1], ",", chr(Encp[int(ascii_values[i])-1]+96))
            textcyphe.write(str(chr(Encp[int(ascii_values[i]) - 1] + 96)))
        # ascii_values[i] = (ascii_values[i]*int(key)) % 97
        temp2 = str(input("Want to save in a .txt file?[y]/[n]")).lower()
        if temp2 == 'y':
            temp3 = str(input("What's the .txt file name?"))
            with open(temp3 + ".txt", "w", encoding='utf-8') as f1:
                f1.write(textcyphe.getvalue())
                print("SAVE YOUR KEY: ", key)
            sys.exit("Complete")
        print("key:", key, "Text:", textcyphe.getvalue())
    if x1 == '2':
        temp = str(input("Want to Encrypt a File[y]/[n]?"))
        if temp == 'y':
            temp1 = str(input("What's the .txt file name?"))
            with open(temp1 + ".txt", "r", encoding='utf-8') as f:
                textplain = str(f.read().replace('\n', '')).lower()
        else:
            textplain = str(input("Insert your text (Only Letters): ")).lower()
        # print("test", ord(textplain)) # important debug
        for character in textplain:
            ascii_values.append(ord(character))
        while search(ascii_values, 32) != -1:  # #
            del (ascii_values[search(ascii_values, 32)])
        while search(ascii_values, 33) != -1:  # ! #
            del (ascii_values[search(ascii_values, 33)])
        while search(ascii_values, 39) != -1:  # ' #
            del (ascii_values[search(ascii_values, 39)])
        while search(ascii_values, 44) != -1:  # , #
            del (ascii_values[search(ascii_values, 44)])
        while search(ascii_values, 46) != -1:  # . #
            del (ascii_values[search(ascii_values, 46)])
        while search(ascii_values, 58) != -1:  # : #
            del (ascii_values[search(ascii_values, 58)])
        while search(ascii_values, 231) != -1:  # ç #
            ascii_values[search(ascii_values, 231)] = 99
        while search(ascii_values, 233) != -1:  # é #
            ascii_values[search(ascii_values, 233)] = 101
        while search(ascii_values, 227) != -1:  # ã #
            ascii_values[search(ascii_values, 227)] = 97
        while search(ascii_values, 226) != -1:  # â #
            ascii_values[search(ascii_values, 226)] = 97
        while search(ascii_values, 244) != -1:  # ô #
            ascii_values[search(ascii_values, 244)] = 111
        # print(ascii_values)
        for i in range(len(ascii_values)):
            ascii_values[i] = ascii_values[i] - 96
        # print(ascii_values)
        key = repr(ts)[-1] + repr(ts)[-2]
        while repr(ts)[-1] + repr(ts)[-2] == '00':
            key = repr(ts)[-1] + repr(ts)[-2]
        seed(int(key))
        Base = list(range(1, 27))
        Encp = list(range(1, 27))
        for i in range(26):
            while Base[i] + int(key) > 26:
                Base[i] = Base[i] - 26
            Encp[i] = Base[i] + int(key)
        #  print(Encp)
        textcyphe = ""
        textcyphe = StringIO()
        for i in range(len(list(ascii_values))):
            #  print(Encp[int(ascii_values[i])-1], ",", chr(Encp[int(ascii_values[i])-1]+96))
            textcyphe.write(str(chr(Encp[int(ascii_values[i]) - 1] + 96)))
        # ascii_values[i] = (ascii_values[i]*int(key)) % 97
        temp2 = str(input("Want to save in a .txt file?[y]/[n]")).lower()
        if temp2 == 'y':
            temp3 = str(input("What's the .txt file name?"))
            with open(temp3 + ".txt", "w", encoding='utf-8') as f1:
                f1.write(textcyphe.getvalue())
                print("SAVE YOUR KEY: ", key)
            sys.exit("Complete")
        print("key:", key, "Text:", textcyphe.getvalue())
    if x1 != '1' and x1 != '2':
        print("Not Available Rule")
if x == 'd':
    print("What type of Encryption is used?")
    print("[1] Random Permutation |k|=26!")
    print("[2] Caesar Cipher |k|=26")
    x1 = input()
    x4 = str
    if x1 == '1':
        temp = str(input("Want to Decrypt a file?[y]/[n]"))
        tempv = False
        if temp == 'y':
            temp1 = str(input("What's the name of the file?"))
            with open(temp1 + ".txt", "r", encoding='utf-8') as f1:
                x4 = str(f1.read().replace('\n', '')).lower()
                tempv = True
        x2 = input("Do you know the key? [y]/[n] ").lower()
        if x2 == 'y':
            x3 = input("What's the key?")  # Clearly i suppose the user is typing numerical but whatever
            if not tempv:
                x4 = str(input("What's the text?"))
            seed(int(x3))
            textplain = ""
            textplain = StringIO()
            ascii_values = []
            Base = list(range(1, 27))
            Encp = random.sample(Base, len(Base))
            for character in x4:
                ascii_values.append(ord(character))
            for i in range(len(x4)):
                ascii_values[i] = ascii_values[i] - 96
                textplain.write(chr(int(search(Encp, ascii_values[i]) + 97)))
            temp3 = str(input("Want to save the Decrypted Text in a file?[y]/[n]")).lower()
            if temp3 == 'y':
                temp4 = str(input("What's the .txt file name?"))
                with open(temp4 + ".txt", "w", encoding='utf-8') as f1:
                    f1.write(textplain.getvalue())
                    print("SAVE YOUR KEY: ", x3)

            else:
                print("key:", x3, "Text:", textplain.getvalue())
        if x2 == 'n':
            print("I actually give up for now trying to break that, it's too abstract for me")
            """
            if not tempv:
                x4 = str(input("What's the text?"))
            temp3 = str(input("Want to save the Decrypted Text in a file?[y]/[n]")).lower()
            if temp3 == 'y':
                temp4 = str(input("What's the .txt file name?"))
            textplain = ""
            textplain = StringIO()
            chrnumber = []
            chrcharac = []
            with open(temp4 + ".txt", "a", encoding='utf-8') as f1:
                f1.write("Letters Counter Table\n")
            for i in range(0, 26):
                temp5n = x4.count(chr(97 + i))
                chrnumber.append(temp5n)  # Lowest to The Highest Value
                chrcharac.append(temp5n)  # Original List i don't know if it'll be useful
                chrnumber.sort()
                if temp3 == 'y':
                    with open(temp4 + ".txt", "a", encoding='utf-8') as f1:
                        f1.write(chr(97 + i))
                        f1.write(": ")
                        f1.write(str(x4.count(chr(97 + i))))
                        f1.write(" ")
                        if (i + 1) % 7 == 0:
                            f1.write('\n')
                else:
                    print("Clearly you don't like your screen, insert the feedback in a .txt thx")
            with open(temp4 + ".txt", "a", encoding='utf-8') as f1:
                f1.write("\nFirst Sub [")
                f1.write("e")
                f1.write("]\n")
            xaux = []
            for character in x4:
                xaux.append(ord(character))
            for j in range(0, 26):
                for k in range(0, 26):
                    for i in range(len(xaux)):
                        print(chrnumber[25-k])
                        print(xaux.count(chr(97 + i)))
                        if chrnumber[25-k] == xaux.count(chr(97 + i)):
                            xaux[i] = EngList[j]
                            with open(temp4 + ".txt", "a", encoding='utf-8') as f1:
                                f1.write(xaux[i])
                                f1.write(" ")
            """
            # ascii_values = []
            # countertext = []
            # Base = list(range(1, 27))
            # Encp = random.sample(Base, len(Base))
            # for character in x4:
            #    ascii_values.append(ord(character))
            # for i in range(len(x4)):
            #    ascii_values[i] = ascii_values[i] - 96
            #    textplain.write(chr(int(search(Encp, ascii_values[i]) + 97)))
            # if temp3 == 'y':
            #    with open(temp4 + ".txt", "w", encoding='utf-8') as f1:
            #        f1.write(textplain.getvalue())
            # else:
            #     print("key:", "Text:", textplain.getvalue())
        if x2 != 'y' and x2 != 'n':
            print("a")
    if x1 == '2':
        temp = str(input("Want to Decrypt a file?[y]/[n]"))
        tempv = False
        if temp == 'y':
            temp1 = str(input("What's the name of the file?"))
            with open(temp1 + ".txt", "r", encoding='utf-8') as f1:
                x4 = str(f1.read().replace('\n', '')).lower()
                tempv = True
        x2 = input("Do you know the key? [y]/[n] ").lower()
        if x2 == 'y':
            x3 = input("What's the key?")  # Clearly i suppose the user is typing numerical but whatever
            if not tempv:
                x4 = str(input("What's the text?"))
            seed(int(x3))
            textplain = ""
            textplain = StringIO()
            ascii_values = []

            for character in x4:
                ascii_values.append(ord(character))
            for i in range(len(x4)):
                while ascii_values[i] - int(x3) < 97:
                    ascii_values[i] = ascii_values[i] + 26
                ascii_values[i] = ascii_values[i] - int(x3) - 96
                textplain.write(chr(ascii_values[i] + 96))
            temp3 = str(input("Want to save the Decrypted Text in a file?[y]/[n]")).lower()
            if temp3 == 'y':
                temp4 = str(input("What's the .txt file name?"))
                with open(temp4 + ".txt", "w", encoding='utf-8') as f1:
                    f1.write(textplain.getvalue())
                    print("SAVE YOUR KEY: ", x3)

            else:
                print("key:", x3, "Text:", textplain.getvalue())
        if x2 == 'n':
            if not tempv:
                x4 = str(input("What's the text?"))
            temp3 = str(input("Want to save the Decrypted Text in a file?[y]/[n]")).lower()
            if temp3 == 'y':
                temp4 = str(input("What's the .txt file name?"))
            print("Starting")
            for x3 in range(1, 27):
                seed(int(x3))
                textplain = ""
                textplain = StringIO()
                ascii_values = []
                for character in x4:
                    ascii_values.append(ord(character))
                counter = False
                if temp3 == 'y':
                    with open(temp4 + ".txt", "a", encoding='utf-8') as f1:
                        f1.write("\n")
                for i in range(len(x4)):
                    while ascii_values[i] - int(x3) < 97:
                        ascii_values[i] = ascii_values[i] + 26
                    ascii_values[i] = ascii_values[i] - int(x3) - 96
                    textplain.write(chr(ascii_values[i] + 96))
                if temp3 == 'n':
                    print("key:", x3, "Text:", textplain.getvalue())
                if temp3 == 'y':
                    with open(temp4 + ".txt", "a", encoding='utf-8') as f1:
                        if not counter:
                            f1.write("Key: [")
                            f1.write(str(x3))
                            f1.write("] Decrypt: ")
                            counter = True
                if temp3 == 'y':
                    with open(temp4 + ".txt", "a", encoding='utf-8') as f1:
                        f1.write(textplain.getvalue())
        if x2 != 'y' and x2 != 'n':
            print("a")
    if x1 != '1' and x1 != '2':
        print("Not Available Rule")
if x != 'e' and x != 'd':
    print("Not Available Choose")

sys.exit("Complete")
