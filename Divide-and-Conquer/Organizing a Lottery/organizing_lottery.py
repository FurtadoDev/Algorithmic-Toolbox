# python3
from sys import stdin
from math import floor
from bisect import bisect_left, bisect_right
from collections import namedtuple

sorted_starts = []
sorted_ends = []


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


# Solution 1
# def points_cover(starts, ends, points):
#     Event = namedtuple('Event', ['coordinate', 'type', 'index'])
#     starts_size = len(starts)
#     ends_size = starts_size
#     points_size = len(points)
#     events_size = starts_size + ends_size + points_size
#     events = []
#     solution_counts = [None] * points_size
#     # Append starts and ends
#     for i in range(0, starts_size):
#         events.append(Event(coordinate=starts[i], type='l', index=i))
#         events.append(Event(coordinate=ends[i], type='r', index=i))
#     # Append points
#     for i in range(0, points_size):
#         events.append(Event(coordinate=points[i], type='p', index=i))
#
#     # sort points such that it is arranged as l < p < r when all points fall on the same coordinate
#     sorted_events = sorted(events)
#     no_segments = 0
#     for i in range(0, events_size):
#         if sorted_events[i].type == 'l':
#             no_segments += 1
#         if sorted_events[i].type == 'r':
#             no_segments -= 1
#         if sorted_events[i].type == 'p':
#             solution_counts[sorted_events[i].index] = no_segments
#     print(solution_counts)
#     return solution_counts

# Solution 2 : Using Divide and Conquer Approach
def points_cover(starts, ends, points):
    global sorted_starts
    global sorted_ends

    sorted_starts = sorted(starts)
    sorted_ends = sorted(ends)
    num_points = len(points)
    num_segments = len(starts)

    answer_segments_cover = []
    for i in range(0, num_points):
        num_lesser_segments = get_lesser_segments(0, num_segments-1, points[i])
        num_greater_segments = get_greater_segments(0, num_segments-1, points[i])
        num_segments_covering_point = num_segments - (num_lesser_segments + num_greater_segments)
        answer_segments_cover.append(num_segments_covering_point)

    return answer_segments_cover


# get the no of segments that are less than query point using sorted ends
def get_lesser_segments(l_idx, r_idx, query_point):
    global sorted_ends
    num_segments_before_query = 0
    low_idx = l_idx
    high_idx = r_idx
    if l_idx == r_idx == 0:
        if sorted_ends[0] < query_point:
            num_segments_before_query = 1
        else:
            num_segments_before_query = 0
    else:
        while low_idx != high_idx:
            mid_idx = floor((low_idx + high_idx)/2)
            if sorted_ends[mid_idx] >= query_point:
                high_idx = mid_idx
            else:
                low_idx = mid_idx + 1

        if low_idx == 0:
            num_segments_before_query = 0
        elif low_idx == (len(sorted_ends) - 1) and sorted_ends[low_idx] < query_point:
            num_segments_before_query = low_idx + 1
        else:
            num_segments_before_query = low_idx

    return num_segments_before_query


# get the no of segments that are greater than query point using sorted starts
def get_greater_segments(l_idx, r_idx, query_point):
    global sorted_starts
    num_segments_after_query = 0
    low_idx = l_idx
    high_idx = r_idx
    if l_idx == r_idx == 0:
        if sorted_starts[0] > query_point:
            num_segments_after_query = 1
        else:
            num_segments_after_query = 0
    else:
        while low_idx != high_idx:
            mid_idx = floor((low_idx + high_idx)/2)
            if sorted_starts[mid_idx] <= query_point:
                low_idx = mid_idx + 1
            else:
                high_idx = mid_idx

        if low_idx == 0:
            num_segments_after_query = len(sorted_starts)
        elif low_idx == (len(sorted_starts) - 1) and sorted_starts[low_idx] <= query_point:
            num_segments_after_query = 0
        else:
            num_segments_after_query = len(sorted_starts) - low_idx

    return num_segments_after_query


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)





