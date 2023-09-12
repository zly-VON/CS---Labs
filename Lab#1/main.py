### Caesar Cipher ###

from caesar_cipher import encryption, decryption, generate_new_alphabet

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def text_is_valid(text):
    return all(char.isalpha() or char.isspace() for char in text)

def key_is_valid(key):
    return 1 <= key <= 25

def key2_is_valid(key):
    return len(key) >= 7 and all(char.isalpha() for char in key)

def input_data():
    while True:
        text = input("Enter the text: ")
        if text_is_valid(text):
            break
        else:
            print("Invalid characters in the text. Please enter only letters.")

    while True:
        key = int(input("Enter the key value (1-25): "))
        if key_is_valid(key):
            break
        else:
            print("Invalid key value. Please enter a value between 1 and 25.")
    
    return text, key

def start_menu():
    choice = input("Enter e for encryption or d for decryption: ")
    
    if choice == "e":
        choice_key = input("Enter 1 for the classic Caesar Cipher or 2 for the two-key method: ")
        if choice_key == "1":
            text, key = input_data()
            print("Encrypted text: ", encryption(text, key, alphabet))
        elif choice_key == "2":
            text, key = input_data()
            while True:
                key2 = input("Enter the 2-key value (minimum 7 letters): ")
                if key2_is_valid(key2):
                    break
                else:
                    print("Invalid key value. Please enter at least 7 alphabet letters.")
            new_alphabet = generate_new_alphabet(key2, alphabet)
            print("Encrypted text: ", encryption(text, key, new_alphabet))
                
    elif choice == "d":
        choice_key = input("Enter 1 for the classic Caesar Cipher or 2 for the two-key method: ")
        if choice_key == "1":
            text, key = input_data()
            print("Decrypted text: ", decryption(text, key, alphabet))
        elif choice_key == "2":
            text, key = input_data()
            while True:
                key2 = input("Enter the 2-key value (minimum 7 letters): ")
                if key2_is_valid(key2):
                    break
                else:
                    print("Invalid key value. Please enter at least 7 alphabet letters.")
            new_alphabet = generate_new_alphabet(key2, alphabet)
            print("Decrypted text: ", decryption(text, key, new_alphabet))

start_menu()