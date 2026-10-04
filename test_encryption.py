from encryption import encrypt_file, decrypt_file


# Encrypt the file
encrypt_file(
    "sample.txt",
    "encrypted_sample.bin"
)

print("File encrypted successfully.")


# Decrypt the file
decrypt_file(
    "encrypted_sample.bin",
    "decrypted_sample.txt"
)

print("File decrypted successfully.")