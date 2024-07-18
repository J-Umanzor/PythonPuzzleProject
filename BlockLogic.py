import pygame
from pygame.sprite import Sprite
from PygameGroups import shown_blocks, interactive_blocks


# Blocks are will all be "rectangles" that are 64 by 64 pixels big
class Block(Sprite):
    #added image_path parameter to be able to change the images of the block
    def __init__(self, color_key, types, x_loc, y_loc, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (64, 64))
        # .fill(color) will make the object a specific color
        # .set_colorkey will make any part of the sprite that is that color transparent
        # for instance a half green, half red sprite with a color key of green, will be half transparent
        # and half red
        
        self.image.set_colorkey(None)

        # This determines where the block will initially spawn
        
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        # Type describes the type of block it is(Currently only works with "player" and "box)
        self.type = types

    # spawn will make the object show up and turn on collision and interacion
    # Parameters are where you want to spawn the object
    # You can now spawn things on top of each other, it will attempt to push things to the right
    # Walls will push things to their left
    def spawn(self):
        if not(self in shown_blocks):
            shown_blocks.add(self)
        if not (self in interactive_blocks):
            interactive_blocks.add(self)
            self.collision_detected("right")

    # Despawn will simply despawn the object, removing from active play and interaction
    def despawn(self):
        shown_blocks.remove(self)
        interactive_blocks.remove(self)

    def teleport(self, x_loc, y_loc):
        self.rect.x = x_loc
        self.rect.y = y_loc

    def collision_detected(self, direction):
        # There should only ever be one block hit ever(the block hit should move such that it no longer hits)
        blocks_hit = pygame.sprite.spritecollide(self, interactive_blocks, False)
        if (self.type == "box") or (self.type == "player"):
            for blocks in blocks_hit:
                if blocks != self:
                    blocks.collide_logic(direction)
        elif self.type == "wall":
            for blocks in blocks_hit:
                if blocks != self:
                    blocks.bounce_back(direction)
        elif self.type == "button":
            if len(blocks_hit) > 1:
                self.collide_logic("active")
            else:
                self.collide_logic("inactive")

    def collide_logic(self, direction):
        if (self.type == "box") or (self.type == "player"):
            if direction == "up":
                self.rect.y -= 64
            elif direction == "down":
                self.rect.y += 64
            elif direction == "left":
                self.rect.x -= 64
            else:
                self.rect.x += 64
            self.collision_detected(direction)
        elif self.type == "wall":
            self.collision_detected(direction)

    # bounce_back is used whenever we need to move somthing back to its original position after a move
    # [currently only used when we need to move somthing back when it hits a wall]
    def bounce_back(self, direction):
        if direction == "up":
            self.collide_logic("down")
        elif direction == "down":
            self.collide_logic("up")
        elif direction == "left":
            self.collide_logic("right")
        else:
            self.collide_logic("left")

    # Used to get the type of the currently block
    def get_type(self):
        return self.type