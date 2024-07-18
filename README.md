PythonPuzzle
    New Changes from main
# Sprite changes:
    Player
    Box
    Button
    
# Code changes:
    Altered level logic code so that its cleaner
    Example of one change from level 3
    Original:
    loop that creates block in bottom right
        for row in range(5):
            for col in range(5):
                if row == 0 or row == 4 or col == 0 or col == 4:
                    block1 = BlockLogic.Block("black", "wall", 64, 64, image_paths["wall"])
                    block1.spawn()
                    block1_x = 896 + col * 64
                   block1_y = 384 + row * 64
                    block1.teleport(block1_x, block1_y)
                    block1_doors.append(block1)
    
     Changed:
      #loop that creates block in bottom right
        for row in range(5):
            for col in range(5):
                if row == 0 or row == 4 or col == 0 or col == 4:
                    block1 = BlockLogic.Block("black", "wall",  896 + col * 64, 384 + row * 64, image_paths["wall"])
                    block1_doors.append(block1)
    
# Visual Changes:
     Buttons sprites will no longer go over player and box sprites
     Essesially boxes and the player sprites will completly overlap the button sprite making it such that we can't see the button
    
# Level change:
     Added a 4th level that is completly empty so that winning level 3 will no longer kick you out of the game
