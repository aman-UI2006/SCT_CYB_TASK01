def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("===== Caesar Cipher Program =====")
    choice = input("Choose (E)ncrypt or (D)ecrypt: ").strip().upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'D':
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice! Use 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
