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
    base.scale(10,10,10, root)
    base.move(0, 95, 2, root)
    base.parent(root, "Loc_Master")
    
    createSpine()

def createSpine():
    for i in range (0, base.intField(spineCount, query = True, value = True)):
        spine = base.spaceLocator(n = "Loc_SPINE_" + str(i))
        base.scale (10,10,10, spine)
        if i == 0:
            base.parent(spine, 'Loc_ROOT')
        else:
            base.parent(spine, 'Loc_SPINE_' + str(i-1))
        base.move(0, 1.25 + (0.25 * i), 0, spine)
       
def deleteLocators():
    nodes = base.ls("Loc_*")
    base.delete(nodes)