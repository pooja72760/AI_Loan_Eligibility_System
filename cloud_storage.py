import os


BLOCK_SIZE = 1024 * 1024   # 1 MB


def split_file(input_file, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    blocks = []

    with open(input_file, "rb") as file:

        block_number = 1

        while True:

            data = file.read(BLOCK_SIZE)

            if not data:
                break

            block_file = os.path.join(
                output_folder,
                f"block_{block_number}.bin"
            )

            with open(block_file, "wb") as output:
                output.write(data)

            blocks.append(block_file)

            block_number += 1

    return blocks


def get_cloud_files():

    files = []

    if not os.path.exists("secure_storage"):
        return files

    for application_folder in os.listdir("secure_storage"):

        folder_path = os.path.join(
            "secure_storage",
            application_folder
        )

        if os.path.isdir(folder_path):

            blocks = [
                file for file in os.listdir(folder_path)
                if file.startswith("encrypted_block_")
                and file.endswith(".bin")
            ]

            filename = "Unknown Document"

            filename_path = os.path.join(
                folder_path,
                "filename.txt"
            )

            if os.path.exists(filename_path):

                with open(filename_path, "r") as file:
                    filename = file.read()

            files.append({
                "application": application_folder.replace(
                    "application_", ""
                ),
                "filename": filename,
                "blocks": len(blocks)
            })

    return files