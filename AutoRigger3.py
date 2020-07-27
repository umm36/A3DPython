import maya.cmds as mc

##setup##
#def loadUI():

if mc.window("HAR", query = True, exists = True):
    mc.deleteUI("HAR")
mc.window("HAR", title = "Human Auto Rigger", widthHeight = (200, 40))
mc.rowColumnLayout("Column1", parent = "HAR", adjustableColumn = True)
mc.button(l = "Create Locators", w = 200, c = "CreateLocators(rigName)")
mc.button(l = "Delete Locators", w = 200, c = "deleteLocators()")  
mc.button(l = "Create Joints", w = 200, c = "createJoints()")
      
mc.text("Spine Count", l = "Spine Count")
spineCount = mc.intField(minValue = 1, maxValue = 10, value = 4) 
       
mc.text("Finger Count", l = "Finger Count")
fingerCount = mc.intField(minValue = 1, maxValue = 10, value = 4)  
      
mc.text("Finger Joints", l = "Finger Joints")
fingerJoints = mc.intField(minValue = 1, maxValue = 10, value = 3) 
       
mc.text("Rig Name", l = "Rig Name")    
mc.textField("NameOfRig", parent = "Column1", placeholderText = "Character Name/IDCode")
mc.showWindow()

#loadUI()



def rN(): #Rig Name
    userInput = mc.textField("NameOfRig", query = True, text = True)
    return userInput
rigName = rN() #sets rig name as a variable using a function.
##Scripting## 

def CreateLocators(rigName):
    sides = ["L", "R"]    
    axis = ["X", "Y", "Z"]
    locScale = 10
    offset = 1
    if mc.objExists(rigName+"_Loc_Master"):
        print 'Loc_Master already exists.'
    else:
        baseGroup = mc.group(em = True, name = rigName+"_Loc_Master")
        mc.scale(10,10,10, baseGroup)

        root = mc.spaceLocator(n = rigName+"_Loc_ROOT")
        mc.move(0,95,2, rigName+"_Loc_ROOT")
        mc.parent(root, rigName+"_Loc_Master")
    for i in sides:
        if mc.objExists(rigName+"_" + i + "_Arm_GRP"):
            print "Arms already exist."
        else:
            #Resetting offset side here
            if i == "R":
                offset = -1

            spineNum = str(mc.intField(spineCount, query = True, value = True) -1)

            wristPos = [43*offset,93.7,3.3]
            anklePos = [40*offset,3,1]
            shoulderPos = [40*offset,3,1]
            claviclePos = [40*offset,3,1]
            elbowPos = [40*offset,3,1]

            prevLoc = ""

            createSpine()
            spawnLocators(wristPos, "Arm", "Wrist", i)
            #spawnLocators(anklePos, "Leg", "Ankle", i)
            #spawnLocators(anklePos, "Leg", "Ankle", i)
            #spawnLocators(anklePos, "Leg", "Ankle", i)
            #spawnLocators(anklePos, "Leg", "Ankle", i)

def spawnLocators(pos, limb, joint, i):
    jntloc = mc.spaceLocator(n = rigName+"_Loc_" + i + "_" + limb + "_" + joint, position = pos)
    mc.parent(jntloc, prevLoc)
    SetScale(jntloc, axis)
    prevLoc = jntloc

def createSpine():
    for i in range (0, mc.intField(spineCount, query = True, value = True)):
        spine = mc.spaceLocator(n = rigName+"_Loc_SPINE_" + str(i+1))
        if i == 0:
            mc.parent(spine, rigName+"_Loc_ROOT")            
        else:
            mc.parent(spine, rigName+"_Loc_SPINE_"+str(i))
        mc.scale(1,1,1, spine)
        mc.move(0, 110 + (15 * i), 2, spine)

def SetScale(component, axis):
    for i in axis:
        mc.setAttr(component + ".localScale" + i, locScale)
        
def deleteLocators():
    nodes = mc.ls(rigName+"_Loc_*")
    mc.delete(nodes)

## OLD SHIT

def createJoints():
    if mc.objExists("RIG"):
        print "Rig already exists"
    else:
        jointGRP = mc.group(em = True, name = rigName+"_Joints_GRP")

        ##create spine joints

        root = mc.ls("*_Loc_ROOT")

        allSpines = mc.ls("*_Loc_SPINE_*", type = "locator")
        spine = mc.listRelatives(*allSpines, p = True, f= True)

        rootPos = mc.xform(root, q = True, t = True, ws = True)
        rootJoint = mc.joint(radius = 4, p = rootPos, name = rigName+"_jnt_Root")
        for i, s in enumerate(spine):
            pos = mc.xform(s, q = True, t = True, ws = True)
            j = mc.joint(radius = 4, p = pos, name = rigName+"_jnt_Spine_"+str(i))
