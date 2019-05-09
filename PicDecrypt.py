import cv2
import ctypes
import sys

def bin2text(s): return "".join([chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8)])


img = cv2.imread('EncryptedBoggle.png')

height, width = img.shape[:2]

print("height: ", height)
print("width: ", width)

binary_list = []

current_byte = ""
current_bit = ""

for i in range(0, height):
    for j in range(0, width):

        if img[i][j][0] % 2 == 0:
            current_byte += "0"
        else:
            current_byte += "1"
        if len(current_byte) == 7:
            # print("byte:", current_byte)
            if current_byte == "0000001":
                break
            binary_list.append(current_byte)
            current_byte = ""
    if current_byte == "0000001":
        print("\ndecryption complete!")
        break

message = bin2text(" ".join(str(x) for x in binary_list)).replace('|', '\n')

f = open("output.txt", "w")
f.write(message)
f.close()

print("\nmessage: ", message)










