import os


def files_list():
    folders = input(
        "Please enter the list of folders with space in between them: ").split()

    for folder in folders:
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            print("Please provide a vaild Folder Name: " + folder)
            continue
        except PermissionError:
            print("The User does not have permission for the folder: " + folder)
            continue

        print()
        print("The Files in the folder are: " + folder)

        for file in files:
            print(f"The files in the '{folder}' are : '{file}'")


files_list()
