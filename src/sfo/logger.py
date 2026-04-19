"""
Logging is critical for:

debugging
CI/CD pipelines
audit trails

Later you can plug into:

cloud logs
ELK stack
Datadog
"""

import logging
import os

os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/sfo.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_action(message):
    logging.info(message)


"""
Let’s go through this step by step. This is a simple but very common logging setup used in real applications to track what the program is doing.

Line 1
import logging
What it does
Imports Python’s built-in logging module.
Why it is used
Provides a standard way to record events (logs) from your program.
Much better than using print() for real applications because logs can be:
saved to files
categorized (info, warning, error, etc.)
timestamped
filtered later
Line 2
import os
What it does
Imports the os module.
Why it is used
Needed to interact with the file system.
Here it is used to create directories safely.
Line 4
os.makedirs("logs", exist_ok=True)
What it does
Creates a folder called logs.
Breakdown:
"logs" → folder name
exist_ok=True → do nothing if folder already exists
Why it is used
Ensures the log directory exists before writing log files.

Prevents errors like:

FileNotFoundError: No such file or directory
Line 6
LOG_FILE = "logs/sfo.log"
What it does
Defines the path to the log file.
Why it is used
Centralizes configuration.
Makes it easy to change log file location in one place.
Line 8–12
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

This is the core logging configuration.

What each parameter does
1. filename=LOG_FILE

Sends all logs to the file:

logs/sfo.log
Why
Persistent storage of logs (they survive program exit).
2. level=logging.INFO
Sets minimum logging level to INFO.
Logging levels (simplified):
DEBUG → detailed development info
INFO → normal operations
WARNING → something unusual
ERROR → failure occurred
CRITICAL → severe failure
Why
Filters out unnecessary low-level logs.
3. format="%(asctime)s | %(levelname)s | %(message)s"
What it does

Defines how each log line looks.

Example output:

2026-04-18 12:30:00 | INFO | File moved successfully
Breakdown:
%(asctime)s → timestamp
%(levelname)s → log level (INFO, ERROR, etc.)
%(message)s → actual log message
Why
Makes logs readable and structured for debugging.
Line 15
def log_action(message):
What it does
Defines a function to log messages.
Why it is used
Wraps logging logic in a reusable function.
Keeps other parts of the system clean.
Line 16
logging.info(message)
What it does
Writes a log entry at INFO level.
Example:
log_action("file.jpg -> Images")

Becomes:

2026-04-18 12:30:00 | INFO | file.jpg -> Images
Why it is used
Centralized logging function ensures:
consistent formatting
easy updates later
avoids repeated logging code everywhere
Overall flow

When you call:

log_action("Moved file.jpg to Images")
Step-by-step execution:
log_action() is called
It calls logging.info()
Logging system formats message

Message is written to:

logs/sfo.log
Why this design is good
✔ Separation of concerns
Logging logic is isolated from business logic.
✔ Persistent records
Logs are saved permanently in a file.
✔ Structured output
Easy to read and debug.
✔ Scalable
You can later add:
rotating logs
different log files for errors
console + file logging simultaneously
Mental model

Think of it like a black box recorder for your program:

Every important action → recorded
Stored in a file
Can be reviewed later when something goes wrong

If you want, I can next show you:

how to add separate ERROR logs vs INFO logs
or how to upgrade this into a professional logging system (with rotating log files and console output at the same time)
"""
