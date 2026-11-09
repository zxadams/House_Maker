import maya.cmds as cmds

import random

# UI set up: make ui for user to input house height, width and depth
# Also allow user to add a chimney if they choose and create a random house as well
# Window will delete/close old window if it's already open in the background when the user starts the program

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
    cmds.checkBox("createChimney", label="Create Chimney")

    cmds.button(label="Create House", command= 'createHouse()')
    cmds.button(label="Create Random House", command = 'createRandomHouse()')

    cmds.showWindow(UI)

# House creation functions(Chimney, walls, roof, door and floor)

#Chimney
def create_chimney(dimensions):
    chimney = cmds.polyCube(width=0.2, height=1.0, depth=0.2)

    cmds.move(dimensions[0] / 3.0, dimensions[1] + 0.2, dimensions[2] / 3.0)
    return chimney

#House floor, walls, door, and roof
def createHouse(houseWidth, houseHeight, houseDepth):

    #Floor/ base of the house
    floor = cmds.polyCube(width = houseWidth, height=0.1, depth=houseDepth)

    #Walls
    wall_A = cmds.polyCube(width=0.05, height=houseHeight, depth=houseDepth)
    cmds.move(houseWidth / 2.0, houseHeight /2.0, 0)

    wall_B = cmds.polyCube(width=0.05, height=houseHeight, depth=houseDepth)
    cmds.move(houseWidth / -2.0, houseHeight /2.0, 0)

    wall_C = cmds.polyCube(width=0.05, height=houseHeight, depth=houseDepth)
    cmds.move(0, houseHeight /2.0, houseDepth / 2.0)

    wall_D = cmds.polyCube(width=0.05, height=houseHeight, depth=houseDepth)
    cmds.move(0, houseHeight /2.0, houseDepth / -2.0)

    wall_Set = cmds.group(wall_A, wall_B, wall_C, wall_D)

    #Door
    door = cmds.polyCube(width=0.5, height=houseHeight/2.0, depth=0.1)
    cmds.move(houseWidth /2.0, houseHeight/4.0, houseDepth /2.0)

    #Roof
    roof = cmds.polyCube(width = houseWidth, height=0.4, depth=houseDepth)
    cmds.scale(1.2, 1.2, 1.2)

    #offsetting the roof so it sits better on the house
    cmds.move(0, houseHeight + 0.2, 0)

    #bevel the top face of the roof, top face index = f[1]
    cmds.select(roof[0] + ".f[1]")
    cmds.polyBevel(offset=0.3)

    #Check if "create chimney" is checked, if yes, chimney will be created
    chimney= []
    if cmds.checkBox("createChimney", query=True, value=True):
        chimney = create_chimney([houseWidth, houseHeight, houseDepth])

        if chimney:
            fullhouse = cmds.group(floor[0], wall_Set, door[0], roof[0], chimney[0], name="house")
        else:
            fullhouse = cmds.group(floor[0], wall_Set, door[0], chimney[0], name="house")

    #Delete history of the whole house(cleans up the outliner for the user)
    cmds.select(fullhouse)
    cmds.delete(all=True, ch=True)

    