import zipfile
import os
import shutil
from tqdm import tqdm


# Takes a directory of zip files and mass extracts them
def mass_extract(target_dir):
    old_dir = os.getcwd()
    os.chdir(target_dir)
    for file in tqdm(os.listdir()):
        if zipfile.is_zipfile(file):
            with zipfile.ZipFile(file, 'r') as zipFile:
                zipFile.extractall(file.split('.')[0])
    os.chdir(old_dir)


def combine(target_dir):
    old_dir = os.getcwd()
    os.chdir(target_dir)
    for folder in os.listdir():
        for subFolder in os.listdir(folder):
            for file in os.listdir(os.path.join(folder, subFolder)):
                shutil.copy2(os.path.join(folder, subFolder, file), folder)
    os.chdir(old_dir)


if __name__ == '__main__':
    mass_extract('temp')