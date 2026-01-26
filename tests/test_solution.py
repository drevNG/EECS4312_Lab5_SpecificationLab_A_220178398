"""
Public test suite for the meeting slot suggestion exercise.

Students can run these tests locally to check basic correctness of their implementation.
The hidden test suite used for grading contains additional edge cases and will not be
available to students.
"""
import importlib
import inspect
import pytest

solution = importlib.import_module("solution")


def test_no_events_returns_sorted_list():
    """No events: the result should be a non-empty, sorted list."""
    result = solution.suggest_slots([], 30, "Mon")
    assert isinstance(result, list), "Result should be a list"
    assert result == sorted(result), "Returned slots should be sorted"
    assert len(result) > 0, "There should be at least one available slot"


def test_lunch_break_excluded():
    """Slots should not include times during the lunch hour."""
    result = solution.suggest_slots([], 30, "Tue")
    assert "12:00" not in result, "12:00 should not be offered as a start time"
    assert "12:30" not in result, "12:30 should not be offered as a start time"


def test_overlap_event_removed():
    """Slots should not overlap an existing event."""
    events = [{"start": "10:00", "end": "10:30"}]
    result = solution.suggest_slots(events, 30, "Wed")
    assert all(not (slot >= "10:00" and slot < "10:30") for slot in result), "Slots must not overlap existing events"


def test_friday_rule_respected():
    """On Fridays, the last meeting must start no later than 15:00."""
    result = solution.suggest_slots([], 60, "Fri")
    for slot in result:
        hour, minute = map(int, slot.split(":"))
        assert hour < 15 or (hour == 15 and minute == 0), "Friday meetings must start by 15:00"

""" TODO: Add at least 10 additional test cases to test your implementation."""
