# HOW TO USE AND TEST: Smart File Organizer (SFO)

## STEP 1 — Create the Project

Make sure your folder structure looks exactly like this:
```
smart-file-organizer/
```

Navigate into it:
```
cd smart-file-organizer
```

## STEP 2 — Set Up Python Environment (Recommended)
Create a virtual environment
```
python -m venv venv
```
### Activate it

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

## STEP 3 — Install Dependencies

Right now:
```
pip install -r requirements.txt
```
(There are no dependencies yet, but this step is important for CI/CD later.)

## STEP 4 — Run the Application

Basic usage:
```
python main.py /path/to/your/folder
```
✅ Example (real usage)
```
python main.py ~/Downloads
```
or on Windows:
```
python main.py C:\Users\YourName\Downloads
```

## STEP 5 — Use Dry Run (IMPORTANT FIRST)

Before moving real files, preview what will happen:
```
python main.py /path/to/folder --dry-run
```
Example:
```
python main.py ~/Downloads --dry-run
```
Output looks like:
```
[DRY RUN] file1.jpg -> /Downloads/Images
[DRY RUN] report.pdf -> /Downloads/Documents
```
👉 This ensures:
- No accidental file movement
- Safe testing

## STEP 6 — Run Actual Organization

Once you're confident:
```
python main.py /path/to/folder
```
Example:
```
python main.py ~/Downloads
```
What happens:
- Files are scanned
- Categorized
- Moved into folders like:
Downloads/
  Images/
  Documents/
  Code/
  Others/

## STEP 7 — Customize Behavior (config.json)

Open:
config.json

Example:
```
{
  "rules": {
    "Projects": [".zip"],
    "Notes": [".md"],
    "Installers": [".exe"]
  }
}
```
What this does:
.zip → Projects/
.md → Notes/
.exe → Installers/

👉 You can define your own categories without touching code.

## STEP 8 — Check Logs

After running, check:
```
logs/sfo.log
```
Example content:
```
2026-04-18 | INFO | /Downloads/file.pdf -> /Downloads/Documents/file.pdf
```
👉 Useful for:
- debugging
- CI/CD validation later
- tracking file changes

## STEP 9 — Run Tests (Optional but Important)

Install pytest (if not already):
```
pip install pytest
```
Run tests:
```
pytest
``
👉 This verifies:
- file scanning works
- rules work
- safe file movement works

## STEP 10 — Important Safety Notes
The app moves files (not copies)
Always use ```--dry-run``` first

Avoid running on:
- system directories
- critical project folders

## REAL-WORLD USE CASES

You can now use this for:

📥 Cleaning Downloads folder
```
python main.py ~/Downloads
```
🧹 Organizing Desktop clutter
```
python main.py ~/Desktop
```
📁 Sorting project dumps
```
python main.py ~/Projects/messy-folder
```

WHAT WE’VE BUILT (IMPORTANT)

You didn’t just build a script—you now have:
- CLI application
- modular architecture
- config-driven system
- logging system
- test suite
- CI/CD-ready structure

## NEXT STEP

Now that you can run and use the app, the logical next step is:

###🔥 GitHub Actions CI/CD pipeline

We’ll add:
- automatic testing on push
- linting (ruff/flake8)
- formatting checks
- build validation