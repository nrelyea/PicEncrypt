import cv2


def reformat_binary(s):
    print("\ninput: ", s, "\n")

    binary_list = s.split()
    zeros = "00000000"

    for i in range(0, len(binary_list)):
        if len(binary_list[i]) < 7:
            binary_list[i] = zeros[0:(7 - len(binary_list[i]))] + binary_list[i]

    s = " ".join(str(x) for x in binary_list)
    return s


img = cv2.imread('babbybeagle.jpg')

height, width = img.shape[:2]

print("height: ", height)
print("width: ", width)

str_input = "Hello World! ayy."

str_binary = ' '.join(["{0:b}".format(x) for x in bytes(str_input, "ascii")])
str_binary = reformat_binary(str_binary)

f = open("binary.txt", "w")
f.write(str_binary)
f.close()

print(str_binary)

n = 0

for i in range(0, height):
    for j in range(0, width):
        val = str_binary[n]
        if img[i][j][0] % 2 == 0:
            img[i][j][0] = 150


cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()


