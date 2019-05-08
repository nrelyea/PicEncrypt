import cv2
import ctypes
import sys


def reformat_binary(s):
    print("\ninput: ", s, "\n")

    binary_list = s.split()
    zeros = "00000000"

    for i in range(0, len(binary_list)):
        if len(binary_list[i]) < 7:
            binary_list[i] = zeros[0:(7 - len(binary_list[i]))] + binary_list[i]

    # s = " ".join(str(x) for x in binary_list)
    return binary_list

def bin2text(s): return "".join([chr(int(s[i:i+8],2)) for i in range(0,len(s),8)])

def output(s): return ctypes.windll.user32.MessageBoxW(0, s, "Error", 1)


img = cv2.imread('babbybeagle.jpg')

height, width = img.shape[:2]

print("height: ", height)
print("width: ", width)

with open('input.txt', 'r') as file:
    str_input = file.read().replace('\n', '')
print("data:", str_input)

str_binary = ' '.join(["{0:b}".format(x) for x in bytes(str_input, "ascii")])

binary_list = reformat_binary(str_binary)

# verify encoding is correct
if str_input == bin2text(" ".join(str(x) for x in binary_list)):
    print("binary conversion successful")
else:
    output("Binary Encoding Error\n" + str_input + " -> " + bin2text(" ".join(str(x) for x in binary_list)))
    sys.exit()

print("reformatted:", " ".join(str(x) for x in binary_list))

f = open("binary.txt", "w")
f.write(str_binary)
f.close()

byte = 0
bit = 0

for i in range(0, height):
    for j in range(0, width):
        print("encoding ", binary_list[byte][bit])
        if img[i][j][0] % 2 == 0 and int(binary_list[byte][bit]) == 1:
            img[i][j][0] += 1
        elif img[i][j][0] % 2 == 1 and int(binary_list[byte][bit]) == 0:
            img[i][j][0] += 1
        bit += 1
        if bit == 7:
            bit = 0
            byte += 1
        if byte > len(binary_list) - 1:
            break
    if byte > len(binary_list) - 1:
        break


cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()


