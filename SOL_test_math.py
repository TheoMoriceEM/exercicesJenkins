import unittest

import mymath



class TestSum(unittest.TestCase):

    def test_add(self):
        """
        Verifie que l'addition fonctionne correctement
        """
        self.assertEqual(mymath.add(1,2), 3)
        self.assertEqual(mymath.add(2,1), 3)
        self.assertEqual(mymath.add(5.7,2), 7.7)
        self.assertEqual(mymath.add(3.7,2.3), 6.0)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            mymath.add('a',1)
            mymath.add(3,'b')
            mymath.add('1','3')

    def test_substract(self):
        """
        Verifie que la soustraction fonctionne correctement
        """
        self.assertEqual(mymath.substract(1,2), -1)
        self.assertEqual(mymath.substract(2,1), 1)
        self.assertEqual(mymath.substract(5.7,2), 3.7)
        # AssertionError: 1.4000000000000004 != 1.4
        # probleme de test ou de code ?
        # https://docs.python.org/3/tutorial/floatingpoint.html
        self.assertAlmostEqual(mymath.substract(3.7,2.3), 1.4)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            mymath.substract('a',1)
            mymath.substract(3,'b')
            mymath.substract('1','3')

    def test_multiply(self):
        """
        Verifie que la multiplication fonctionne
        """
        self.assertEqual(mymath.multiply(4,2), 8)
        self.assertEqual(mymath.multiply(-2,-4), 8)
        self.assertEqual(mymath.multiply(-1.2,2), -2.4)
        self.assertEqual(mymath.multiply(1.2,-5.5), -6.6)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            mymath.multiply('a',1)
            mymath.multiply(3,'b')
            mymath.multiply('1','3')

    def test_divide(self):
        """
        Verifie que la division fonctionne
        """
        self.assertEqual(mymath.divide(4,2), 2)
        self.assertEqual(mymath.divide(2,4), 0.5)
        self.assertEqual(mymath.divide(-1.2,2), -0.6)
        self.assertAlmostEqual(mymath.divide(-1.2,-5.5), 0.2181818)

        self.assertRaises(ValueError, mymath.divide, 4, 0)
        # une autre maniere d'ecrire cette instruction
        with self.assertRaises(ValueError):
            mymath.divide(4, 0)

        # on s'assure que la fonction leve une erreur pour les types differents
        with self.assertRaises(TypeError):
            mymath.substract('a',1)
            mymath.substract(3,'b')
            mymath.substract('1','3')

if __name__ == '__main__':
    unittest.main()
