import unittest

import poo


personne = poo.Personne("Jean", "Truc")

class TestPoo(unittest.TestCase):

    def test_creer_compte(self):
        personne.creer_compte_bancaire()
        solde = personne.compte_bancaire.solde
        self.assertEqual(solde, 0)

    def test_depot(self):
        personne.depot(1000)
        solde = personne.compte_bancaire.solde
        self.assertEqual(solde, 1000)

    def test_retrait(self):
        personne.retrait(500)
        solde = personne.compte_bancaire.solde
        self.assertEqual(solde, 500)
        
if __name__ == '__main__':
    unittest.main()