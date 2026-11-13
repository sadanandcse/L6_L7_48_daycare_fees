# L6_L7_48 — Daycare Fees

## Lab 6: Code and Branch Coverage

### About

A small Python module that calculates extra-hours fees based on the child's age group, number of hours, and sibling discount. It also checks whether an enrolment is allowed and reports the child's pickup status.

### Files

| File | Description |
|---|---|
| `daycare_fees.py` | Python module under test |
| `test_daycare_fees.py` | Test cases for the daycare fees module |
| `CodeCoverageTest_48_daycare_fees.py` | Code coverage test file |

### Testing

Run the tests using:

```bash
python -m pytest -v
```

### Code Coverage

Run coverage using:

```bash
coverage run -m pytest
coverage report -m
```

To generate an HTML coverage report:

```bash
coverage html
```

Open the generated report from the `htmlcov` folder.

### Lab 6 Objectives

- Understand code coverage.
- Understand branch coverage.
- Write test cases for Python functions.
- Identify untested statements and branches.
- Improve test coverage through additional test cases.

### Note

Keep all Lab 6 files and work inside the `Lab 6` folder. Lab 7 (Fuzz Testing) is maintained separately in the `Lab 7` folder.
