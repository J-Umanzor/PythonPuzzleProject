import BlockLogic
import ButtonLogic
import PlayerLogic
import os

from PygameGroups import shown_blocks, interactive_blocks


# Change current level every time we go to a new level
current_level = 0

# Clears the level to get ready to import a new one
def clear_level():
    interactive_blocks.empty()
    shown_blocks.empty()
# I kinda want to add an animation to show level transition here, but I also don't have the time for it
# Feel free to add one if you like

def create_level_border():
    for i in range(0, 12):
        border = BlockLogic.Block("black", "wall", -64, 64*i, image_paths["wall"])
        border2 = BlockLogic.Block("black", "wall", 1280, 64*i, image_paths["wall"])
        border.spawn()
        border2.spawn()
    for i in range(0, 20):
        border = BlockLogic.Block("black", "wall", 64* i, -64, image_paths["wall"])
        border2 = BlockLogic.Block("black", "wall", 64 * i, 768, image_paths["wall"])
        border.spawn()
        border2.spawn()


# This is an example on how to make a level
# First we teleport the player to a location(Footnote 1)
# Then we create any object that we need for this level
# Then we spawn them in(including the player)
# Make sure to add an ExitBtn to win the level

#added small disctionary for image paths / must be changed to local path
image_paths = {
    "box": os.path.join('box.png'),
    "wall": os.path.join('wall.png')
}




def level1():
    clear_level()
    global current_level
    current_level = 1
    create_level_border()
    PlayerLogic.Player.teleport(64, 64)

    #create moveable block
    Box = BlockLogic.Block( "black", "box", 64, 64, image_paths["box"])
    #loop to create wall in center of area
    for i in range(1, 13):
        #condition to make the center wall the gate that will despawn with button
        if (i != 5):
            wall = BlockLogic.Block("black", "wall", 640, (-64 + 64 * i), image_paths["wall"])
            wall.spawn()
        else: 
            gate = BlockLogic.Block("black", "wall", 640, (-64 + 64 * i), image_paths["wall"])
            gate.spawn()
    Button1 = ButtonLogic.Button(256, 128, BlockLogic.Block.despawn, BlockLogic.Block.spawn, gate)
    ExitBtn = ButtonLogic.Button(1028, 512, level2, useless_function(), 0)

    Button1.spawn()
    ExitBtn.spawn()
    PlayerLogic.Player.spawn()
    Box.spawn()
    Box.teleport(64, 128)
    


def level2():
    global  current_level
    current_level = 2
    clear_level()
    create_level_border()
    PlayerLogic.Player.teleport(64, 256)
    #two lists used to keep track of both obstacles in level
    traps = []
    exit_doors = []

    #loop that creates a box of wall blocks
    for row in range(5):
        for col in range(5):
            if row == 0 or row == 4 or col == 0 or col == 4:
                trap = BlockLogic.Block("black", "wall", 320 + col * 64, 384 + row * 64, image_paths["wall"])
                trap.spawn()
                traps.append(trap)

    #loop that creates a box of wall blocks
    for row in range(5):
        for col in range(5):
            if row == 0 or row == 4 or col == 0 or col == 4:
                exit = BlockLogic.Block("black", "wall", 896 + col * 64, 0 + row * 64, image_paths["wall"])
                exit.spawn()
                exit_doors.append(exit)

    Box1 = BlockLogic.Block( "black", "box", 64, 64, image_paths["box"])
    Box2 = BlockLogic.Block( "black", "box", 64, 64, image_paths["box"])

    Button1 = ButtonLogic.Button(256, 128, BlockLogic.Block.despawn, BlockLogic.Block.spawn, traps[7])
    Button2 = ButtonLogic.Button(448, 512, BlockLogic.Block.despawn, BlockLogic.Block.spawn, exit_doors[7])
    Button3 = ButtonLogic.Button(1024, 128, level3, useless_function(), 0)
    Button1.spawn()
    Button2.spawn()
    Button3.spawn()
    PlayerLogic.Player.spawn()
    Box1.spawn()
    Box1.teleport(64, 512)
    Box2.spawn()
    Box2.teleport(576, 64)




def level3():
    global  current_level
    current_level = 3
    clear_level()
    create_level_border()
    PlayerLogic.Player.teleport(576, 192)
    #lists to keep track of the walls made so a certain passage can be opened
    block1_doors = []
    block2_doors = []
    reset_doors = []
    end_doors = []


    #loop that creates block in bottom right
    for row in range(5):
        for col in range(5):
            if row == 0 or row == 4 or col == 0 or col == 4:
                block1 = BlockLogic.Block("black", "wall",  896 + col * 64, 384 + row * 64, image_paths["wall"])
                block1.spawn()
                block1_doors.append(block1)

    #loop that creates block in top right
    for row in range(5):
        for col in range(5):
            if row == 0 or row == 4 or col == 0 or col == 4:
                reset = BlockLogic.Block("black", "wall", 896 + col * 64, row * 64, image_paths["wall"])
                reset.spawn()
                reset_doors.append(reset)
    
    #loop that creates block in top left
    for row in range(5):
        for col in range(5):
            if row == 0 or row == 4 or col == 0 or col == 4:
                end = BlockLogic.Block("black", "wall", col * 64, row * 64, image_paths["wall"])
                end.spawn()
                end_doors.append(end)

    #loop that creates block in bottom left
    for row in range(5):
        for col in range(5):
            if row == 0 or row == 4 or col == 0 or col == 4:
                block2 = BlockLogic.Block("black", "wall",col * 64, 384 + row * 64, image_paths["wall"])
                block2.spawn()
                block2_doors.append(block2)
    Box1 = BlockLogic.Block( "black", "box", 64, 64, image_paths["box"])
    Box2 = BlockLogic.Block( "black", "box", 64, 64, image_paths["box"])

    #buttons located in the center that will open the gate to lower corner blocks
    block1_button = ButtonLogic.Button(704, 384, BlockLogic.Block.despawn, BlockLogic.Block.spawn, block1_doors[7])
    block2_button = ButtonLogic.Button(448, 384, BlockLogic.Block.despawn, BlockLogic.Block.spawn, block2_doors[8])

    #buttons located on bottom corners that open door to upper corner blocks
    reset_doors_button = ButtonLogic.Button(1024, 512, BlockLogic.Block.despawn, BlockLogic.Block.spawn, reset_doors[7])
    end_doors_button = ButtonLogic.Button(128, 512, BlockLogic.Block.despawn, BlockLogic.Block.spawn, end_doors[8])

    #this button will send the player back a level
    reset_button = ButtonLogic.Button(1024, 128, level2, useless_function(), 0)

    #this button will completes the level
    end_button = ButtonLogic.Button(128, 128, level4, useless_function(), 0)

    block1_button.spawn()
    block2_button.spawn()
    end_doors_button.spawn()
    reset_button.spawn()
    end_button.spawn()
    PlayerLogic.Player.spawn()
    Box1.spawn()
    Box1.teleport(704, 64)
    Box2.spawn()
    Box2.teleport(448, 64)
    reset_doors_button.spawn()


def level4():
    global current_level
    current_level = 4
    clear_level()
    create_level_border()
    PlayerLogic.Player.teleport(576, 192)
    PlayerLogic.Player.spawn()


# as you make levels add them to this list
levels = [level1, level2, level3, level4]

# This is used to reset the level, remember to keep track of what level we're in
def reset_level():
    levels[current_level-1]()

# This doesn't do anything, I just needed a placeholder function because the button class needs 2 functions
def useless_function():
    pass

# Footnote 1
# The reason for the teleport is that I currently am using main.py as the place where I gather all inputs
# Due to the way python works(or probably every coding language works) I can't circular import a created player
# From this file to main because I need main to import this file to get levels
# There might be a workaround, but I can't think of one right now and this works fine
