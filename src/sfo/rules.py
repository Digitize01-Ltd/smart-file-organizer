"""
This is the classification engine:

decides where files go
supports config overrides

This is where you later plug in AI classification if you want.
"""

import os
import json

CONFIG_FILE = "config.json"


DEFAULT_RULES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".js", ".ts", ".html", ".css"]
}


def load_custom_rules():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f).get("rules", {})
    except FileNotFoundError:
        return {}


def get_category(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    rules = DEFAULT_RULES.copy()
    rules.update(load_custom_rules())

    for category, extensions in rules.items():
        if ext in extensions:
            return category

    return "Others"

"""
Let’s go step by step through this code. This is a file classification system that decides which folder a file belongs to based on its extension, while also supporting user-defined rules from a config file.

=========================
IMPORTS
=========================
Line 1
import os
What it does
Imports Python’s built-in os module.
Why it is used
Used for file path operations, especially:
extracting file extensions
working with file paths in a cross-platform way
Line 2
import json
What it does
Imports the json module.
Why it is used
Allows reading JSON configuration files (like config.json)
Converts JSON → Python dictionary
=========================
CONFIG FILE PATH
=========================
Line 4
CONFIG_FILE = "config.json"
What it does
Defines the file name for configuration.
Why it is used
Centralizes config location.
Makes it easy to change later.
=========================
DEFAULT RULES
=========================
Lines 7–14
DEFAULT_RULES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".js", ".ts", ".html", ".css"]
}
What it does
Defines built-in file categorization rules.
Why it is used
Acts as a fallback system if no user configuration exists.
Ensures the program always works even without config.json.
Conceptually:

This is the default knowledge base of the system.

=========================
LOAD CUSTOM RULES
=========================
Line 17
def load_custom_rules():
What it does
Defines a function to load user-defined rules.
Why it is used
Separates configuration loading logic from classification logic.
Line 18
try:
What it does
Starts error-handling block.
Why it is used
File operations may fail (missing file, corrupted JSON, etc.).
Line 19–20
with open(CONFIG_FILE, "r") as f:
    return json.load(f).get("rules", {})
What it does step by step:
Opens config.json
Reads JSON content
Converts it into Python dictionary
Extracts "rules" key
If "rules" doesn't exist → returns {}
Why it is used
Safely loads user-defined categorization rules.
Prevents crashes if config structure is incomplete.
Line 21–22
except FileNotFoundError:
    return {}
What it does
If config file doesn’t exist:
returns empty dictionary
Why it is used
Prevents program failure.
Allows system to fall back to DEFAULT_RULES.
=========================
CATEGORY DETECTION
=========================
Line 25
def get_category(file_path):
What it does
Defines function to determine file category.
Why it is used
Core logic of the system:
→ decides where each file belongs
Line 26
ext = os.path.splitext(file_path)[1].lower()
What it does step by step:

Splits file path:

photo.jpg → ("photo", ".jpg")
Takes extension [1]
Converts to lowercase
Why it is used
Normalizes file extension for matching:
.JPG and .jpg are treated the same
Line 28
rules = DEFAULT_RULES.copy()
What it does
Creates a copy of default rules.
Why it is used
Prevents modifying the original DEFAULT_RULES.
Line 29
rules.update(load_custom_rules())
What it does
Loads custom rules from config.
Merges them into default rules.
Why it is used
Enables user customization while preserving defaults.
Important behavior:
If user defines a category, it overrides or extends defaults.
Line 31–33
for category, extensions in rules.items():
    if ext in extensions:
        return category
What it does step by step:

Loops through each category:

Images → [.jpg, .png, ...]
Documents → [.pdf, ...]
Checks if file extension matches any list
If match found → returns category immediately
Why it is used
Efficient classification (stops at first match).
Simple rule-based system.
Line 35
return "Others"
What it does
If no match is found → assign file to "Others"
Why it is used
Ensures every file gets categorized.
Prevents None or errors.
=========================
OVERALL FLOW
=========================

When you call:

get_category("file.xyz")
Step-by-step execution:
Extract file extension → .xyz
Load default rules
Load custom rules (if any)
Merge both rule sets
Loop through categories:
check if extension matches
If match found → return category
If no match → return "Others"
=========================
WHY THIS DESIGN IS GOOD
=========================
✔ Flexible

Users can override or extend rules via JSON.

✔ Safe

Defaults always exist, so system never breaks.

✔ Modular
loading rules → separate function
classification → separate function
✔ Extensible

You can easily add:

priority rules
regex matching
MIME type detection
=========================
MENTAL MODEL
=========================

Think of it like a sorting assistant:

You show it a file
It checks its built-in knowledge (DEFAULT_RULES)
It checks user preferences (config.json)
It decides the best category
If unsure → puts it in “Others”

If you want, I can next show you:

how to add priority rules (so custom rules always override defaults properly)
or 
how to upgrade this into a machine-learning-based file classifier (advanced version)
"""