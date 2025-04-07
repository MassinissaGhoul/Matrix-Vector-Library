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

    def test_gauss(self):
        # Test de la méthode gauss sur un système simple :
        #   2x + y = 5
        #   x - y = 1
        # Solution attendue : x = 2, y = 1
        tableau = [
            [2, 1, 5],
            [1, -1, 1]
        ]
        # Utilisation d'une instance dummy pour appeler gauss (la méthode est membre de Matrix)
        dummy = Matrix([[0]])
        dummy.gauss(tableau)
        self.assertAlmostEqual(tableau[0][-1], 2)
        self.assertAlmostEqual(tableau[1][-1], 1)

    def test_simplex(self):
        # Test du simplex pour le problème de maximisation suivant :
        # Maximiser z = 3x₁ + 2x₂
        # sous les contraintes :
        #    x₁ + x₂ <= 4
        #    x₁ <= 2
        #    x₂ <= 3
        # avec x₁, x₂ >= 0
        # La solution optimale attendue est x₁ = 2, x₂ = 2 et z = 10.
        A = Matrix([[1, 1],
                    [1, 0],
                    [0, 1]])
        b = Vector([4, 2, 3])
        c = Vector([3, 2])
        sol, opt_val = A.simplex(b, c)
        self.assertAlmostEqual(sol.elements[0], 2)
        self.assertAlmostEqual(sol.elements[1], 2)
        self.assertAlmostEqual(opt_val, 10)

if __name__ == '__main__':
    unittest.main()
