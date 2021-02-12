import unittest

import SOL_mymath



class TestSum(unittest.TestCase):

    def test_add(self):
        """
        Verifie que l'addition fonctionne correctement
        """
        self.assertEqual(SOL_mymath.add(1,2), 3)
        self.assertEqual(SOL_mymath.add(2,1), 3)
        self.assertEqual(SOL_mymath.add(5.7,2), 7.7)
        self.assertEqual(SOL_mymath.add(3.7,2.3), 6.0)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            SOL_mymath.add('a',1)
            SOL_mymath.add(3,'b')
            SOL_mymath.add('1','3')

    def test_substract(self):
        """
        Verifie que la soustraction fonctionne correctement
        """
        self.assertEqual(SOL_mymath.substract(1,2), -1)
        self.assertEqual(SOL_mymath.substract(2,1), 1)
        self.assertEqual(SOL_mymath.substract(5.7,2), 3.7)
        # AssertionError: 1.4000000000000004 != 1.4
        # probleme de test ou de code ?
        # https://docs.python.org/3/tutorial/floatingpoint.html
        self.assertAlmostEqual(SOL_mymath.substract(3.7,2.3), 1.4)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            SOL_mymath.substract('a',1)
            SOL_mymath.substract(3,'b')
            SOL_mymath.substract('1','3')

    def test_multiply(self):
        """
        Verifie que la multiplication fonctionne
        """
        self.assertEqual(SOL_mymath.multiply(4,2), 8)
        self.assertEqual(SOL_mymath.multiply(-2,-4), 8)
        self.assertEqual(SOL_mymath.multiply(-1.2,2), -2.4)
        self.assertEqual(SOL_mymath.multiply(1.2,-5.5), -6.6)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            SOL_mymath.multiply('a',1)
            SOL_mymath.multiply(3,'b')
            SOL_mymath.multiply('1','3')

    def test_divide(self):
        """
        Verifie que la division fonctionne
        """
        self.assertEqual(SOL_mymath.divide(4,2), 2)
        self.assertEqual(SOL_mymath.divide(2,4), 0.5)
        self.assertEqual(SOL_mymath.divide(-1.2,2), -0.6)
        self.assertAlmostEqual(SOL_mymath.divide(-1.2,-5.5), 0.2181818)

        self.assertRaises(ValueError, SOL_mymath.divide, 4, 0)
        # une autre maniere d'ecrire cette instruction
        with self.assertRaises(ValueError):
            SOL_mymath.divide(4, 0)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            SOL_mymath.substract('a',1)
            SOL_mymath.substract(3,'b')
            SOL_mymath.substract('1','3')

if __name__ == '__main__':
    unittest.main()
