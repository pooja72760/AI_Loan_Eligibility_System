import os
from cryptography.fernet import Fernet


KEY_FILE = "encryption.key"
BLOCK_SIZE = 1024 * 1024   # 1 MB


def load_key():

    with open(KEY_FILE, "rb") as file:
        return file.read()


def secure_split_file(input_file, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    key = load_key()
    cipher = Fernet(key)

    block_number = 1
    encrypted_blocks = []

    with open(input_file, "rb") as file:

        while True:

            data = file.read(BLOCK_SIZE)

            if not data:
                break

            encrypted_data = cipher.encrypt(data)

            block_file = os.path.join(
                output_folder,
                f"encrypted_block_{block_number}.bin"
            )

            with open(block_file, "wb") as output:
                output.write(encrypted_data)

            encrypted_blocks.append(block_file)

            block_number += 1

    return encrypted_blocks
def reconstruct_file(input_folder, output_file):

    key = load_key()
    cipher = Fernet(key)

    block_files = []

    for filename in os.listdir(input_folder):

        if filename.startswith("encrypted_block_") and filename.endswith(".bin"):
            block_files.append(filename)

    # Arrange blocks in correct order
    block_files.sort(
        key=lambda x: int(
            x.replace("encrypted_block_", "").replace(".bin", "")
        )
    )

    with open(output_file, "wb") as output:

        for block_file in block_files:

            block_path = os.path.join(
                input_folder,
                block_file
            )

            with open(block_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()

            data = cipher.decrypt(encrypted_data)

            output.write(data)