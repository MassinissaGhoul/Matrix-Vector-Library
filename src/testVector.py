import unittest
from Vector import Vector  # Assurez-vous que le fichier s'appelle bien Vector.py

class TestVector(unittest.TestCase):
    def test_push_back(self):
        v = Vector([1, 2, 3])
        v.push_back(4)
        self.assertEqual(v.elements, [1, 2, 3, 4])

    def test_add_vector(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = v1 + v2
        self.assertEqual(v3.elements, [5, 7, 9])

    def test_sub_vector(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = v1 - v2
        self.assertEqual(v3.elements, [-3, -3, -3])

    def test_multiply_vector(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = v1 * v2
        self.assertEqual(v3.elements, [4, 10, 18])

    def test_scalar_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 @ v2, 32)

    def test_are_orthogonal(self):
        # Test avec des vecteurs orthogonaux
        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        self.assertTrue(v1.are_orthogonal(v2))

        # Test avec des vecteurs non orthogonaux
        v3 = Vector([1, 2])
        v4 = Vector([3, 4])
        self.assertFalse(v3.are_orthogonal(v4))

        # Test avec des vecteurs de tailles incompatibles (doit lever une ValueError)
        v5 = Vector([1, 0, 0])
        v6 = Vector([0, 1])
        with self.assertRaises(ValueError):
            v5.are_orthogonal(v6)

    # Tests pour les opérateurs en place
    def test_iadd(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v1 += v2
        self.assertEqual(v1.elements, [5, 7, 9])

    def test_isub(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v1 -= v2
        self.assertEqual(v1.elements, [-3, -3, -3])

    def test_imul(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v1 *= v2
        self.assertEqual(v1.elements, [4, 10, 18])

    def test_add_vector_incompatible_sizes(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5])
        with self.assertRaises(ValueError):
            val = v1 + v2

if __name__ == '__main__':
    unittest.main()
