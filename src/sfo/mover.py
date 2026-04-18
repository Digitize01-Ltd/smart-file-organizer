"""
This handles safe file operations:

prevents overwrites
handles duplicates
isolates filesystem logic

This is critical for production safety.
"""

import os
import shutil


def ensure_unique_path(path):
    if not os.path.exists(path):
        return path

    base, ext = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = f"{base} ({counter}){ext}"
        counter += 1

    return path


def move_file_safe(file_path, target_dir):
    os.makedirs(target_dir, exist_ok=True)

    filename = os.path.basename(file_path)
    destination = os.path.join(target_dir, filename)

    safe_destination = ensure_unique_path(destination)

    shutil.move(file_path, safe_destination)

    return safe_destination

"""
Let’s go step by step through this code. This is a safe file-moving utility, designed to avoid overwriting existing files by automatically renaming them when needed.

Line 1
import os
What it does
Imports Python’s built-in os module.
Why it is used
Used for filesystem operations like:
checking if a file exists
splitting file names
joining paths
creating directories
Line 2
import shutil
What it does
Imports the shutil module.
Why it is used
Provides high-level file operations like:
moving files (shutil.move)
copying files
removing directories
===============================
FUNCTION 1: ensure_unique_path
===============================
Line 5
def ensure_unique_path(path):
What it does
Defines a function that ensures a file path does not already exist.
Why it is used
Prevents overwriting existing files.
Instead of replacing files, it renames new ones safely.
Line 6–7
if not os.path.exists(path):
    return path
What it does
Checks if the file path already exists.
If it does NOT exist → returns it immediately.
Why it is used
Fast path optimization:
If no conflict exists, no need to rename anything.
Line 9
base, ext = os.path.splitext(path)
What it does
Splits the file path into:
base → file name without extension
ext → file extension
Example:
photo.jpg

Becomes:

base = "photo"
ext = ".jpg"
Why it is used

Needed so we can generate new names like:

photo (1).jpg
photo (2).jpg
Line 10
counter = 1
What it does
Initializes a counter used for numbering duplicates.
Why it is used
Helps generate unique file names incrementally.
Line 12
while os.path.exists(path):
What it does
Loops while the current file path already exists.
Why it is used
Ensures we keep trying new names until we find a free one.
Line 13
path = f"{base} ({counter}){ext}"
What it does
Creates a new file name with a number suffix.
Example progression:
photo.jpg
photo (1).jpg
photo (2).jpg
Why it is used
Prevents overwriting existing files.
Mimics behavior of file systems like Windows/macOS.
Line 14
counter += 1
What it does
Increments the counter.
Why it is used
Ensures the next filename is different if conflict still exists.
Line 16
return path
What it does
Returns a safe, unique file path.
Why it is used
Final output of the function.
===============================
FUNCTION 2: move_file_safe
===============================
Line 19
def move_file_safe(file_path, target_dir):
What it does
Defines a function to safely move a file into a directory.
Why it is used
Wraps file-moving logic with safety checks.
Line 20
os.makedirs(target_dir, exist_ok=True)
What it does
Creates the destination folder if it does not exist.
Why it is used

Prevents errors like:

FileNotFoundError: No such directory
exist_ok=True ensures no error if folder already exists.
Line 22
filename = os.path.basename(file_path)
What it does
Extracts just the file name from a full path.
Example:
/downloads/photo.jpg → photo.jpg
Why it is used
Needed to reconstruct destination path correctly.
Line 23
destination = os.path.join(target_dir, filename)
What it does
Builds the full destination path.
Example:
target_dir = /images
filename = photo.jpg
→ /images/photo.jpg
Why it is used
Prepares file for moving.
Line 25
safe_destination = ensure_unique_path(destination)
What it does
Ensures the destination file name won’t overwrite existing files.
Why it is used
Protects against data loss.
Automatically renames duplicates.
Line 27
shutil.move(file_path, safe_destination)
What it does
Physically moves the file to the new location.
Why it is used
This is the actual file operation.
Line 29
return safe_destination
What it does
Returns the final location of the moved file.
Why it is used
Useful for:
logging
user feedback
further processing
===============================
OVERALL FLOW
===============================

When you call:

move_file_safe("/downloads/photo.jpg", "/images")
Step-by-step:
Ensure /images exists
Extract filename → photo.jpg
Build destination → /images/photo.jpg
Check if file exists:
if yes → rename to photo (1).jpg, photo (2).jpg, etc.
Move file
Return final path
===============================
WHY THIS DESIGN IS GOOD
===============================
✔ Prevents data loss

No overwriting existing files.

✔ User-friendly behavior

Automatic renaming like OS file systems.

✔ Reusable logic

ensure_unique_path() can be used anywhere.

✔ Clean separation
naming logic → ensure_unique_path
moving logic → move_file_safe
🧠 Mental model

Think of it like a careful librarian:

Before placing a book (file), it checks the shelf
If space is taken, it renames the new book:
Book
Book (1)
Book (2)
Then places it safely

If you want, I can next show you:

a faster version using pathlib
or 
how to make this concurrency-safe (important for real production systems)
"""