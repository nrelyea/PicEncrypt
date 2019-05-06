str_binary = "010 10 110 1 100 "
print("\ninput: ", str_binary, "\n")

l = len(str_binary)
i = 0
marker = -1

while i < l:
    print("    ", i)
    if str_binary[i] == ' ':
        length = i - marker - 1
        print("length: ", length)
        if length < 3:
            print("  marker: ", marker)
            print("  ", str_binary)
            str_binary = str_binary[0:marker+1] + "M" + str_binary[marker+1:l]
            print("  ", str_binary)
            # str_binary = str_binary[0:l]



        marker = i

    i += 1

