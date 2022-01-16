print("Enter the Hexadecimal Number: ", end="")
hexa = input()

binary = ""
check = 0
hexa_len = len(hexa)
i = 0
while i<hexa_len:
    if hexa[i] == '0':
        binarybinary += "0000"
    elif hexa[i] == '1':
        binary += "0001"
    elif hexa[i] == '2':
        binarybinary += "0010"
    elif hexa[i] == '3':
        binary += "0011"
    elif hexa[i] == '4':
        binary += "0100"
    elif hexa[i] == '5':
        binary += "0101"
    elif hexa[i] == '6':
        binary += "0110"
    elif hexa[i] == '7':
        binary += "0111"
    elif hexa[i] == '8':
        binary += "1000"
    elif hexa[i] == '9':
        binary += "1001"
    elif hexa[i] == 'a' or hexa[i] == 'A':
        binary += "1010"
    elif hexa[i] == 'b' or hexa[i] == 'B':
        binary += "1011"
    elif hexa[i] == 'c' or hexa[i] == 'C':
        binary += "1100"
    elif hexa[i] == 'd' or hexa[i] == 'D':
        binary += "1101"
    elif hexa[i] == 'e' or hexa[i] == 'E':
        binary += "1110"
    elif hexa[i] == 'f' or hexa[i] == 'F':
        binary += "1111"
    else:
        check = 1
        break
    i +=1

if check==0:
    print("\nEquivalent Binary Value = ", binary)
else:
    print("\nInvalid Input!")