"""
Smart File Organizer (SFO)

A lightweight Python tool for automatically organizing files into structured folders.
Designed with modular architecture for scalability and CI/CD integration.
"""

__version__ = "1.0.0"

# Public API (what users of the package are allowed to import directly)
from .core import organize

__all__ = [
    "organize",
    "__version__"
]

"""
Let’s walk through this piece of code carefully. It’s typical of a package’s __init__.py, where you define what your package exposes to users.

Line 1
__version__ = "1.0.0"
What it does
Defines a variable called __version__ and assigns it the string "1.0.0".
Why it is used

Provides a simple way to check the package version programmatically:

import your_package
print(your_package.__version__)
Useful for:
debugging
compatibility checks
logging
This is a widely used convention in Python packages.
Line 2–3
# Public API (what users of the package are allowed to import directly)
from .core import organize
What it does
Imports the function organize from a module named core in the same package (. means “current package”).
Why it is used
Exposes organize at the package level.

Without this line, users would need to write:

from your_package.core import organize

With this line, they can simply write:

from your_package import organize

👉 This improves usability and creates a cleaner public interface.

Line 4–7
__all__ = [
    "organize",
    "__version__"
]
What it does
Defines a list of names that are considered the public API of the module.
Why it is used
1. Controls from package import *

If someone does:

from your_package import *

Only the names in __all__ will be imported:

organize
__version__
2. Documents intended usage

It signals to users and developers:

“These are the officially supported things you should use.”

3. Hides internal implementation details

Anything not in __all__ is treated as internal (even though Python doesn’t strictly enforce it).

Putting it all together

This file is essentially defining a clean public interface for your package:

It exposes:
organize → main functionality
__version__ → metadata
It hides:
internal modules like core.py from direct use (unless explicitly accessed)
Resulting user experience

With this setup, users can do:

from your_package import organize, __version__

Instead of:

from your_package.core import organize
Big picture

This pattern is about API design:

Keep internal structure flexible
Expose only what matters
Make the package easy to use
"""