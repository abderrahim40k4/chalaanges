class Cipher:
    def __init__(self, alphabet='abcdefghijklmnopqrstuvwxyz', key=1):
        self.alphabet = alphabet
        self.key = key

    def encrypt_caesar(self, message):
        encrypted_message = ''
        for char in message:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                next_index = (index + self.key) % len(self.alphabet)
                encrypted_message += self.alphabet[next_index]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_caesar(self, encrypted_message):
        decrypted_message = ''
        for char in encrypted_message:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                prev_index = (index - self.key) % len(self.alphabet)
                decrypted_message += self.alphabet[prev_index]
            else:
                decrypted_message += char
        return decrypted_message

    def encrypt_vigenere(self, message):
        encrypted_message = ''
        key_length = len(self.key)
        for i, char in enumerate(message):
            if char in self.alphabet:
                index = self.alphabet.index(char)
                shift = self.key[i % key_length]
                next_index = (index + shift) % len(self.alphabet)
                encrypted_message += self.alphabet[next_index]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_vigenere(self, encrypted_message):
        decrypted_message = ''
        key_length = len(self.key)
        for i, char in enumerate(encrypted_message):
            if char in self.alphabet:
                index = self.alphabet.index(char)
                shift = self.key[i % key_length]
                prev_index = (index - shift) % len(self.alphabet)
                decrypted_message += self.alphabet[prev_index]
            else:
                decrypted_message += char
        return decrypted_message

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
