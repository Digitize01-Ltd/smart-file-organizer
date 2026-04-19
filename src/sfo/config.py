"""
Provides a safe abstraction layer for configuration loading.

Even though rules.py uses config directly, this prepares for:

environment configs
remote configs
CI/CD injected settings
"""

import json

CONFIG_FILE = "config.json"


def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"rules": {}}


"""
Let’s go through this carefully, line by line, and explain both what happens and why it’s written this way. This is a small utility function for loading configuration from a JSON file.

Line 1
import json
What it does
Imports Python’s built-in json module.
Why it is used
The json module allows you to:
read JSON files → convert them into Python objects (dicts, lists)
write Python objects → save them as JSON
Line 3
CONFIG_FILE = "config.json"
What it does
Defines a constant variable holding the filename "config.json".
Why it is used
Centralizes the config file name in one place.
Makes it easy to:
change the file name later
reuse it across functions
Improves readability (you know what file is being used).
Line 6
def load_config():
What it does
Defines a function named load_config.
Why it is used
Encapsulates the logic for reading configuration.
Makes it reusable anywhere in your program.
Keeps your code modular and clean.
Line 7
try:
What it does
Starts a try block for exception handling.
Why it is used
File operations can fail (e.g., file doesn’t exist).
Prevents the program from crashing.
Lets you define fallback behavior.
Line 8–9
with open(CONFIG_FILE, "r") as f:
    return json.load(f)
What it does
Step-by-step:
open(CONFIG_FILE, "r")
Opens config.json in read mode.
with ... as f
Creates a file object f.
Automatically closes the file after use.
json.load(f)
Reads the JSON content from the file.
Converts it into a Python dictionary (or list).
return
Returns the parsed data immediately.
Why it is used
✔ with open(...)
Ensures the file is properly closed (even if errors occur).
✔ json.load()
Converts JSON into usable Python data structures.
✔ return inside the block
Immediately returns the config once successfully loaded.
Line 10–11
except FileNotFoundError:
    return {"rules": {}}
What it does
Catches the specific error when the file does not exist.

Returns a default configuration:

{"rules": {}}
Why it is used
✔ Graceful fallback
If config.json is missing, the program still works.
✔ Prevents crashes
Without this, Python would raise an error and stop execution.
✔ Provides a default structure

Ensures the rest of the program can safely assume:

config["rules"]

exists.

Overall flow
Case 1: File exists
Open config.json
Parse JSON
Return dictionary
Case 2: File does NOT exist
open() raises FileNotFoundError
Execution jumps to except

Returns:

{"rules": {}}
Example
config.json
{
  "rules": {
    ".jpg": "Images",
    ".pdf": "Documents"
  }
}
Returned value:
{
  "rules": {
    ".jpg": "Images",
    ".pdf": "Documents"
  }
}
Why this design is good
✔ Robust
Handles missing files safely
✔ Clean
Simple and readable
✔ Predictable
Always returns a dictionary with "rules"
One subtle improvement (optional)

Right now, it only handles missing files. You might also want to handle invalid JSON:

except (FileNotFoundError, json.JSONDecodeError):

This prevents crashes if the file exists but is corrupted.

If you want, 
I can show you how this config could be integrated into your organize() function to make file rules user-configurable.
"""
