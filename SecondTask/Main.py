import numpy as np
import unittest

# Function to generate random data for threat scores
def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

# Function to calculate the average threat score for a department
def calculate_department_score(threat_scores):
    return np.mean(threat_scores)

# Class to test threat score calculations
class TestThreatScore(unittest.TestCase):
    def test_calculate_department_score(self):
        scores = [15, 25, 35, 45, 55]
        self.assertEqual(calculate_department_score(scores), 35)

    def test_generate_random_data(self):
        data = generate_random_data(30, 10, 50)
        self.assertTrue((data >= 20).all() and (data <= 40).all())

    def test_functional_case_same_scores(self):
        # All departments have similar threat scores
        scores = [generate_random_data(30, 5, 50) for _ in range(5)]
        dept_scores = [calculate_department_score(s) for s in scores]
        self.assertTrue(all(abs(s - dept_scores[0]) < 5 for s in dept_scores))  # Similar scores

    def test_functional_case_high_department_score(self):
        # One department has a high score
        scores = [
            generate_random_data(30, 5, 50),  # Normal department
            generate_random_data(30, 5, 50),  # Normal department
            generate_random_data(70, 10, 50),  # High score department
            generate_random_data(30, 5, 50),  # Normal department
            generate_random_data(30, 5, 50)   # Normal department
        ]
        dept_scores = [calculate_department_score(s) for s in scores]
        self.assertTrue(max(dept_scores) > 60)  # High score should be > 60

    def test_functional_case_high_individual_scores(self):
        # All departments have the same mean, but one has outliers
        scores = [
            generate_random_data(30, 5, 50),
            generate_random_data(30, 5, 50),
            generate_random_data(30, 5, 48).tolist() + [90, 90],  # Outliers in this department
            generate_random_data(30, 5, 50),
            generate_random_data(30, 5, 50)
        ]
        dept_scores = [calculate_department_score(s) for s in scores]
        high_score_dept = scores[2]
        self.assertTrue(np.mean(high_score_dept) > 30)  # Mean affected by outliers
        self.assertTrue(len([x for x in high_score_dept if x > 80]) > 0)  # Outliers present

    def test_functional_case_different_user_counts(self):
        # Departments with different user counts
        scores = [
            generate_random_data(30, 5, 50),  # Department 1
            generate_random_data(40, 5, 100),  # Department 2
            generate_random_data(35, 10, 20),  # Department 3
            generate_random_data(25, 5, 80),  # Department 4
            generate_random_data(50, 10, 60)  # Department 5
        ]
        dept_scores = [calculate_department_score(s) for s in scores]
        self.assertEqual(len(dept_scores), 5)  # Correct number of departments
        self.assertTrue(all(0 <= s <= 90 for s in dept_scores))  # Valid scores

if __name__ == '__main__':
    unittest.main()
