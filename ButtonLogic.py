from BlockLogic import Block
import os

# NOTE TO SELF, find an elegant way to code activate such that it can do everything it already does
# and also allows for the creation of a block at any location


class Button(Block):
    # The activate_function is the function that will happen if somthing collides with the button
    # The deactivate_function is the function that will happen when somthing leaves the button
    # deactivate_function should ALWAYS reverse whatever activate function does.
    # EX: if activate function spawns a box, deactivate should remove it

    def __init__(self,  x_loc, y_loc, activate_function, deactivate_function, parameters=0,):
        # image path must be changed on local machine
        super().__init__("green", "button", x_loc, y_loc, os.path.join('button.png'))
        self.btn_active_function = activate_function
        self.btn_inactive_function = deactivate_function
        self.activated = False
        self.parameter = parameters

    def activate(self):
        if not self.activated:
            print("this ran")
            if self.parameter != 0:
                self.btn_active_function(self.parameter)
            else:
                self.btn_active_function()
            self.activated = True

    def deactivate(self):
        if self.activated:
            print("this activated")
            if self.parameter != 0:
                self.btn_inactive_function(self.parameter)
            else:
                self.btn_inactive_function()
        self.activated = False

    # Buttons use the direction parameter in a different way than every other block
    # If direction is up, that means something is currently on top of it
    # Otherwise it means nothing is on top of it

    def collide_logic(self, direction):
        if direction == "active":
            self.activate()
        elif direction == "inactive":
            self.deactivate()
        else:
            self.collision_detected("active")