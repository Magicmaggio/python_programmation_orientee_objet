from models.livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.membres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté à la bibliothèque.")

    def supprimer_livre(self, isbn):
        livre = self.trouver_livre_par_isbn(isbn)
        if livre:
            self.livres.remove(livre)
            print(f"Le livre '{livre.titre}' a été supprimé de la bibliothèque.")
        else:
            print("Livre introuvable.")

    def enregistrer_membre(self, membre):
        self.membres.append(membre)
        print(f"{membre.nom} a été enregistré comme membre de la bibliothèque.")

    def afficher_livres_disponibles(self):
        livres_disponibles = [livre for livre in self.livres if livre.statut == "disponible"]
        if livres_disponibles:
            print("Livres disponibles :")
            for livre in livres_disponibles:
                print(f"- {livre.titre} de {livre.auteur}")
        else:
            print("Aucun livre disponible.")

    def rechercher_livre(self, critere, valeur):
        if critere == "titre":
            livres_trouves = [livre for livre in self.livres if livre.titre.lower() == valeur.lower()]
        elif critere == "auteur":
            livres_trouves = [livre for livre in self.livres if livre.auteur.lower() == valeur.lower()]
        else:
            print("Critère de recherche invalide.")
            return

        if livres_trouves:
            print(f"Livres trouvés par {critere}: {valeur}")
            for livre in livres_trouves:
                print(f"- {livre.titre} de {livre.auteur} (ISBN: {livre.isbn})")
        else:
            print(f"Aucun livre trouvé pour {critere}: {valeur}.")

    def trouver_livre_par_isbn(self, isbn):
        for livre in self.livres:
            if livre.isbn == isbn:
                return livre
        return None
