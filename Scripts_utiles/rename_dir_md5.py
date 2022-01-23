import glob
import hashlib
from pathlib import Path
import os

<<<<<<< HEAD
=======
# if os.path.exists(os.path.normpath("./JPEGImages/")):
#     print("[ERROR] Path not found: 'JPEGImages'")
#     quit()

path = "JPEGImages"
filenames = glob.glob(os.path.join(path, "*.jpg"))
filenames += glob.glob(os.path.join(path, "*.jpeg"))
filenames += glob.glob(os.path.join(path, "*.JPG"))
filenames += glob.glob(os.path.join(path, "*.JPEG"))

file_old = []
file_new = []
>>>>>>> 5e9fabf90c81fcad539562f01c463623d637b01a

# Check if path exist
path = "JPEGImages"
if Path(path).is_file():
    print("[ERROR] Path not found: 'JPEGImages'")
    quit()

# Append pictures
file_names = glob.glob(os.path.join(path, "*.jpg"))
file_names += glob.glob(os.path.join(path, "*.jpeg"))
file_names += glob.glob(os.path.join(path, "*.JPG"))
file_names += glob.glob(os.path.join(path, "*.JPEG"))
file_names += glob.glob(os.path.join(path, "*.png"))

# Iterate on all picture for get md5sum
file_old = []
file_new = []
for filename in file_names:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        file_old.append(os.path.basename(filename))
        file_new.append(hashlib.md5(data).hexdigest() + os.path.splitext(filename)[1])
<<<<<<< HEAD
        print("file_old {}".format(file_old[-1]))
        print("file_new {}".format(file_new[-1]))

    # Move original name to md5sum name
=======

        print("file_old {}".format(file_old[-1]))
        print("file_new {}".format(file_new[-1]))
>>>>>>> 5e9fabf90c81fcad539562f01c463623d637b01a
    os.rename(os.path.join(path, file_old[-1]), os.path.join(path, file_new[-1]))