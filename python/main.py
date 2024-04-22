from cipher import Cipher

# Main program loop
while True:
    # Get user input
    message = input("Enter message: ")
    alph = input("Enter alphabet (default: abcdefghijklmnopqrstuvwxyz): ")
    if not alph:
        alph = 'abcdefghijklmnopqrstuvwxyz'

    method = input("Choose encryption method (Caesar/Vigenere): ").lower()
    key = int(input("Enter key: "))
    operation = input("Choose operation (encrypt/decrypt): ").lower()

    cipher = Cipher(alph, key)

    if method == 'caesar':
        if operation == 'encrypt':
            result = cipher.encrypt_caesar(message)
        elif operation == 'decrypt':
            result = cipher.decrypt_caesar(message)
        else:
            result = "Invalid operation."
    elif method == 'vigenere':
        if operation == 'encrypt':
            keyword = input("Enter keyword: ")
            cipher.set_keyword(keyword)
            result = cipher.encrypt_vigenere(message)
        elif operation == 'decrypt':
            keyword = input("Enter keyword: ")
            cipher.set_keyword(keyword)
            result = cipher.decrypt_vigenere(message)
        else:
            result = "Invalid operation."
    else:
        result = "Invalid encryption method."

    print("Result:", result)

    # Ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != 'yes':
        break
