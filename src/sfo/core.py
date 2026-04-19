"""
This is the brain of the application.

It:

connects all modules
controls flow
decides what happens and when

This is where CI/CD tests will focus.
"""

import os
from .scanner import scan_files
from .rules import get_category
from .mover import move_file_safe
from .logger import log_action


def organize(path, dry_run=False):
    files = scan_files(path)

    if not files:
        print("No files found.")
        return

    for file_path in files:
        category = get_category(file_path)
        target_dir = os.path.join(path, category)

        if dry_run:
            print(f"[DRY RUN] {file_path} -> {target_dir}")
            continue

        new_path = move_file_safe(file_path, target_dir)

        log_action(f"{file_path} -> {new_path}")
        print(f"Moved: {file_path} -> {category}")

    print("Organization complete.")


"""
This is a nicely modular version of a file organizer. Instead of doing everything in one function, it delegates responsibilities to different modules (scanner, rules, mover, logger). Let’s go line by line.

Line 1
import os
What it does
Imports Python’s built-in os module.
Why it is used

Needed for path operations like:

os.path.join()
Helps build platform-independent file paths (Windows, Linux, macOS).
Lines 2–5
from .scanner import scan_files
from .rules import get_category
from .mover import move_file_safe
from .logger import log_action
What each does
scan_files
Finds all files in a directory (likely recursively or flat scan).
get_category
Decides what category a file belongs to (e.g., Images, Documents).
move_file_safe
Moves a file while handling edge cases (like duplicates or missing folders).
log_action
Records what happened (for debugging or audit purposes).
Why this structure is used

This is modular design:

Instead of one big function, each responsibility is separated:

scanning → scanner.py
classification → rules.py
moving → mover.py
logging → logger.py

👉 This makes the system:

easier to test
easier to maintain
easier to extend
Line 8
def organize(path, dry_run=False):
What it does
Defines the main function that organizes files.
Parameters:
path: folder to organize
dry_run: whether to simulate actions
Why it is used
Central entry point for the organization process.
dry_run adds safety for previewing changes.
Line 9
files = scan_files(path)
What it does
Calls scan_files() to get a list of files.
Result example:
["/downloads/a.jpg", "/downloads/b.pdf"]
Why it is used
Separates scanning logic from organizing logic.
Keeps organize() clean and high-level.
Line 11–13
if not files:
    print("No files found.")
    return
What it does
Checks if the folder has no files.
Stops execution if empty.
Why it is used
Prevents unnecessary processing.
Provides user feedback.
Line 15
for file_path in files:
What it does
Loops through each file found.
Why it is used
Core processing loop: handle one file at a time.
Line 16
category = get_category(file_path)
What it does
Determines which category the file belongs to.
Example:
file.jpg → "Images"
file.pdf → "Documents"
Why it is used
Delegates classification logic to rules.py
Keeps organize() independent of rule logic
Line 17
target_dir = os.path.join(path, category)
What it does
Builds destination folder path.
Example:
/downloads + Images → /downloads/Images
Why it is used
Ensures correct platform-safe path creation.
Line 19–21 (dry run mode)
if dry_run:
    print(f"[DRY RUN] {file_path} -> {target_dir}")
    continue
What it does
If dry run is enabled:
prints what would happen
skips actual execution
Why it is used
Safety feature:
prevents accidental file movement
allows preview of changes
Line 23
new_path = move_file_safe(file_path, target_dir)
What it does
Moves the file safely to the target folder.
Returns the new file location.
Why it is used
Encapsulates complex logic:
handling duplicates
ensuring directory exists
avoiding overwrite issues
Line 25
log_action(f"{file_path} -> {new_path}")
What it does
Logs the file movement operation.
Why it is used
Creates an audit trail:
useful for debugging
useful for tracking changes
useful for user transparency
Line 26
print(f"Moved: {file_path} -> {category}")
What it does
Prints confirmation message to user.
Why it is used
Provides real-time feedback in CLI.
Line 28
print("Organization complete.")
What it does
Prints final completion message after loop ends.
Why it is used
Signals end of process.
Improves user experience.
Overall flow (big picture)

When you call:

organize("/downloads", dry_run=False)
Step-by-step execution:
Scan all files in folder
If no files → stop
For each file:
determine category
compute destination folder
if dry run → show preview
else:
move file safely
log action
print confirmation
Print completion message
Why this architecture is strong
✔ Separation of concerns

Each module has a single job:

scanner → finds files
rules → categorizes
mover → handles file operations
logger → records actions
✔ Testability

You can test each component independently.

✔ Scalability

You can upgrade one part without breaking others.

Mental model

Think of it like a factory:

scanner → collects raw materials (files)
rules → decides where things go
mover → physically moves items
logger → keeps records
organize() → factory manager coordinating everything

If you want, I can next show you:

what move_file_safe() typically looks like (it’s actually the trickiest part)
or 
how to convert this into a professional CLI package with pyproject.toml
"""
