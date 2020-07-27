import maya.cmds as mc

##setup##
#def loadUI():


if mc.window("HAR", query = True, exists = True):
    mc.deleteUI("HAR")
mc.window("HAR", title = "Human Auto Rigger", widthHeight = (200, 40))
mc.rowColumnLayout("Column1", parent = "HAR", adjustableColumn = True)
mc.button(l = "Create Locators", w = 200, c = "CreateLocators()")
mc.button(l = "Delete Locators", w = 200, c = "deleteLocators()")  
mc.button(l = "Create Joints", w = 200, c = "createJoints()")
mc.button(l = "Delete Joints", w = 200, c = "deleteJoints()")
      
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
#rigName = "" #rN() #sets rig name as a variable using a function. #doesn't work?

def rN(): #Rig Name
    userInput = mc.textField("NameOfRig", query = True, text = True)
    return str(userInput)
    
####Scripting####
def CreateLocators():    

    sides = ["L", "R"]    
    axis = ["X", "Y", "Z"]
    locScale = 10
    offset = 1
    if mc.objExists(rN()+"_Loc_Master"):
        print 'Loc_Master already exists.'
    else:
        print rN() + "_Loc_Master"
        
        baseGroup = mc.group(em = True, name = rN() + "_Loc_Master")
        mc.scale(10,10,10, baseGroup)

        root = mc.spaceLocator(n = rN()+"_Loc_ROOT")
        mc.move(0,95,2, rN()+"_Loc_ROOT")
        mc.parent(root, rN()+"_Loc_Master")
    for i in sides:
        if mc.objExists(rN()+"_" + i + "_Arm_GRP"):
            print "Arms already exist."
        else:
            #Re-setting offset side
            if i == "R":
                offset = -1

            #spineNum = str(mc.intField(spineCount, query = True, value = True) -1) #Needless currently.
            
            #Arm Locators
            claviclePos = [12.3*offset,148,-1.4]
            shoulderPos = [19.8*offset,143,-1.4]
            elbowPos = [30.3*offset,117.6,-2.6]
            wristPos = [43*offset,93.7,3.3]
            
            #Leg Locators
            hipPos = [9.9*offset, 87.8, 1.7]
            kneePos = [11.9*offset, 46.4, 1.1]
            anklePos = [14.8*offset, 2.4, -3.8]
            toesPos = [17*offset, 2.7, 7.8]
            
            #handLocators
            #wrist 1-5
            #thumb
            #index finger
            #middle finger
            #ring finger
            #pinky finger
            
            #prevLoc = ""
            if i == "L":
                createSpine()
            
            clavicalParent = rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2)
            hipParent = rN()+"_Loc_ROOT"
            ####CBB: could be refined/optimised using dictionaries
            Clavicle = spawnLocators(clavicalParent, claviclePos, "Arm", "Clavicle", i)
            Shoulder = spawnLocators(Clavicle, shoulderPos, "Arm", "Shoulder", i)
            Elbow = spawnLocators(Shoulder, elbowPos, "Arm", "Elbow", i)
            Wrist = spawnLocators(Elbow, wristPos, "Arm", "Wrist", i)
            Hip = spawnLocators(hipParent, hipPos, "Leg", "Hip", i)
            Knee = spawnLocators(Hip, kneePos, "Leg", "Knee", i)
            Ankle = spawnLocators(Knee, anklePos, "Leg", "Ankle", i)
            Toes = spawnLocators(Ankle, toesPos, "Leg", "Toes", i)

def spawnLocators(parent, pos, limb, joint, i):
    jntloc = mc.spaceLocator(n = rN()+"_Loc_" + i + "_" + limb + "_" + joint, position = pos)
    mc.parent(jntloc, parent)
    ##SetScale(jntloc, axis)
    return jntloc

def createSpine():
    #rN() = rN()
    for i in range (0, mc.intField(spineCount, query = True, value = True)):
        spine = mc.spaceLocator(n = rN()+"_Loc_SPINE_" + str(i))
        if i == 0:
            mc.parent(spine, rN()+"_Loc_ROOT")            
        else:
            mc.parent(spine, rN()+"_Loc_SPINE_"+str(i-1))
        mc.scale(1,1,1, spine)
        mc.move(0, 110 + (15 * i), 2, spine)



def SetScale(component, axis):
    for i in axis:
        mc.setAttr(component + ".localScale" + i, locScale)

####Delete####
def deleteLocators():
    nodes = mc.ls(rN()+"_Loc_*")
    mc.delete(nodes)

def deleteJoints():
    nodes = mc.ls(rN()+"_jnt_*")
    mc.delete(nodes)


####Create Rig####
def createJoints():
    if mc.objExists("RIG"):
        print "Rig already exists"
    else:
        jointGRP = mc.group(em = True, name = rN()+"_jnt_GRP")

        ##create spine joints

        root = mc.ls("*_Loc_ROOT")

        allSpines = mc.ls("*_Loc_SPINE_*", type = "locator")
        spine = mc.listRelatives(*allSpines, p = True, f= True)

        rootPos = mc.xform(root, q = True, t = True, ws = True)
        rootJoint = mc.joint(radius = 4, p = rootPos, name = rN()+"_jnt_Root")
        for i, s in enumerate(spine):
            pos = mc.xform(s, q = True, t = True, ws = True)
            j = mc.joint(radius = 4, p = pos, name = rN()+"_jnt_Spine_"+str(i))
