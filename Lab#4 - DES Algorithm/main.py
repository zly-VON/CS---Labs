from to_binary import convert_to_binary
from random_key import create_random_key


def convert_to_kplus(key_binary):
    key_plus = ''

    global pc1
    pc1 = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]

    for value in pc1:
        key_plus += key_binary[value]

    return key_plus


def retrieve_key():
    while True:
        choice = input("Enter (e) for entering a key, or (r) to randomly generate one: ")
        if choice == "e":
            key = input("Enter your 8-symbols key: ")
            if len(key) == 8: 
                break
            else:
                print("Invalid key - 8 symbols required.\n")

        elif choice == "r":
            key = create_random_key(8)
            break

        else:
            print("No such option available\n")

    return key


def print_steps(key, key_binary, key_plus):
    print(f"\nOriginal Key: {key} Length: {len(key)}")
    print(f"Binary Key:   {key_binary} Length: {len(key_binary)}")
    print(f"K+:           {key_plus} Length: {len(key_plus)}")

    print("\nPC-1 Permutation Table:")
    for i in range(0, len(pc1), 8):
        row = pc1[i:i + 8]
        for bit in row:
            print(f"{bit:2}", end=" ")
        print()
    print()


if __name__ == "__main__":
    print("\nLab 4 - Given the key of the DES algorithm (8 symbols), determine K+.\n")
    key = retrieve_key()
    key_binary = convert_to_binary(key) 
    key_plus = convert_to_kplus(key_binary)
    print_steps(key, key_binary, key_plus)
