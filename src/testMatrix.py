import unittest
from Matrix import Matrix
from Vector import Vector

class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        self.m2 = Matrix([[7, 8, 9], [10, 11, 12]])
        self.m3 = Matrix([[2, 3], [5, 6]])
        self.m4 = Matrix([[1, 1], [1, 1]])

    def test_addition(self):
        result = self.m1 + self.m2
        expected = Matrix([[8, 10, 12], [14, 16, 18]])
        self.assertEqual(str(result), str(expected))

    def test_subtraction(self):
        result = self.m2 - self.m1
        expected = Matrix([[6, 6, 6], [6, 6, 6]])
        self.assertEqual(str(result), str(expected))

    def test_invalid_addition(self):
        with self.assertRaises(ValueError):
            _ = self.m1 + self.m3

    def test_multiplication(self):
        mA = Matrix([[1, 2], [3, 4]])
        mB = Matrix([[2, 0], [1, 2]])
        result = mA * mB
        expected = Matrix([[4, 4], [10, 8]])
        self.assertEqual(str(result), str(expected))

    def test_invalid_multiplication(self):
        with self.assertRaises(ValueError):
            _ = self.m1 * self.m3

    def test_get_column(self):
        column = self.m1.get_column(1)
        self.assertEqual(column, [2, 5])


    def test_solve(self):
        A = Matrix([[2, 1, -1],
                    [-3, -1, 2],
                    [-2, 1, 2]])
        b = Vector([8, -11, -3])
        solution = A.solve(b)
        expected = Vector([2, 3, -1])
        # Comparaison avec tolérance pour éviter les problèmes d'arrondi
        for sol_val, exp_val in zip(solution.elements, expected.elements):
            self.assertAlmostEqual(sol_val, exp_val)

    def test_non_square_solve(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        b = Vector([1, 2])
        with self.assertRaises(ValueError):
            _ = m.solve(b)

    def test_invalid_init(self):
        with self.assertRaises(ValueError):
            _ = Matrix([[1, 2], [3, 4, 5]])

if __name__ == '__main__':
    unittest.main()
