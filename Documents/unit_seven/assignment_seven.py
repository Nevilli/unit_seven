def choose():
    choice1 = input("Type e to encode, type d to decode, or type q to quit")
    if choice1 == "e":
        print("encode")
    elif choice1 == "d":
        print("decode")
    else:
        print("Goodbye")


def string():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
