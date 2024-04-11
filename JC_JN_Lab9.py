# Jessica Chao

def encode_password(password):
    encodepass = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encodepass
# Jess-created the encode function to start the project so that the str of numbers can be encoded

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

# Jess-while loop started to display the menu

    choice = input("Please enter an option: ")

# Jess-created a choice for the user to input their option

    if choice == 1:
        password = input("Please enter your password to encode: ")
        done = encode_password(password)
        print("Your password has been encoded and stored!")
# Jess-when choice 1 is selected the function encode_password is used to encode the str

    elif choice == 3:
        break
# Jess-breaks the code when choice 3 is selected
