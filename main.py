try:
    from pygame import *
except Exception as e:
    print(f"\n\n\033[91mModule pygame Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")
    exit()
try:
    from assets import game
except Exception as e:
    print(f"\n\n\033[91mFile /assets/game.py Not Found\nPlease make sure you have all file an folder in the right order.\n\n\033[0m")
    exit()