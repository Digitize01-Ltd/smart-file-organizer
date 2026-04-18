"""
Single responsibility:

only scans files
no business logic

This makes it:
easy to test
reusable later (watch mode, etc.)
"""

import os


def scan_files(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Invalid path: {path}")

    return [
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]

"""
Let’s go step by step through this function. This is a simple file scanner that lists all files in a given directory and returns their full paths.

=========================
LINE 1
=========================
import os
What it does
Imports Python’s built-in os module.
Why it is used
Needed for interacting with the file system:
checking if a path exists
listing directory contents
checking whether something is a file
building file paths safely
=========================
LINE 4
=========================
def scan_files(path):
What it does
Defines a function named scan_files.
Why it is used
Encapsulates the logic for scanning a directory.
Makes the function reusable anywhere in the program.
=========================
LINE 5
=========================
if not os.path.exists(path):
What it does
Checks whether the given path exists.
Why it is used
Prevents errors later in the code.
Ensures you don’t try to scan a folder that doesn’t exist.
=========================
LINE 6
=========================
raise FileNotFoundError(f"Invalid path: {path}")
What it does
Manually raises an error if the path is invalid.
Why it is used
Stops execution immediately when input is wrong.

Provides a clear error message for debugging:

Invalid path: /wrong/folder
=========================
LINE 8–13
=========================
return [
    os.path.join(path, f)
    for f in os.listdir(path)
    if os.path.isfile(os.path.join(path, f))
]

This is a list comprehension that builds a list of files.

Let’s break it down step by step:
1. os.listdir(path)
What it does

Gets all items in the directory:

["file1.txt", "file2.jpg", "folderA"]
Why it is used
This is how Python reads directory contents.
2. for f in os.listdir(path)
What it does
Loops through each item in the folder.
Why it is used
Processes each file/folder one by one.
3. os.path.isfile(os.path.join(path, f))
What it does
Checks if the item is a file (not a folder).
Breakdown:

os.path.join(path, f) → full path

/folder/file1.txt
os.path.isfile(...) → returns True if it is a file
Why it is used
Ensures only files are included, not directories.
4. os.path.join(path, f) (in output)
What it does
Builds full file path.
Example:
path = "/downloads"
f = "file.txt"
→ "/downloads/file.txt"
Why it is used
Ensures correct full paths instead of just filenames.
5. The full list comprehension
[
    os.path.join(path, f)
    for f in os.listdir(path)
    if os.path.isfile(os.path.join(path, f))
]
What it does overall
Returns a list of full file paths only.
Example output:
[
    "/downloads/file1.txt",
    "/downloads/image.png"
]
=========================
OVERALL FLOW
=========================

When you call:

scan_files("/downloads")
Step-by-step execution:
Check if /downloads exists
If not → raise error
List everything inside folder
For each item:
build full path
check if it's a file
Keep only files
Return list of file paths
=========================
WHY THIS DESIGN IS GOOD
=========================
✔ Safe
Prevents scanning invalid paths
✔ Clean
Uses list comprehension (compact and efficient)
✔ Accurate
Excludes directories automatically
✔ Reusable
Can be used in file organizers, backup tools, etc.
=========================
MENTAL MODEL
=========================

Think of it like a security guard at a building:

Looks at everything in the building (folder)
Ignores rooms (directories)
Only collects documents (files)
Returns a clean list of documents

If you want, I can next show you:

a recursive version (scans subfolders too)
or a pathlib version (more modern and cleaner Python style)
"""