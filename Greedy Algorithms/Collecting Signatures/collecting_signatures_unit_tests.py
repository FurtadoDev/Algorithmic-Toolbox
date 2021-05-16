import unittest
from collecting_signatures import compute_optimal_points, Segment


class CollectingSignatures(unittest.TestCase):
    def test(self):
        for (segments, answer) in [
            ([Segment(1, 3), Segment(2, 5), Segment(3, 6)], 1),
            ([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)], 2),
            ([Segment(1, 3), Segment(4, 15), Segment(6, 13), Segment(8, 12), Segment(5, 7), Segment(16, 20)], 4)
        ]:
            self.assertEqual(len(compute_optimal_points(segments)), answer)


if __name__ == '__main__':
    unittest.main()
