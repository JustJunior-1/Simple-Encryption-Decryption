def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message: ").lower()
    text = input("Enter the message: ")
    shift = int(input("Enter the shift number: "))
    if choice == 'encrypt':
        print(f"Encrypted message: {encrypt(text, shift)}")
    elif choice == 'decrypt':
        print(f"Decrypted message: {decrypt(text, shift)}")
    else:
        print("Invalid choice.")
