# 📚 Gestion de Bibliothèque

Un projet simple en Python pour gérer une bibliothèque avec des fonctionnalités d'ajout de livres, d'enregistrement de membres, d'emprunt et de retour de livres.
## 🚀 Fonctionnalités

    Ajout et suppression de livres 📖
    Enregistrement des membres 🧑‍🤝‍🧑
    Emprunt et retour de livres 🔄
    Affichage des livres disponibles 📚
    Recherche de livres par titre ou auteur 🔍

## 🏗️ Structure du projet
```
📂 python_programmation_orientee_objet
│── 📂 models
│   ├── livre.py                # Classe Livre
│   ├── membre.py               # Classe Membre
│   ├── bibliotheque.py         # Classe Bibliotheque
│── main.py                     # Script principal
│── README.md                   # Documentation du projet
```

## 🔧 Installation & Utilisation
### 1️⃣ Cloner le projet
```
git clone https://github.com/votre-repo.git
cd votre-repo
```

### 2️⃣ Exécuter le programme

Assurez-vous d'avoir Python 3 installé, puis lancez :

``python main.py``

## ✅ Exemples d'utilisation

### Ajouter des livres 📖
```
livre1 = Livre("1984", "George Orwell", "978-0451524935")
bibliotheque.ajouter_livre(livre1)
```

### Enregistrer un membre 🧑
```
membre1 = Membre("Alice", 1)
bibliotheque.enregistrer_membre(membre1)
```

### Emprunter et retourner un livre 🔄
```
membre1.emprunter_livre(livre1)
membre1.retourner_livre(livre1)
```