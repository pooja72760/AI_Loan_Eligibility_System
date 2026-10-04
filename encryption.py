from cryptography.fernet import Fernet
import os


KEY_FILE = "encryption.key"


def generate_key():

    if not os.path.exists(KEY_FILE):

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)


def load_key():

    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file(input_file, output_file):

    generate_key()

    key = load_key()

    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(input_file, output_file):

    key = load_key()

    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)