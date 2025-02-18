# Ayan Singh
def encode(password): # encoding function
    encoded = "" # variable containing encoded password
    for char in password: # iterates through each character of the password string
        encoded_integer = (int(char) + 3) % 10
        encoded += str(encoded_integer)
    return encoded

def decode(password):
    decoded = "" # variable containing decoded password
    for char in password: # iterates through each character of the password string
        decoded_integer = (int(char) - 3) % 10
        decoded += str(decoded_integer)
    return decoded

def main():
    encoded = "" # variable containing encoded password

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1": # encode option
            password = input("Please enter your password to encode: ")
            if len(password) != 8: # checks if integers and 8-digit password format
                print("Invalid password input - must be 8-digits.")
            else:
                encoded = encode(password) # stores encoded password
                print("Your password has been encoded and stored!")
        elif option == "2": # decode option
            if encoded == "":
                print("No password has been encoded yet.")
            else:
                print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
            
        elif option == "3": # quits program
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()