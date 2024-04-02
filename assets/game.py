# Import Libs
try:
    import pygame, pygame_menu
    from pygame_menu import themes,font,baseimage
    from random import randint
except Exception as e:
    print(f"\n\n\033[91mModule pygame, pygame_menu or random Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")
    exit()
try:
    from assets import scores
except Exception as e:
    try:
        import scores
    except Exception as e:
        print(f"\n\n\033[91mFile /assets/scores.py Not Found\nPlease make sure you have all file an folder in the right order.\033[0m\nDEBUG : {e}\n\n")
        exit()
try:
    from assets import color
except Exception as e:
    try:
        import color 
    except Exception as e:
        print(f"\n\n\033[91mFile /assets/scores.py Not Found\nPlease make sure you have all file an folder in the right order.\033[0m\nDEBUG : {e}\n\n")
        exit()



# Init PyGame and Windows Game
pygame.init()
surface = pygame.display.set_mode()
pygame.display.toggle_fullscreen()
x, y = pygame.display.get_window_size()
# Theme Params
simon_Theme = themes.THEME_DARK.copy()
simon_Theme.title_font = font.FONT_MUNRO
simon_Theme.background_color = (25, 25, 25)
simon_Theme.widget_alignment = pygame_menu.locals.ALIGN_RIGHT
simon_Theme.widget_selection_effect = pygame_menu.widgets.RightArrowSelection(arrow_size = (10, 15))
try:
    image_Path="./assets/menu.png"
    simon_Theme.background_color = baseimage.BaseImage(load_from_file=True, image_path=image_Path, drawing_mode=baseimage.IMAGE_MODE_FILL, drawing_offset=(0,0) )
except Exception as e:
    print(f"\n\n\033[91mFile {image_Path} Not Found\nPlease make sure you have all file an folder in the right order.\n\n\033[0m")
    exit()
mode = 1
def set_mode(value, gamemode):
    #print(value)
    global mode
    mode=gamemode
    return mode


def start_the_game():
    pygame_menu.events.CLOSE
    #color.basic_Game()
    print("start game")

    if mode == 1:
        print("Classic")
    elif mode==2:
        print("Inverted")
    elif mode==3:
        print("Multi")
    else:
        print("Nothing change")


def mode_menu():
    mainmenu._open(gamemode)

# Main menu
mainmenu = pygame_menu.Menu('Simon', x, y, theme=simon_Theme)
mainmenu.add.button('Start', mode_menu)
mainmenu.add.button('Quitter', pygame_menu.events.EXIT)

table = mainmenu.add.table(table_id='score', font_size=20,float=True,float_origin_position=True)
table.default_cell_padding = 5
table.border_color="None"

score = scores.high_score(scores.export_score())
for entry in score:
    table.add_row([entry['score'], entry['nom']])
    
print(scores.high_score(scores.export_score()))

gamemode = pygame_menu.Menu('Select a Difficulty', x, y, theme=themes.THEME_DARK)
gamemode.add.selector('',[('Classic',1),('Reverse',2),('MultiPlayer',3)], onchange=set_mode)
gamemode.add.button('Start', start_the_game)
gamemode.add.button('Return', pygame_menu.events.BACK)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        
 
    pygame.display.update()