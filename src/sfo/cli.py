"""
This is the user interface layer:

parses terminal commands
passes control to core logic

Keeps CLI separate from business logic.
"""

import argparse
from .core import organize


def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer (SFO)")

    parser.add_argument("path", help="Folder path to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()

    organize(args.path, dry_run=args.dry_run)

"""
Let’s go through this step by step and explain both what each line does and why it’s written that way. This is a typical CLI (command-line interface) entry function.

Line 1
import argparse
What it does
Imports Python’s built-in argparse module.
Why it is used
argparse is used to:
read command-line arguments
validate them
provide help messages automatically

Without it, you’d have to manually parse things like:

python app.py folder --dry-run
Line 2
from .core import organize
What it does
Imports the organize function from a local module called core.
Why it is used
Keeps the CLI logic separate from the actual functionality.
organize() likely contains the real file-handling logic.
This separation improves:
testing
readability
maintainability
Line 5
def main():
What it does
Defines a function named main.
Why it is used
Acts as the entry point of the CLI program.
This function will be called when the program runs.
Makes the code reusable (you can call main() from elsewhere).
Line 6
parser = argparse.ArgumentParser(description="Smart File Organizer (SFO)")
What it does
Creates a new argument parser object.
Adds a description for the program.
Why it is used

The description appears when users run:

python app.py --help
Helps users understand what the program does.
Line 8
parser.add_argument("path", help="Folder path to organize")
What it does
Defines a positional argument called path.
Why it is used
This argument is required.

The user must provide it:

python app.py /home/user/downloads
It tells the program which folder to organize.
Line 9–13
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Preview changes without moving files"
)
What it does
Adds an optional flag called --dry-run.
Key detail: action="store_true"
If the flag is included → value becomes True
If not included → value is False
Why it is used

Allows users to simulate the operation:

python app.py /folder --dry-run
Prevents accidental file changes.
Very common safety feature in CLI tools.
Line 15
args = parser.parse_args()
What it does
Parses the command-line input.
Converts arguments into an object (args).
Result

If user runs:

python app.py my_folder --dry-run

Then:

args.path     # "my_folder"
args.dry_run  # True
Why it is used
Provides structured access to user input.
Avoids manual string parsing.
Line 17
organize(args.path, dry_run=args.dry_run)
What it does
Calls the organize function.
Passes:
the folder path
whether it’s a dry run
Why it is used
This is where the actual program logic starts.
Delegates work to the core functionality.
Overall Flow

When a user runs:

python app.py /my/files --dry-run
Execution steps:
main() is called
Argument parser is created
Arguments are defined (path, --dry-run)
User input is parsed
Values stored in args
organize() is called with those values
Why this design is good
✔ Separation of concerns
CLI parsing → main()
Business logic → organize()
✔ Safe execution
--dry-run prevents unintended file changes
✔ User-friendly

Automatic help messages:

python app.py --help
Quick mental model

Think of it like this:

argparse → listens to user input
main() → translates input into actions
organize() → does the real work
"""