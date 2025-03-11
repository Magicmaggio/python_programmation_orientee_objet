class Membre:
    def __init__(self, nom, id_membre):
        self.nom = nom
        self.id_membre = id_membre
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        try:
            livre.emprunter()
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté '{livre.titre}'.")
        except Exception as e:
            print(e)

    def retourner_livre(self, livre):
        try:
            livre.retourner()
            self.livres_empruntes.remove(livre)
            print(f"{self.nom} a retourné '{livre.titre}'.")
        except Exception as e:
            print(e)

    def afficher_livres_empruntes(self):
        if self.livres_empruntes:
            print(f"Livres empruntés par {self.nom}:")
            for livre in self.livres_empruntes:
                print(f"- {livre.titre}")
        else:
            print(f"{self.nom} n'a emprunté aucun livre.")
