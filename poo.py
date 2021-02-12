class Personne:
    """docstring for Personne."""

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.compte_bancaire = None

    def creer_compte_bancaire(self):
        self.compte_bancaire = CompteBancaire(self.nom)

    def depot(self, somme):
        self.compte_bancaire.depot(somme)
    def solde(self):
        self.compte_bancaire.affiche();
    def retrait(self,somme):
        self.compte_bancaire.retrait(somme)

class CompteBancaire:

    def __init__(self,nom='Dupont'):
        """ creation du constructeur de la classe avec les valeurs par defaut 'Dupont' et 0 """
        self.nom=nom
        self.solde=0

    def depot(self,somme):
        """ ajout d'une somme a l'attribut solde """

        self.solde+=somme

    def retrait(self,somme):
        """ retrait d'une somme a l'attribut solde """

        self.solde-=somme

    def affiche(self):
        """ L'affichage des informations d'un compte"""

        print("Le solde du compte bancaire de %s est de %.2f euros."%(self.nom,self.solde))
