import numpy as np
import unittest

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_score(threat_scores):
    return np.mean(threat_scores)

def calculate_aggregated_score(department_scores, importance_weights):
    weighted_sum = sum(score * weight for score, weight in zip(department_scores, importance_weights))
    total_weight = sum(importance_weights)
    return weighted_sum / total_weight if total_weight else 0

class TestAggregatedUserThreatScore(unittest.TestCase):
    def test_calculate_department_score(self):
        scores = [15, 25, 35, 45, 55]
        self.assertEqual(calculate_department_score(scores), 35)

    def test_calculate_aggregated_score_equal_importance(self):
        scores = [20, 30, 40, 50, 60]
        weights = [1, 1, 1, 1, 1]
        self.assertEqual(calculate_aggregated_score(scores, weights), 40)

    def test_calculate_aggregated_score_varying_importance(self):
        scores = [10, 30, 50, 70, 90]
        weights = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(calculate_aggregated_score(scores, weights), 63.33, places=2)

    def test_generate_random_data(self):
        data = generate_random_data(30, 10, 50)
        self.assertTrue((data >= 20).all() and (data <= 40).all())

    def test_functional_case_1(self):
        scores = [generate_random_data(30, 5, 100) for _ in range(5)]
        dept_scores = [calculate_department_score(s) for s in scores]
        importance = [1] * 5
        agg_score = calculate_aggregated_score(dept_scores, importance)
        self.assertTrue(0 <= agg_score <= 90)

    def test_functional_case_2(self):
        scores = [
            generate_random_data(60, 10, 150),
            generate_random_data(20, 5, 50),
            generate_random_data(40, 8, 75),
            generate_random_data(25, 10, 20),
            generate_random_data(35, 15, 200),
        ]
        dept_scores = [calculate_department_score(s) for s in scores]
        importance = [5, 1, 3, 2, 4]
        agg_score = calculate_aggregated_score(dept_scores, importance)
        self.assertTrue(0 <= agg_score <= 90)

    def test_functional_case_3(self):
        scores = [
            generate_random_data(5, 2, 80),
            generate_random_data(10, 2, 60),
            generate_random_data(8, 3, 100),
            generate_random_data(5, 2, 50),
            generate_random_data(7, 2, 120),
        ]
        dept_scores = [calculate_department_score(s) for s in scores]
        importance = [3, 2, 1, 4, 5]
        agg_score = calculate_aggregated_score(dept_scores, importance)
        self.assertTrue(0 <= agg_score <= 90)

if __name__ == '__main__':
    unittest.main()
