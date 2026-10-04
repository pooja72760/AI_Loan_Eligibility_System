from secure_cloud import secure_split_file


blocks = secure_split_file(
    "sample.txt",
    "secure_cloud_blocks"
)

print("File split and encrypted successfully.")

for block in blocks:
    print(block)