# smart-file-organizer

# Smart File Organizer (SFO)

A Python CLI tool that organizes messy folders into structured categories.

---

## 🚀 Features

- Auto file classification by extension
- Custom rules via config.json
- Safe file moving (prevents overwrites)
- Dry-run mode (preview changes)
- Logging system
- Modular architecture (CI/CD ready)

---

## 📦 Usage

### Organize folder
```bash
python main.py /path/to/folder
```

# Dry run (safe preview)
```bash
python main.py /path/to/folder --dry-run
```

# Example
Before:
```bash
Downloads/
  image.png
  doc.pdf
  script.py
```

After:
```bash
Downloads/
  Images/
  Documents/
  Code/
```

# Design Philosophy
- Separation of concerns
- Testable modules
- CI/CD ready structure
- Minimal dependencies


---

# 📁 SOURCE CODE (`src/sfo/`)

---

# 📄 `src/sfo/__init__.py`

## 🧠 Why this exists
Marks `sfo` as a Python package.

Also allows future:
- versioning
- imports like `from sfo import ...`

## ✅ Code

```python
__version__ = "1.0.0"