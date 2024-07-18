import pygame
import LevelLogic
import PlayerLogic
from PygameGroups import shown_blocks, check_btn
import os

pygame.init()
screen = pygame.display.set_mode((1280, 768))
clock = pygame.time.Clock()
running = True
dt = 0



# This loads the background image from local files / must be changed to local path
background_image = pygame.image.load(os.path.join('background.jpg'))
background_image = pygame.transform.scale(background_image, (1280, 768))

# Set up the font
font = pygame.font.SysFont('Impact', 60)

# Function to display the menu options

def display_menu():
    menu_options = [
        "Press 1 to Start Game",
        " ",
        "Press Q to Quit"
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    LevelLogic.level1()
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        # Clear the screen
        screen.blit(background_image, (0, 0))

        # Display the menu options on the screen
        for i, option in enumerate(menu_options):
            text = font.render(option, True, (255, 255, 255))
            screen.blit(text, (400, 150 + i * 50))
        
        pygame.display.flip()
        clock.tick(60)

display_menu()


while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset the current level
                LevelLogic.reset_level()
            if event.key == pygame.K_t:
                # Reset the current level
                display_menu()
            PlayerLogic.Player.move(event.key)

    # Fill the screen with a color to wipe away anything from the last frame
    screen.blit(background_image, (0, 0))
    # Render your game here


    shown_blocks.update()
    # This constantly checks if all active buttons are currently pressed and deactivates them if they're not
    check_btn()
    shown_blocks.draw(screen)

    # Flip() the display to put your work on the screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()