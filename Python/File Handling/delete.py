import os
if os.path.exists("student.txt"):
    os.remove("student.txt")
    print("File deleted successfully")
else:
    print("No file found")


# Remove empty folder

import os
if os.path.exists("Folder"):
    os.rmdir("Folder")
    print("Folder deleted successfully")
else:
    print("No file found")