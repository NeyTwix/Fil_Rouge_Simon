[image_0]: https://pfst.cf2.poecdn.net/base/image/a22aa60808ba9d729ad4027e8c855bbee43bb0236013ac2891effc5484843133?w=1000&h=682&pmaid=54689190

# Simon :video_game:

### Note :memo:

Le but de ce projet est de programmer le jeu de société [Simon](<https://fr.wikipedia.org/wiki/Simon_(jeu)>). Le jeu crée une séquence de couleurs (🔴 rouge, 🟢 vert, 🔵 bleu, 🟡 jaune) et l'utilisateur doit reproduire la séquence. Le programme recommence alors en ajoutant une couleur à la séquence en boucle jusqu'à ce que l'utilisateur se trompe.

---

### Cahier des charges :clipboard:

Le programme doit afficher une séquence de couleurs (🔴 rouge, 🟢 vert, 🔵 bleu, 🟡 jaune) au hasard, en commençant par une séquence de longueur 1. Il doit ensuite demander à l'utilisateur de reproduire la séquence et vérifier que la réponse est correcte. Si la réponse est correcte, le programme recommence en ajoutant une couleur à la séquence. Si la réponse est incorrecte, le programme affiche un message d'erreur et s'arrête en indiquant le score de l'utilisateur. Le programme doit également être équipé d’une interface adaptée. Le programme doit également sauvegarder les meilleurs résultats et les afficher avant le début du jeu.
Le programme doit contenir trois modes de jeux :

- Le mode 1 consiste à reproduire une suite de touches créée aléatoirement par le jeu, la plus longue possible.
- Le mode 2 inverse les rôles : le joueur va composer la suite de touches, et Simon va la reproduire. Cependant, le joueur ne doit pas se tromper en produisant sa propre suite.
- Le mode 3 est un mode multijoueur : chaque joueur va s'attribuer une touche, et devra la presser quand Simon la lui demandera. Si un joueur ne répond pas quand Simon lui demande, ou répond au mauvais moment, il sera éliminé de la manche. La partie s'arrête quand il ne reste plus qu'un joueur en lice.

### Liste des tâches :pencil:

- [ ] [1] Interface Graphique
  - [x] [1] Détection du tactile
  - [ ] [1] Menu de démarrage
    - [ ] [1-3] Sélection du mode
    - [ ] [2] Meilleurs scores en haut à gauche
- [ ] [1] Jeu basique
  - [ ] [1] Génération aléatoire de couleur
  - [ ] [1] Continuité du jeu si couleur correcte
- [ ] [2] Sauvegarde du score dans un fichier
- [ ] [2] Affichage des 5 meilleurs scores au démarrage
- [ ] [3] Mode Inversé
- [ ] [3] Mode Multi
  - [ ] [1] Gérer l'élimination des joueurs
  - [ ] [2] Ajout d'une voix pour les couleurs

### Modules Requis :toolbox:

- [PyGame](https://www.pygame.org/docs)
- [Random](https://docs.python.org/3/library/random.html)
- [PyGame-Menu](https://pygame-menu.readthedocs.io/en/4.4.2/index.html)
- [CSV]()
- [Time]() (Pas sûr)

---

### Images :camera:

![simon_image][image_0]
