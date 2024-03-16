# Simon

---

### Note

Le but de ce projet est de programmer le jeu de société [Simon](<https://fr.wikipedia.org/wiki/Simon_(jeu)>). Le jeu crée une séquence de couleurs (rouge, vert, bleu, jaune) et l'utilisateur doit reproduire la séquence. Le programme recommence alors en ajoutant une couleur à la séquence en boucle jusqu'à ce que l'utilisateur se trompe.

---

### Cahier des charges

Le programme doit afficher une séquence de couleurs (rouge, vert, bleu, jaune) au hasard, en commençant par une séquence de longueur 1. Il doit ensuite demander à l'utilisateur de reproduire la séquence et vérifier que la réponse est correcte. Si la réponse est correcte, le programme recommence en ajoutant une couleur à la séquence. Si la réponse est incorrecte, le programme affiche un message d'erreur et s'arrête en indiquant le score de l'utilisateur. Le programme doit également être équipé d’une interface adaptée. Le programme doit également sauvegarder les meilleurs résultats et les afficher avant le début du jeu.
Le programme doit contenir trois modes de jeux ;

- Le mode 1 consiste à reproduire une suite de touches créée aléatoirement par le jeu, la plus longue possible.
- Le mode 2 inverse les rôles : le joueur va composer la suite de touches, et Simon va la reproduire. Cependant, le joueur ne doit pas se tromper en produisant sa propre suite.
- Le mode 3 est un mode multijoueur : chaque joueur va s'attribuer une touche, et devra la presser quand Simon la lui demandera. Si un joueur ne répond pas quand Simon lui demande, ou répond au mauvais moment, il sera éliminé de la manche. La partie s'arrête quand il ne reste plus qu'un joueur en lice.

### Listes des taches

- [ ] [1] Interface Graphique
  - [x] [1] Détection du tactile
  - [ ] [1] Menu de demarrage
    - [ ] [1-3] Selection du mode
    - [ ] [2] Meilleurs scores en haut a gauche
- [ ] [1] Jeu basique
  - [ ] [1] Generation aleatoire de couleur
  - [ ] [1] Continuité du jeu si couleur correcte
- [ ] [2] Sauvegarde du score dans un fichier
- [ ] [2] Affichage des 5 meilleurs score au démarrage
- [ ] [3] Mode Inversé
- [ ] [3] Mode Multi
  - [ ] [1] Gerer l'elimination des joueurs
  - [ ] [2] Ajout d'une voix pour les couleurs

### Module Requis

- [PyGame](https://www.pygame.org/docs)
- [Random](https://docs.python.org/3/library/random.html)
- [PyGame-Menu](https://pygame-menu.readthedocs.io/en/4.4.2/index.html)
- [CSV]()
- [Time]() (Pas sur)

---

### Images

![simon_image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.clubjouet.com%2FPREXTRA%2Fdocs%2F7011897.jpg&f=1&nofb=1&ipt=2d3332d18eacbd81d9786dec11751352833608d4af6d810ad0dbb5f394b66ea1&ipo=images "Juste une image du jeu.")
