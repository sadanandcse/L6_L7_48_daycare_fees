# L6_L7_48 — Daycare Fees

## Lab 7: Fuzz Testing

### About

A small Python module that parses enrolment details, calculates average weekly hours, and works out the payable fee after applying a discount.

### Files

| File | Description |
|---|---|
| `daycare_fees.py` | Python module under test |
| `test_daycare_fees.py` | Hypothesis-based fuzz testing file |

### Testing

Install the required packages:

```bash
python -m pip install pytest hypothesis
```

Run the Lab 7 fuzz tests:

```bash
python -m pytest -v --import-mode=importlib test_daycare_fees.py
```

### Lab 7 Objectives

- Understand fuzz testing.
- Generate different inputs automatically using Hypothesis.
- Test functions with valid and invalid inputs.
- Identify unexpected errors and input-handling issues.
- Improve the reliability of Python functions.

### Test Results

The Lab 7 test file contains three fuzz-testing tests:

1. `test_parse_enrolment_no_crash`
2. `test_hours_average_no_crash`
3. `test_payable_fee_no_crash`

### Evidence

The following screenshots are included as testing evidence:

- `Lab7_Before_Testing.png`
- `Lab7_After_Testing.png`

### Note

Keep all Lab 7 files and screenshots inside the `Lab 7` folder. Lab 6 work is maintained separately in the `Lab 6` folder.
