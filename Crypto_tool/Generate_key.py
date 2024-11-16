from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
print(f'Your key is: {key}')

if os.path.exists("Secret.key"):
    print("You already have a file by the name of 'Secret.key', do you want to overwrite it?")
    answer = input("[y/n]")
    if answer == "y":
        with open("Secret.key", "wb") as key_file:
            key_file.write(key)
        print("Secret key has been saved as 'Secret.key'")

    elif answer == "n":
        print("The key has not been saved")

    else: print("Wrong input")

else:
    with open("Secret.key", "wb") as key_file:
        key_file.write(key)
    print("Secret key has been saved as 'Secret.key'")


