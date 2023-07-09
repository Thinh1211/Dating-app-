import sys
import math

def encode(message):
    def toBinary(a):
        b = []
        for i in a:
            if len(bin(ord(i))[2:]) < 7:
                for j in range(7 - len(bin(ord(i))[2:])):
                    b.append(0)
            b.append(int(bin(ord(i))[2:]))
        return b

    mess = []
    mess = toBinary(message)
    str1 = ""
    for i in mess:
        str1 += str(i)
    str1 += " "
    k = 0
    str2 = ""
    while k < len(str1) - 1:
        if str1[k] == "1":
            cnt = 0
            while str1[k] == "1" and k < len(str1) - 1:
                k += 1
                cnt += 1
            str2 += "0 " + "0"*cnt + " "
        elif str1[k] == "0":
            cnt = 0
            while str1[k] == "0" and k < len(str1) - 1:
                k += 1
                cnt += 1
            str2 += "00 " + "0"*cnt + " "
    return str2[:-1]

def decode(message):
    def BinaryToDecimal(n):
        return int(n,2)

    def BinaryToDecimalExtended(message):
        i = 7
        Final_message = ""
        while i <= len(message):
            str = ""
            str += message[(i-7):i]
            Final_message += chr(BinaryToDecimal(str))
            i += 7
        return Final_message

    def UnaryToBinary(message):
        message += " "
        new_message = []
        i = 0
        while i < len(message):
            str = ""
            if message[i] == " ":
                str += message[:i]
                message = message[(i + 1):]
                i = 0
            i += 1
            if str != "":
                new_message.append(str)
        str2 = ""
        j = 0
        while j < len(new_message):
            if new_message[j] == "00":
                str2 += "0"*len(new_message[j + 1])
            if new_message[j] == "0":
                str2 += "1"*len(new_message[j + 1])
            j += 2
        return str2
    return BinaryToDecimalExtended(UnaryToBinary(message))