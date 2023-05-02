def minimum_meeting_rooms(meetings: list[tuple[int]]):
    # Create a list of "events" for meeting starts and ends
    events: list[tuple[str, int]] = []
    for m in meetings:
        events.append(("start", m[0]))
        events.append(("end", m[1]))
    # Sort events in chronological order ("end" events come before "start" events)
    events.sort(key=lambda e: (e[1], e[0]))
    # The number of rooms needed at one point in time
    current_rooms: int = 0
    # The maximum number of rooms needed at any point
    max_rooms: int = current_rooms
    # Iterate through events and update current_rooms
    for e in events:
        if e[0] == "start":
            current_rooms += 1
            if current_rooms > max_rooms:
                max_rooms = current_rooms
        elif e[0] == "end":
            current_rooms -= 1
    # The minimum number of rooms needed is the maximum number of rooms needed at any point in time
    return max_rooms

if __name__ == "__main__":
    print(minimum_meeting_rooms([(1, 4), (2, 8),(3, 7)]))
