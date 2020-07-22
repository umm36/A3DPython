import maya.cmds as base
from functools import partial

base.window("Auto Rigger")
base.rowColumnLayout(nc = 2)

base.button(l = "Create Locators", w = 200, c = "createLocators()")
base.button(l = "Delete Locators", w = 200, c = "deleteLocators()")

#base.button(l = "Create Locators", w = 200, c = partial(createLocators))
#base.button(l = "Delete Locators", w = 200, c = partial(deleteLocators))

base.text("Spine Count", l = "Spine Count")
spineCount = base.intField(minValue = 1, maxValue = 10, value = 4)

base.showWindow()

############### Actual Code ###############      

def createLocators():
    if base.objExists("Loc_Master"):
        print 'Loc_Master already exists.'
    else:
        base.group(em = True, name = "Loc_Master")
    
    root = base.spaceLocator(n = 'Loc_ROOT')
    #base.scale(10,10,10, root)
    base.move(0, 95, 2, root)
    base.parent(root, "Loc_Master")
    
    createSpine()

def createSpine():
    for i in range (0, base.intField(spineCount, query = True, value = True)):
        spine = base.spaceLocator(n = "Loc_SPINE_" + str(i))
        base.scale (1,1,1, spine)
        if i == 0:
            base.parent(spine, 'Loc_ROOT')
        else:
            base.parent(spine, 'Loc_SPINE_' + str(i-1))
        base.move(0, 1.25 + (10.25 * i), 0, spine)
    createArms(1)
    createArms(-1)


def createArms(side):
    if side == 1: #left
        if base.objExists("L_Arm_GRP"):
            print "Nah"
        else:
            L_arm = base.group(em = True, name = "L_Arm_GRP")
            base.parent(L_arm, "Loc_SPINE_" + str(base.intField(spineCount, query = True, value = True) - 1))
            base.move(12.338 * side, 148.887, -1.486, L_arm)
    else: #right
        if base.objExists("R_Arm_GRP"):
            print "Naaaah"
        else:
            R_arm = base.group(em = True, name = "R_Arm_GRP")
            base.parent(R_arm, "Loc_SPINE_" + str(base.intField(spineCount, query = True, value = True) - 1))
            base.move(12.338 * side, 148.887, -1.486, R_arm)

def deleteLocators():
    nodes = base.ls("Loc_*")
    base.delete(nodes)