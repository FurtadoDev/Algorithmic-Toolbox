# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key=lambda x: x.end)
    points = []
    segments_size = len(segments)
    current_min = -1
    for i in range(0, segments_size):
        if segments[i].start > current_min:
            current_min = segments[i].end
            points.append(current_min)

    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
