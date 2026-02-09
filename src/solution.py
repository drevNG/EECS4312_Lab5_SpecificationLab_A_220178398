## Student Name: Evan Gocool
## Student ID: 220178398

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict


# Helper functions
def _time_to_minutes(t: str) -> int:
    """Convert 'HH:MM' to minutes since midnight."""
    hours, minutes = map(int, t.split(":"))
    return hours * 60 + minutes


def _minutes_to_time(m: int) -> str:
    """Convert minutes since midnight to 'HH:MM'."""
    hours = m // 60
    minutes = m % 60
    return f"{hours:02d}:{minutes:02d}"

def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    """
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Three-letter day abbreviation (e.g., "Mon", "Tue", ... "Fri")

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """
    # TODO: Implement this function
    #raise NotImplementedError("suggest_slots function has not been implemented yet")
    
    

    
    WORK_START_TIME = _time_to_minutes("09:00")
    WORK_END_TIME = _time_to_minutes("17:00")
    SLOT_INCREMENT = 15  # minutes

    # Add lunch break as a fixed busy interval
    LUNCH_START = _time_to_minutes("12:00")
    LUNCH_END = _time_to_minutes("13:00")

    # Convert events to minute ranges
    busy_intervals = []
    for event in events:
        busy_intervals.append((
            _time_to_minutes(event["start"]),
            _time_to_minutes(event["end"])
        ))

    # Include lunch break
    busy_intervals.append((LUNCH_START, LUNCH_END))

    busy_intervals.sort()

    valid_slots = []
    start = WORK_START_TIME
    latest_start = WORK_END_TIME - meeting_duration

    while start <= latest_start:
        end = start + meeting_duration

        # new req (no starting after 15:00 on friday)
        if day == "Fri" and start > _time_to_minutes("15:00"):
            start += SLOT_INCREMENT
            continue

        overlaps = False
        for busy_start, busy_end in busy_intervals:
            if start < busy_end and end > busy_start:
                overlaps = True
                break

        if not overlaps:
            valid_slots.append(_minutes_to_time(start))

        start += SLOT_INCREMENT

    return valid_slots
