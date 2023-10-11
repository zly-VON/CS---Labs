def vigenere(option, string, key, alpha):
    new_string = ""
    string = string.replace(" ", "")
    string = string.upper()

    key_times = (len(string) // len(key)) + 1
    key_string = (key * key_times)[:len(string)]
    key_string = key_string.upper()

    for char, k in zip(string, key_string):
        if option == 'encrypt':
            e = (alpha.index(char) + alpha.index(k)) % len(alpha)
        elif option == 'decrypt':
            e = (alpha.index(char) - alpha.index(k)) % len(alpha)
        new_string = new_string + alpha[e]
    return new_string
