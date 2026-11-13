
from hypothesis import given, strategies as st
from daycare_fees import (
    parse_enrolment,
    hours_average,
    payable_fee
)


# Test 1: Enrolment fuzz testing
@given(st.text() | st.none())
def test_parse_enrolment_no_crash(s):
    try:
        parse_enrolment(s)
    except (ValueError, TypeError, AttributeError):
        pass


# Test 2: Weekly hours fuzz testing
@given(st.text() | st.none())
def test_hours_average_no_crash(s):
    try:
        hours_average(s)
    except (ValueError, TypeError, AttributeError):
        pass


# Test 3: Payable fee fuzz testing
@given(st.text() | st.none())
def test_payable_fee_no_crash(s):
    try:
        payable_fee(s)
    except (ValueError, TypeError, AttributeError):
        pass
