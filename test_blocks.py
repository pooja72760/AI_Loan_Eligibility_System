from cloud_storage import split_file


blocks = split_file(
    "sample.txt",
    "cloud_blocks"
)

print("File split successfully.")

for block in blocks:
    print(block)