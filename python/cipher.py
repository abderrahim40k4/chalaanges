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
