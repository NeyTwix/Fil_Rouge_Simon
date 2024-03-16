# Import Libs
try:
    import pygame, pygame_menu
    from pygame_menu import themes,font,baseimage
except Exception as e:
    print(f"\n\n\033[91mModule pygame or pygame_menu Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")

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


def set_mode(value, difficulty):
    print(value)
    print(difficulty)
 
def start_the_game():
    pass

# Main menu
mainmenu = pygame_menu.Menu('Simon', x, y, theme=simon_Theme)
mainmenu.add.button('Start', start_the_game)
mainmenu.add.text_input('', default='Player', maxchar=20)
mainmenu.add.selector('',[('Classic',1),('Reverse',2),('MultiPlayer',3)], onchange=set_mode)
mainmenu.add.button('Quitter', pygame_menu.events.EXIT)
mainmenu.add.label('TEST')
 


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
 
    pygame.display.update()