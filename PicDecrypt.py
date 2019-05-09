import cv2
import ctypes
import sys

img = cv2.imread('EncryptedBoggle.png')

height, width = img.shape[:2]

print("height: ", height)
print("width: ", width)

binary_list = []

current_byte = ""
current_bit = ""

print("origin: ", img[0][0][0])

for i in range(0, height):
    for j in range(0, width):

        # print("encoding ", binary_list[byte][bit])
        print(img[i][j][0])
        if img[i][j][0] % 2 == 0:
            current_byte += "0"
        else:
            current_byte += "1"
        if len(current_byte) == 7:
            print(current_byte)
            sys.exit()












