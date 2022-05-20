import math
import sys
import subprocess
import os
import itertools
import random
import codecs
import time
import numpy as np
import Functions
from random import seed
from io import StringIO
from random import randint
from datetime import datetime

from FrequencySymbolsTable import FreqSymEng
from FrequencySymbolsTable import EngList
from FrequencySymbolsTable import Letters

# from nltk.corpus import words

Eng = FreqSymEng
dt = datetime.now()
ts = datetime.timestamp(dt)


# word_list = words.words()


def search(xlist, platform):
    for i1 in range(len(xlist)):
        if xlist[i1] == platform:
            return i1
    return -1


# subprocess.Popen("Teste.py", shell=True)
# Funciona mas aparentemente é estritamente em segundo plano.
# Work perfectly as expected
# os.startfile('Teste.py') # Agradecimentos a @Breno pelo auxílio


# print(Functions.facsmall(9788111, 1000))
# print(Functions.facdifsquare(50729878697299, 10000))
# list1.sort()
# print(list1)
os.startfile(Functions)

print("Right now this code read 223 Symbols, it's just for educational purposes")
x = input("You want Encrypt[e] or Decrypt[d] your message?")
x = x.lower()

# for i in range(33, 255):  # ASCII List
#    with open("debug4" + ".txt", "a", encoding="utf-8") as f1:
#        f1.write(chr(i))

if x == 'e':
    ascii_values = []
    textplain = str
    # for i in range(33, 256):
    #     print("[", i, "]: ", chr(i))
    temp = str(input("Want to Encrypt a File[y]/[n]?"))
    if temp == 'y':
        temp1 = str(input("What's the .txt file name?"))
        with open("Text/" + temp1 + ".txt", "r", encoding='utf-8') as f:
            textplain = str(f.read().replace('\n', ''))
    else:
        textplain = str(input("Insert your text: "))
    # print("test", ord(textplain)) # important debug
    for character in textplain:
        ascii_values.append(ord(character))
    while search(ascii_values, 32) != -1:  # #
        del (ascii_values[search(ascii_values, 32)])
    # print(ascii_values)
    for i in range(len(ascii_values)):
        ascii_values[i] = ascii_values[i] - 32
    # for i in range(0, len(ascii_values)):
    #    print(chr(int(ascii_values[i]) + 32))

    key = int(input("What's the key?"))
    #  print(Encp)
    textcyphe = ""
    textcyphe = StringIO()
    for i in range(len(list(ascii_values))):
        #  print(Encp[int(ascii_values[i])-1], ",", chr(Encp[int(ascii_values[i])-1]+96))
        textcyphe.write(chr((ascii_values[i] * key % 223) + 32))
    # ascii_values[i] = (ascii_values[i]*int(key)) % 97
    temp2 = str(input("Want to save in a .txt file?[y]/[n]")).lower()
    if temp2 == 'y':
        temp3 = str(input("What's the .txt file name?"))
        with open("Text/" + temp3 + ".txt", "w", encoding='utf-8') as f1:
            f1.write(textcyphe.getvalue())
            print("SAVE YOUR KEY: ", key)
        sys.exit("Complete")
    print("key:", key, "Text:", textcyphe.getvalue())

if x == 'd':
    temp = str(input("Want to Decrypt a file?[y]/[n]"))
    tempv = False
    if temp == 'y':
        temp1 = str(input("What's the name of the file?"))
        with open("Text/" + temp1 + ".txt", "r", encoding='utf-8') as f1:
            x4 = str(f1.read().replace('\n', ''))
            tempv = True
    x2 = input("Do you know the key? [y]/[n] ").lower()
    if x2 == 'y':
        x3 = input("What's the key?")  # Clearly i suppose the user is typing numerical but whatever
        if not tempv:
            x4 = str(input("What's the text?"))
        textplain = ""
        textplain = StringIO()
        ascii_values = []
        for character in x4:
            ascii_values.append(ord(character))
        for i in range(len(x4)):
            # print(int((congruence(int(ascii_values[i]-32), 1, int(x3), 'd', 0, 223)+32) % 223))
            # print(chr(int((congruence(int(ascii_values[i]-32), 1, int(x3), 'd', 0, 223)+32) % 223)))
            textplain.write(
                chr(int((Functions.congruence(int(ascii_values[i] - 32), 1, int(x3), 'd', 0, 223)) % 223) + 32))
        temp3 = str(input("Want to save the Decrypted Text in a file?[y]/[n]")).lower()
        if temp3 == 'y':
            temp4 = str(input("What's the .txt file name?"))
            with open("Text/" + temp4 + ".txt", "w", encoding='utf-8') as f1:
                f1.write(textplain.getvalue())
                print("SAVE YOUR KEY: ", x3)
        else:
            print("key:", x3, "Text:", textplain.getvalue())
    if x2 == 'n':
        print("I actually give up for now trying to break that, it's too abstract for me")
        if not tempv:
            x4 = str(input("What's the text?"))
        temp3 = str(input("Want to save the Decrypted Text in a file?[y]/[n]")).lower()
        if temp3 == 'y':
            temp4 = str(input("What's the .txt file name?"))
        for x3 in range(1, 223):
            textplain = ""
            textplain = StringIO()
            ascii_values = []
            for character in x4:
                ascii_values.append(ord(character))
            for i in range(100):
                # print(int((congruence(int(ascii_values[i]-32), 1, int(x3), 'd', 0, 223)+32) % 223))
                # print(chr(int((congruence(int(ascii_values[i]-32), 1, int(x3), 'd', 0, 223)+32) % 223)))
                textplain.write(
                    chr(int((Functions.congruence(int(ascii_values[i] - 32), 1, int(x3), 'd', 0, 223)) % 223) + 32))
            if temp3 == 'y':
                with open("Text/" + temp4 + ".txt", "a", encoding='utf-8') as f1:
                    f1.write("Key: [")
                    f1.write(str(x3))
                    f1.write("] PlainText: ")
                    f1.write(textplain.getvalue())
                    f1.write("\n")
            else:
                print("Key: [", x3, "] PlainText: ", textplain.getvalue(), "\n")
            time.sleep(0.1)
    if x2 != 'y' and x2 != 'n':
        print("a")
if x != 'e' and x != 'd':
    print("Not Available Choose")

sys.exit("Complete")
