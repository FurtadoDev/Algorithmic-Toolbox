import unittest
import numpy as np
from organizing_lottery import points_cover, points_cover_naive
from numpy.random import seed
from numpy.random import randint


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([-10], [10], [-100, 100, 0]),
            ([0, -3, 7], [5, 2, 10], [1, 6])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        seed(1)
        a = randint(0, 10, 15)
        b = randint(10, 20, 15)
        c = randint(0, 35, 10)
        for starts, ends, points in [
            (a, b, c)
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_large(self):
        seed(1)
        a = randint(0, 100, 50)
        b = randint(100, 200, 50)
        c = randint(-50, 300, 20)
        for starts, ends, points in [
            (a, b, c)
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))


if __name__ == '__main__':
    unittest.main()
