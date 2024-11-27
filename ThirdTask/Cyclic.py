import numpy as np
import unittest

def time_to_cyclic_features(hour):
    """Convert an hour (0-24) into cyclic sine and cosine features."""
    hour = hour % 24  # Normalize hour to [0, 24)
    radians = 2 * np.pi * hour / 24
    return np.sin(radians), np.cos(radians)

def cyclic_time_difference(hour1, hour2):
    """
    Calculate the shortest cyclic time difference (in hours) between two times.
    Handles wraparound by considering the cyclic nature of time.
    """
    diff = abs(hour1 - hour2) % 24  # Ensure difference is in [0, 24)
    return min(diff, 24 - diff)  # Shortest path around the clock

class TestCyclicTimeFeatures(unittest.TestCase):
    def test_time_to_cyclic_features(self):
        # Test a common hour
        hour = 6
        sin_val, cos_val = time_to_cyclic_features(hour)
        self.assertAlmostEqual(sin_val, 0.5, places=2)
        self.assertAlmostEqual(cos_val, np.sqrt(3)/2, places=2)

    def test_cyclic_time_difference_direct(self):
        # Test direct difference without wraparound
        diff = cyclic_time_difference(23, 1)
        self.assertAlmostEqual(diff, 2, places=1)

    def test_cyclic_time_difference_no_wraparound(self):
        # Test difference without crossing 24-hour boundary
        diff = cyclic_time_difference(10, 14)
        self.assertAlmostEqual(diff, 4, places=1)

    def test_cyclic_time_difference_wraparound(self):
        # Test difference crossing 24-hour boundary
        diff = cyclic_time_difference(22, 2)
        self.assertAlmostEqual(diff, 4, places=1)

    def test_cyclic_time_difference_same_time(self):
        # Test no difference
        diff = cyclic_time_difference(5, 5)
        self.assertEqual(diff, 0)

    def test_time_to_cyclic_features_boundaries(self):
        # Test boundaries at 0 and 24 hours
        sin_0, cos_0 = time_to_cyclic_features(0)
        self.assertAlmostEqual(sin_0, 0, places=1)
        self.assertAlmostEqual(cos_0, 1, places=1)
        sin_24, cos_24 = time_to_cyclic_features(24)
        self.assertAlmostEqual(sin_24, 0, places=1)
        self.assertAlmostEqual(cos_24, 1, places=1)

    def test_cyclic_time_difference_large_values(self):
        # Test large input values
        diff = cyclic_time_difference(25, -1)
        self.assertAlmostEqual(diff, 2, places=1)

    def test_time_to_cyclic_features_large_values(self):
        # Test large and negative values
        sin_large, cos_large = time_to_cyclic_features(49)
        sin_neg, cos_neg = time_to_cyclic_features(-1)
        self.assertAlmostEqual(sin_large, sin_neg, places=2)
        self.assertAlmostEqual(cos_large, cos_neg, places=2)

if __name__ == '__main__':
    unittest.main()
