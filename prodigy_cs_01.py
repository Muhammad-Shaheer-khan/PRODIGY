def caesar_cipher(text, shift, mode):
    shift %= 26
    if mode == 'decrypt':
        shift = -shift
    trans_table = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[shift:] + 
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[:shift]
    )
    return text.translate(trans_table)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Please enter 'e' for encryption or 'd' for decryption.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (an integer between 1 and 25): "))
        if 1 <= shift <= 25:
            result = caesar_cipher(message, shift, 'encrypt' if choice == 'e' else 'decrypt')
            print("Encrypted message:" if choice == 'e' else "Decrypted message:", result)
        else:
            print("Shift value must be between 1 and 25.")

        again = input("Do you want to perform another operation? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
