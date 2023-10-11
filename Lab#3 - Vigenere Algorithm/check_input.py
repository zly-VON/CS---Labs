def text_is_valid(text):
    return all(char.isalpha() or char.isspace() for char in text)

def key_is_valid(key):
    return len(key) >= 7 and all(char.isalpha() for char in key)

def input_data():
    while True:
        text = input("Enter the text: ")
        if text_is_valid(text):
            break
        else:
            print("Invalid characters in the text. Please enter only letters.")

    while True:
        key = input("Enter the key value (minimum 7 letters): ")
        if key_is_valid(key):
            break
        else:
            print("Key value too short or invalid character. Please enter minimum 7 letters.")
    
    return text, key
