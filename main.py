from models.livre import Livre
from models.membre import Membre
from models.bibliotheque import Bibliotheque

# Création des livres
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "978-0261103573")
livre2 = Livre("1984", "George Orwell", "978-0451524935")
livre3 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", "978-0747532743")

# Création des membres
membre1 = Membre("Alice", 1)
membre2 = Membre("Bob", 2)

# Création de la bibliothèque
bibliotheque = Bibliotheque()

# Ajout des livres à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Enregistrement des membres
bibliotheque.enregistrer_membre(membre1)
bibliotheque.enregistrer_membre(membre2)

# Affichage des livres disponibles
bibliotheque.afficher_livres_disponibles()

# Emprunt et retour d'un livre
membre1.emprunter_livre(livre1)
membre1.afficher_livres_empruntes()
membre1.retourner_livre(livre1)

# Recherche d'un livre
bibliotheque.rechercher_livre("titre", "1984")
