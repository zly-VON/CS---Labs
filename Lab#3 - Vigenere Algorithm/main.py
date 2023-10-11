from vigenere import vigenere
from check_input import input_data


alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"


def start_menu():
    choice = input("Enter e for encryption or d for decryption: ")
    
    if choice == "e":
        text, key = input_data()
        print("Encrypted text: ", vigenere('encrypt', text, key, alphabet))
            
    elif choice == "d":
        text, key = input_data()
        print("Decrypted text: ", vigenere('decrypt' ,text, key, alphabet))

    else:
        print("No such option available")


start_menu()