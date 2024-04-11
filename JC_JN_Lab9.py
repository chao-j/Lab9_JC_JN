def decode_password(password):
    """
    Decodes the password by subtracting three to each number.
    :param password: The encoded password.
    :return: the decoded password or an error if the password is not all numerical.
    """
    newPassword = ""
    for num in password:
        holder = int(num) - 3
        # if the password is negative adds 10 to get the shift.
        if holder < 0:
            holder += 10
        newPassword += str(holder)
    return newPassword


# Jessica Chao
def encode_password(password):
    encodepass = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encodepass
# Jess-created the encode function to start the project so that the str of numbers can be encoded
done = ""
while True:
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

# Jess-while loop started to display the menu

    choice = int(input("\nPlease enter an option: "))

# Jess-created a choice for the user to input their option

    if choice == 1:
        password = input("Please enter your password to encode: ")
        done = encode_password(password)
        print("Your password has been encoded and stored!")
    elif choice == 2:
        # Added this function call Javier Noda
        decoded = decode_password(done)
        print(f"The encoded password is {done}, and the original password is {decoded}.")
# Jess-when choice 1 is selected the function encode_password is used to encode the str

    elif choice == 3:
        break
# Jess-breaks the code when choice 3 is selected
