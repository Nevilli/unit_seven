# Liam Neville
# 10/2/18
# This program allows the user to encode and decode a message


def choose():
    """
    This function
    :return:
    """
    choice1 = input("Type e to encode, type d to decode, or type q to quit")
    if choice1 == "e":
        return "e"
    elif choice1 == "d":
        return "d"
    else:
        print("Goodbye")


def main():
    choice = choose()
    if choice == "e":
        number = int(input("Choice a number between 0-25"))
        phrase = input("Choose a phrase to encode")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first = alphabet[0:number]
        last = alphabet[number:]
        final = last + first
        encode = ""
        for x in phrase:
            if x not in alphabet:
                encode = encode + x
            else:
                code = alphabet.index(x)
                final2 = final[code]
                encode = encode + final2
        print(encode)
    elif choice == "d":
        number = int(input("Choice a number between 0-25"))
        phrase = input("Choose a phrase to decode")
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        first = alphabet[0:number]
        last = alphabet[number:]
        final = last + first
        decode = ""
        for x in phrase:
            if x not in final:
                decode = decode + x
            else:
                code = alphabet.index(x)
                final2 = final[code]
                decode = decode + final2
        print(decode)


main()
