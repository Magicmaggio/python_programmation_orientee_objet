class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.statut = "disponible"

    def __str__(self):
        return f"{self.titre} de {self.auteur} (ISBN: {self.isbn}) - {self.statut}"

    def emprunter(self):
        if self.statut == "disponible":
            self.statut = "emprunté"
        else:
            raise Exception(f"Le livre '{self.titre}' est déjà emprunté.")

    def retourner(self):
        if self.statut == "emprunté":
            self.statut = "disponible"
        else:
            raise Exception(f"Le livre '{self.titre}' n'est pas emprunté.")
