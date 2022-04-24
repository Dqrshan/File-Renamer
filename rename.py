import os

directory = input("Enter path of folder: ")
fileName = input("New prefix of the file names: ")
os.chdir(directory)
print(os.getcwd())

try:
    for i, f in enumerate(os.listdir()):
        name, ext = os.path.splitext(f)
        name = f"{fileName}_{str(i)}"
        new = ""
        if not ext:
            print("Found a directory..")
            new = f"folder_{name}"
            os.rename(f, new)
            continue

        new = f"{name}{ext}"

        os.rename(f, new)
except IsADirectoryError:
    print("Error: Destination is a directory")
except NotADirectoryError:
    print("Error: Source is a directory")
except PermissionError:
    print("Missing Permissions")
except OSError as e:
    print(e)

print(f"Successfully renamed {len(os.listdir())} files")
