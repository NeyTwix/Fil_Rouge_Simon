try:
    from pygame import *
except Exception as e:
    print(f"\n\n\033[91mModule pygame Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")
try:
    from random import randint
except Exception as e:
    print(f"\n\n\033[91mModule random Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")
try:
    from assets import menu
except Exception as e:
    print(f"\n\n\033[91mFile /assets/menu.py Not Found\nPlease make sure you have all file an folder in the right order.\n\n\033[0m")
try:
    from assets import scores
except Exception as e:
    print(f"\n\n\033[91mFile /assets/scores.py Not Found\nPlease make sure you have all file an folder in the right order.\n\n\033[0m")