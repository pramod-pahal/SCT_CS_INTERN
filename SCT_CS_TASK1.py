def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            code_point = ord(char)
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            new_char = chr((code_point - base + shift_amount) % 26 + base)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted Text: {encrypted_text}\n")

        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted Text: {decrypted_text}\n")

        elif choice == '3':
            break

        else:
            print("Invalid option, please choose again.\n")

if __name__ == "__main__":
    main()
