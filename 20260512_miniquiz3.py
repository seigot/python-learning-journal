activities = [
    (0, 3, "A"),
    (1, 2, "B"),
    (3, 5, "C"),
    (0, 1, "D"),
    (3, 4, "E"),
    (4, 5, "F"),
    (2, 3, "G"),
]

def solve(activities):
    activities.sort(key=lambda x: x[1])  # sort by end time
    result = []
    current_end = 0
    for start, end, name in activities:
        if start >= current_end:
            result.append((name, start, end))
            current_end = end
    return result
print(solve(activities))
