import unittest

from poo import Personne


class TestSum(unittest.TestCase):

    def test_creation_compte(self):
        """
        Verifie que la creation d'un compte fonctionne
        """
        personne = Personne('Jean','Jacques')
        personne.creer_compte_bancaire()

        self.assertEqual(personne.compte_bancaire.solde, 0)
    def test_depot_compte(self):
        personne = Personne('Jean','Jacques')
        personne.creer_compte_bancaire()
        personne.depot(1000)
        self.assertEqual(personne.compte_bancaire.solde, 1000)

    def test_retrait_compte(self):
        personne = Personne('Jean','Jacques')
        personne.creer_compte_bancaire()
        personne.retrait(20)
        self.assertEqual(personne.compte_bancaire.solde, -20)

if __name__ == '__main__':
    unittest.main()
