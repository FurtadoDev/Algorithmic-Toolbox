import unittest
from maximum_loot import maximum_loot_value


class TestMaximumLoot(unittest.TestCase):
    def test(self):
        for (capacity, weights, prices, answer) in [
            (50, [20, 50, 30], [60, 100, 120], 180.0),
            (10, [30], [500], 500/3),
            (500, [50, 150, 200, 100], [100, 200, 200, 150], 650)
        ]:
            self.assertAlmostEqual(
                maximum_loot_value(capacity, weights, prices),
                answer,
                delta=1e-03
            )


if __name__ == '__main__':
    unittest.main()
