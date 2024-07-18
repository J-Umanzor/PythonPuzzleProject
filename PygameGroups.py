import pygame

# active_blocks is a pygame group to display any blocks that are should be displayed
shown_blocks = pygame.sprite.Group()

# interactive_block are basically every block that can be interacted with
# note this means you can have blocks that the player doesn't interact with but are still shown
# and vice versa, stuff that isn't shown but can still be interacted with
interactive_blocks = pygame.sprite.Group()

# Just a simple function to make some other stuff look cleaner
# Checks every button and deactivates them if they don't have something currently on them
def check_btn():
    blocks = interactive_blocks.__iter__()
    for block in blocks:
        if block.get_type() == "button":
            block.collision_detected("active")
