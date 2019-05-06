str_binary = "010 10 110 1 100 "
print("\ninput: ", str_binary, "\n")

binary_list = str_binary.split()
zeros = "0000000"

for i in range (0,len(binary_list)):
    #print(binary_list[i])
    if len(binary_list[i]) < 3:
        binary_list[i] = zeros[0:(3 - len(binary_list[i]))] + binary_list[i]
    print(binary_list[i])

str_binary = " ".join(str(x) for x in binary_list)

print("\noutput: ", str_binary)
