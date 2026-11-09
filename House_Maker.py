import maya.cmds as cmds

import random

#UI set up: make ui for user to input house height, width and depth
# Also allow user to add a chimney if they choose and create a random house as well
#Window will delete/close old window if it's already open in the background when the user starts the program

def create_ui():
    win_name = "House Maker"
    if cmds.window(win_name, exists=True):
        cmds.deleteUI(win_name)

    UI = cmds.window(win_name, title= "House Maker", width = 400)

    cmds.columnLayout(rowSpacing=10)

    cmds.text(label="House Maker")

    #Sliders house dimensions(width, height, depth)
    cmds.intSliderGrp("width", label="Width", min=1, max=10)

    cmds.intSliderGrp("height", label="Height", min=1, max=10)

    cmds.intSliderGrp("depth", label="Depth", min=1, max=10)

    #Checkbox for chimney
    cmds.checkBox("includeChimney", label="Include Chimney")

    cmds.button(label="Create House", command= 'createHouse()')
    cmds.button(label="Create Random House", command = 'createRandomHouse()')

    cmds.showWindow(UI)

# House creation functions(Chimney, walls, roof, door and floor)