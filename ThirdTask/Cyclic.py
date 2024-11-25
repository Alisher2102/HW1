import numpy as np
import unittest

def time_to_cyclic_features(hour):
    radians = 2 * np.pi * hour / 24
    return np.sin(radians), np.cos(radians)

def cyclic_time_difference(hour1, hour2):
    sin1, cos1 = time_to_cyclic_features(hour1)
    sin2, cos2 = time_to_cyclic_features(hour2)
    angle_diff = np.arctan2(sin2 - sin1, cos2 - cos1)
    return abs(angle_diff * 24 / (2 * np.pi))

class TestCyclicTimeFeatures(unittest.TestCase):
    def test_time_to_cyclic_features(self):
        hour = 6
        sin_val, cos_val = time_to_cyclic_features(hour)
        self.assertAlmostEqual(sin_val, 0.5, places=2)
        self.assertAlmostEqual(cos_val, np.sqrt(3)/2, places=2)

    def test_cyclic_time_difference_direct(self):
        diff = cyclic_time_difference(23, 1)
        self.assertAlmostEqual(diff, 2, places=1)

    def test_cyclic_time_difference_no_wraparound(self):
        diff = cyclic_time_difference(10, 14)
        self.assertAlmostEqual(diff, 4, places=1)

    def test_cyclic_time_difference_wraparound(self):
        diff = cyclic_time_difference(22, 2)
        self.assertAlmostEqual(diff, 4, places=1)

    def test_cyclic_time_difference_same_time(self):
        diff = cyclic_time_difference(5, 5)
        self.assertEqual(diff, 0)

    def test_time_to_cyclic_features_boundaries(self):
        sin_0, cos_0 = time_to_cyclic_features(0)
        self.assertAlmostEqual(sin_0, 0, places=1)
        self.assertAlmostEqual(cos_0, 1, places=1)
        sin_24, cos_24 = time_to_cyclic_features(24)
        self.assertAlmostEqual(sin_24, 0, places=1)
        self.assertAlmostEqual(cos_24, 1, places=1)

if __name__ == '__main__':
    unittest.main()
