"""
Ensures:

classification logic works correctly
"""

from src.sfo.rules import get_category


def test_get_category_image():
    assert get_category("photo.jpg") == "Images"


def test_get_category_unknown():
    assert get_category("file.xyz") == "Others"

"""
This is a small unit test file (again likely using pytest) that verifies the correctness of the get_category() function. Let’s go line by line.

=========================
LINE 1
=========================
from src.sfo.rules import get_category
What it does
Imports the get_category function from src.sfo.rules.
Why it is used
This is the function being tested (the “unit under test”).
The test file needs direct access to it in order to call it.
=========================
TEST 1
=========================
Line 4
def test_get_category_image():
What it does
Defines a test function named test_get_category_image.
Why it is used
In pytest, any function starting with test_ is automatically discovered and executed.
This test specifically checks image classification behavior.
Line 5
assert get_category("photo.jpg") == "Images"
What it does
Calls get_category("photo.jpg")
Checks whether the result equals "Images"
Why it is used
Validates that image files are correctly categorized.
"photo.jpg" should map to the "Images" category based on rules.
What happens if it fails?
Test fails → function is not behaving correctly.
=========================
TEST 2
=========================
Line 8
def test_get_category_unknown():
What it does
Defines another test function.
Why it is used
This test checks how the function behaves with unknown file types.
Line 9
assert get_category("file.xyz") == "Others"
What it does
Calls get_category("file.xyz")
Expects result to be "Others"
Why it is used
Ensures the fallback behavior works correctly.
Confirms that unknown extensions do not break the system.
=========================
OVERALL PURPOSE OF THIS FILE
=========================

This test suite checks two key behaviors:

✔ 1. Known file type handling
photo.jpg → Images

Ensures:

mapping rules work correctly
image classification is correct
✔ 2. Unknown file type handling
file.xyz → Others

Ensures:

system has a safe fallback
unknown files don’t cause errors
=========================
EXECUTION FLOW (PYTEST)
=========================

When you run:

pytest
Step-by-step:
pytest discovers functions starting with test_
Runs test_get_category_image()
asserts "photo.jpg" → "Images"
Runs test_get_category_unknown()
asserts "file.xyz" → "Others"
Reports success or failure
=========================
WHY THIS TEST DESIGN IS GOOD
=========================
✔ Simple

Each test checks one behavior only.

✔ Clear intent
image case
unknown case
✔ Fast

No file system or external dependencies

✔ Deterministic

Same input → same output every time

=========================
MENTAL MODEL
=========================

Think of this as:

“I give the function a file name and check if it puts it in the right folder.”

It’s basically verifying a sorting brain:

photo.jpg → should go to Images
file.xyz → should go to Others
=========================
LIMITATION (IMPORTANT)
=========================

These tests are unit-level only, meaning:

They do NOT test:

config overrides
real file movement
integration with scanner/mover/logger
edge cases like uppercase extensions (.JPG)

If you want, I can next show you:

how to write integration tests for the full file organizer
or 
how to test file system behavior safely using tmp_path (very useful in real projects)
"""