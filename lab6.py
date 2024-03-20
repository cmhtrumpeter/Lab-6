def encode(password):
    new = []
    for i in password:
        i = int(i) + 3
        i = str(i)
        if len(i) == 2:
            new.append(str(i[1:]))
        else:
            new.append(str(i))

    encoded = ''.join(new)
    return encoded


def decode(encoded):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        menu_opt = int(input("Please enter an option: "))
        if menu_opt == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_opt == 2:
            pass
        elif menu_opt == 3:
            pass


if __name__ == "__main__":
    main()
