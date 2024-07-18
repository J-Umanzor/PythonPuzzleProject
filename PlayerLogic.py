import pygame

from BlockLogic import Block
import os

# After some revision the player basically acts completely like a box but that you directly control
class Player(Block):
    def __init__(self, x_loc, y_loc):
        #image must be changed to local path
        super().__init__(None, "player", x_loc, y_loc, os.path.join('player.png'))

    def move(self, key):
        # Anytime the "WSAD" keys are pressed, it moves the player, then sees if they hit somthing
        if key == pygame.K_w:
            self.rect.y -= 64
            self.collision_detected("up")
        if key == pygame.K_s:
            self.rect.y += 64
            self.collision_detected("down")
        if key == pygame.K_a:
            self.rect.x -= 64
            self.collision_detected("left")
        if key == pygame.K_d:
            self.rect.x += 64
            self.collision_detected("right")

Player = Player(64, 64)
Player.spawn()