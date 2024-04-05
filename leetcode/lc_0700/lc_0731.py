from bisect import bisect


class MyCalendarTwo:
    def __init__(self):
        self.events: list[(int, int)] = []
        self.double_booked_slots: list[(int, int)] = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double_booked_slots:
            if s < end and e > start:
                return False
        # Update double_booked_slots
        for s, e in self.events:
            overlap_start, overlap_end = max(start, s), min(end, e)
            if overlap_end > overlap_start:
                self.double_booked_slots.append((overlap_start, overlap_end))
        self.events.append((start, end))
        return True


class MyCalendarTwoSortedList:
    def __init__(self):
        self.events_by_start: list[(int, int)] = []
        self.events_by_end: list[(int, int)] = []

    def book(self, start: int, end: int) -> bool:
        start_before_index = bisect(self.events_by_start, end, key=lambda i: i[0])
        # Add all events that starts before current event ends
        end_after_index = bisect(self.events_by_end, start, key=lambda i: i[1])
        candidate_events_by_start = self.events_by_start[:start_before_index]
        candidate_events_by_end = self.events_by_end[end_after_index:]
        candidate_events = [
            i for i in candidate_events_by_start if i in candidate_events_by_end
        ]

        overlaps: list[(int, int)] = []
        for s, e in candidate_events:
            overlaps.append((max(start, s), min(end, e)))
        # Sort overlaps by start time
        overlaps.sort(key=lambda i: i[0])
        # If there's any overlap between any two items in overlaps array,
        # (start, end) is a triple booked event
        for i in range(len(overlaps) - 1):
            if overlaps[i][1] > overlaps[i + 1][0]:
                return False
        # No triple booked scenario found, insert this event
        start_position = bisect(self.events_by_start, start, key=lambda i: i[0])
        end_position = bisect(self.events_by_end, start, key=lambda i: i[1])
        self.events_by_start.insert(start_position, (start, end))
        self.events_by_end.insert(end_position, (start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
