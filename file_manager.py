import os


def create_directory(path):

    os.makedirs(path, exist_ok=True)

    print(f"Directory created: {path}")


def create_file(path, content):

    folder = os.path.dirname(path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"File created: {path}")