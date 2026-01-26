# How to Run Test Cases 

This document explains how to run the provided test cases for the `suggest_slots` function using **pytest**.

---

## 1. Install pytest

If you don't already have `pytest` installed, you can install it using pip:

```bash
pip install pytest
```

Verify the installation:

```bash
pytest --version
```

---

## 2. Organize Your Files

Place your implementation and test files in the same directory:

```
/project-folder
    solution.py         # your implementation
    test_solution.py    # your test cases
```

* `solution.py` contains the `suggest_slots` function.
* `test_solution.py` contains the test functions.

> **Note:** If your file names are different, adjust the instructions below accordingly.

---

## 3. Update Test File Import

In `test_solution.py`, import your implementation module. For example:

```python
import importlib
solution = importlib.import_module("solution")  # replace "solution" with your implementation file name without .py
```

---

## 4. Run All Tests

Navigate to the folder containing the files and run:

```bash
pytest
```

Or with more detailed output:

```bash
pytest -v
```

Expected output:

```
test_solution.py::test_no_events_returns_sorted_list PASSED
test_solution.py::test_lunch_break_excluded PASSED
test_solution.py::test_overlap_event_removed PASSED
test_solution.py::test_friday_rule_respected PASSED
```

---

## 5. Run a Specific Test Function

To run a single test function, use the `-k` option:

```bash
pytest -v -k test_lunch_break_excluded
```

---

## 6. If Your File Names Are Different

* **Test file**: If your test file doesn't match `test_*.py` or `*_test.py`, specify it explicitly:

```bash
pytest mytests.py
```

* **Implementation file**: Update the import in the test file:

```python
solution = importlib.import_module("meeting")  # if your file is meeting.py
```

* Run a single test in a differently named file:

```bash
pytest -v mytests.py -k test_lunch_break_excluded
```

---

## Summary

1. Install `pytest`
2. Organize files
3. Update the import in test file if necessary
4. Run all tests: `pytest -v`
5. Run a single test: `pytest -v -k <test_name>`
6. Adjust commands if file names differ

---

You are ready to run the test cases for your `suggest_slots` implementation!
