import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compresses.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


# if __name__ == "__main__":
#     make_archive(filepaths=["bonus1.py","bonus2.1.py"], dest_dir="dest")