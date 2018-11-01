def choose():
    choice1 = input("Type e to encode, type d to decode, or type q to quit")
    if choice1 == "e":
        print("encode")
    elif choice1 == "d":
        print("decode")
    else:
        print("Goodbye")


def main():
    if choose == "e":
        number = int(input("Choice a number between 0-25"))
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first = alphabet[0:number]
        last = alphabet[number:]
        final = last + first


main()
