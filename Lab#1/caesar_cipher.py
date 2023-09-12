def encryption(string, key, alpha):
    encrypted_string = ""
    string = string.upper()
    for char in string:
        if char != " ":
            e = (alpha.index(char) + key) % 26
            encrypted_string = encrypted_string + alpha[e]
    return encrypted_string
    
def decryption(string, key, alpha):
    return encryption(string, -key, alpha)

def generate_new_alphabet(key_2, alphabet):
    key_2 = key_2.upper()
    key2_letters = []
    for letter in key_2:
        if letter not in key2_letters:
            key2_letters.append(letter)
    remaining_letters = [letter for letter in alphabet if letter not in key2_letters]
    new_alphabet = ''.join(key2_letters + remaining_letters)
    return new_alphabet