# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')

sorted_x = []
sorted_y = []


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))
    return min_distance_squared


def minimum_distance_squared(points):
    global sorted_x
    global sorted_y
    sorted_x = sorted(points, key=lambda item: item.x)
    sorted_y = sorted(points, key=lambda item: item.y)
    # print(sorted_x)
    # print(sorted_y)
    # print(len(sorted_x))
    overall_min_dist = closest_pair(int(0), int(len(sorted_x) - 1))
    return overall_min_dist


def closest_pair(left_idx, right_idx):
    global sorted_x
    global sorted_y
    min_overall_dist_squared = float("inf")
    if (right_idx - left_idx + 1) <= 3:
        # implement the base case here using brute force
        min_overall_dist_squared = minimum_distance_squared_naive(sorted_x[left_idx:right_idx + 1])
    else:
        mid_idx = int((right_idx + left_idx)/2)
        min_left_dist_squared = closest_pair(left_idx, mid_idx)
        min_right_dist_squared = closest_pair(mid_idx + 1, right_idx)
        min_split_dist_squared = closest_split_pair(mid_idx, min(min_left_dist_squared, min_right_dist_squared))
        min_overall_dist_squared = min(min_left_dist_squared, min_right_dist_squared, min_split_dist_squared)

    return min_overall_dist_squared


def closest_split_pair(mid_idx, min_dist_squared):
    global sorted_x
    global sorted_y
    closest_split_pair_distance_squared = float("inf")

    # append elements to the the filtered_strip
    length_sorted_y = len(sorted_y)
    filtered_strip = []
    left_limit = sorted_x[mid_idx].x - sqrt(min_dist_squared)
    right_limit = sorted_x[mid_idx].x + sqrt(min_dist_squared)
    for i in range(0, length_sorted_y):
        if (sorted_y[i].x > left_limit) and (sorted_y[i].x < right_limit):
            filtered_strip.append(sorted_y[i])

    # get the closest distance between a split pair if it exists
    for i in range(1, len(filtered_strip) + 1):
        for j in range(1, min(7 + 1, len(filtered_strip) - i + 1)):
            temp_dist = distance_squared(filtered_strip[i - 1], filtered_strip[i + j - 1])
            if temp_dist < closest_split_pair_distance_squared:
                closest_split_pair_distance_squared = temp_dist

    return closest_split_pair_distance_squared


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
