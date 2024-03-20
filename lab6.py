# Christopher Horhota

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


# Ben Davidson - added decode function
def decode(encoded):
    temp_list = [int(i) for i in encoded]

    for index in range(len(temp_list)):
        if temp_list[index] == 2:
            temp_list[index] = 9
        elif temp_list[index] == 1:
            temp_list[index] = 8
        elif temp_list[index] == 0:
            temp_list[index] = 7
        else:
            temp_list[index] -= 3

    temp_list = [str(i) for i in temp_list]
    decoded_password = ''.join(temp_list)

    return decoded_password


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
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_opt == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif menu_opt == 3:
            break
        else:
            print("Incorrect choice, please try again.\n")


if __name__ == "__main__":
    main()
