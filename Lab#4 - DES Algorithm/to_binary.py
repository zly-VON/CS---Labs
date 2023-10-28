def convert_to_binary(string):
    string_binary = ''
    for char in string:
        string_binary += format(ord(char), '08b')

    return string_binary