import maya.cmds as mc

##setup##
#def loadUI():


if mc.window("HAR", query = True, exists = True):
    mc.deleteUI("HAR")
mc.window("HAR", title = "Human Auto Rigger", widthHeight = (175, 40))
mc.rowColumnLayout("Column1", parent = "HAR", adjustableColumn = True, nc = 2)
mc.button(l = "Create Locators", c = "CreateLocators()")
mc.button(l = "Delete Locators", w = 175, c = "deleteLocators()")  
mc.button(l = "Create Joints", c = "createJoints()")
mc.button(l = "Delete Joints", w = 175, c = "deleteJoints()")
      
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
        #print rN() + "_Loc_Master"
        
        baseGroup = mc.group(em = True, name = rN() + "_Loc_Master")
        mc.scale(10,10,10, baseGroup)

        root = mc.spaceLocator(n = rN()+"_Loc_ROOT")
        mc.move(0,95,2, rN()+"_Loc_ROOT")
        mc.parent(root, rN()+"_Loc_Master")
    for side in sides:
        if mc.objExists(rN()+"_" + side + "_Arm_GRP"):
            print "Arms already exist."
        else:
            #Re-setting offset side
            if side == "R":
                offset = -1
            
                ##HELP## #Is this dictionary needed?
                '''
                dictHandDictionaries = {
                "ArmDict":"dictArmJnts",
                "ThumbDict":"dictThumbJnts",
                "IndexDict":"dictIndexJnts",
                "MiddleDict":"dictMiddleJnts",
                "RingDict":"dictRingJnts",
                "PinkyDict":"dictPinkyJnts"
                }
                '''

            if side == "L":
                createSpine()
            
            clavicalParent = rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2)
            hipParent = rN()+"_Loc_ROOT"
            
            #Dictionary of details for thumb joints. <<dictionary Key:[Coordinates (needs input), "Limb", "Name of this joint", "Name of the parent joint"]>>
            
            ##HELP## #Set up dictionaries outside Create Locators function so both create locators and create Joints functions can call the data inside.
            
            #Arm joint dictionary.
            dictArmArray = [
            {"claviclePos":[(12.3*offset,148, -1.4), "Arm", "Clavicle", clavicalParent]},
            {"shoulderPos":[(19.8*offset,143, -1.4), "Arm", "Shoulder", "Clavicle"]},
            {"elbowPos":[(30.3*offset,117.6, -2.6), "Arm", "Elbow", "Shoulder"]},
            {"wristPos":[(43*offset,93.7, 3.3), "Arm", "Wrist", "Elbow"]}
            ]
            
            #Thumb finger joints
            dictThumbJnts = [
            {"thumbBasePos":[(41.5*offset, 93, 7.2), "Arm", "ThumbBase", "Wrist"]},
            {"thumb1Pos":[(40.8*offset, 89.7, 9.4), "Arm", "Thumb1", "ThumbBase"]},
            {"thumb2Pos":[(40.4*offset, 85.6, 11), "Arm", "Thumb2", "Thumb1"]}
            ]
            
            #Index finger joints
            dictIndexJnts = [
            {"indexBasePos":[(43.9*offset, 92.6, 5.3), "Arm", "IndexFingerBase", "Wrist"]},
            {"index1Pos":[(45.8*offset, 84.4, 8.7), "Arm", "IndexFinger1", "IndexFingerBase"]},
            {"index2Pos":[(46*offset, 81.3, 9.6), "Arm", "IndexFinger2", "IndexFinger1"]},
            {"index3Pos":[(45.3*offset, 78.3, 10.9), "Arm", "IndexFinger3", "IndexFinger2"]}
            ]
            
            #Middle finger joints
            dictMiddleJnts = [
            {"middleBasePos":[(44.7*offset, 92.1, 3.6), "Arm", "MiddleFingerBase", "Wrist"]},
            {"middle1Pos":[(46.5*offset, 84.2, 5.7), "Arm", "MiddleFinger1", "MiddleFingerBase"]},
            {"middle2Pos":[(46.8*offset, 80.1, 6.6), "Arm", "MiddleFinger2", "MiddleFinger1"]},
            {"middle3Pos":[(45.7*offset, 76.2, 7.8), "Arm", "MiddleFinger3", "MiddleFinger2"]}
            ]
            
            #Ring finger joints
            dictRingJnts = [
            {"ringBasePos":[(44.2*offset, 91.7, 2.4), "Arm", "RingFingerBase", "Wrist"]},
            {"ring1Pos":[(46*offset, 83.4, 3.1), "Arm", "RingFinger1", "RingFingerBase"]},
            {"ring2Pos":[(45.9*offset, 79.8, 3.7), "Arm", "RingFinger2", "RingFinger1"]},
            {"ring3Pos":[(44.5*offset, 75.6, 5), "Arm", "RingFinger3", "RingFinger2"]}
            ]
            
            #Pinky finger joints
            dictPinkyJnts = [
            {"pinkyBasePos":[(42.9*offset, 91.1, 0.7), "Arm", "PinkyFingerBase", "Wrist"]},
            {"pinky1Pos":[(44.4*offset, 83.5, 0.7), "Arm", "PinkyFinger1", "PinkyFingerBase"]},
            {"pinky2Pos":[(44*offset, 80.1, 0.8), "Arm", "PinkyFinger2", "PinkyFinger1"]},
            {"pinky3Pos":[(43.1*offset, 77.7, 1.3), "Arm", "PinkyFinger3", "PinkyFinger2"]}
            ]
            
            #Arm joint dictionary
            dictLegJnts = [
            {"hipPos":[(9.9*offset, 87.8, 1.7), "Leg", "Hip", hipParent]},
            {"kneePos":[(11.9*offset, 46.4, 1.1), "Leg", "Knee", "Hip"]},
            {"anklePos":[(14.8*offset, 2.4, -3.8), "Leg", "Ankle", "Knee"]},
            {"toesPos":[(17*offset, 2.7, 7.8), "Leg", "Toes", "Ankle"]}
            ]
            
            dictionaryArray = [
            dictArmArray,
            dictThumbJnts,
            dictIndexJnts,
            dictMiddleJnts,
            dictRingJnts,
            dictPinkyJnts,
            dictLegJnts
            ]
            
            spawnLocators(dictionaryArray, side)
            mc.select(rN() + "_Loc_Master")
            
def spawnLocators(dictArray, side):
    for dictionary in dictArray:
        for dict in dictionary:
            for key, v in dict.items():
                
                jntloc = mc.spaceLocator(n = rN() + "_Loc_" + v[1] + "_" + side + "_" + v[2])                
                mc.move(v[0][0],v[0][1],v[0][2], jntloc)
                 
                if key != "claviclePos" and key != "hipPos":
                    #print key
                    mc.parent(jntloc , rN()+"_Loc_"+ v[1] + "_" + side + "_" + v[3])
                elif key == "claviclePos":
                    mc.parent(jntloc, rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2))
                else:                    
                    mc.parent(jntloc, rN()+"_Loc_ROOT")

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

'''
####Create Rig####
def createJoints():
    sides = ["L", "R"] ##HELP## #pass in the function, or sit in here?
    if mc.objExists(rN()+"_jnt_GRP"):
        print "Rig already exists"
    else:
        jointGRP = mc.group(em = True, name = rN()+"_jnt_GRP") #Creates joint group
'''
'''
        #defines locations of all the spine locators
        root = mc.ls("*_Loc_ROOT")
        allSpines = mc.ls("*_Loc_SPINE_*", type = "locator")
        spine = mc.listRelatives(*allSpines, p = True, f= True)
        
        #create spine joints based on locations of spine locators.
        rootPos = mc.xform(root, q = True, t = True, ws = True)
        rootJoint = mc.joint(radius = 4, p = rootPos, name = rN()+"_jnt_Root")
        
        for i, s in enumerate(spine):
            pos = mc.xform(s, q = True, t = True, ws = True)
            j = mc.joint(radius = 4, p = pos, name = rN()+"_jnt_Spine_"+str(i))
'''
'''
        ##___________________________
        
        
        #defines locations of all the spine locators
        root = mc.ls("*_Loc_ROOT")
        allSpines = mc.ls("*_Loc_*", type = "locator")
        spine = mc.listRelatives(*allSpines, p = True, f= True)
        
        #create spine joints based on locations of spine locators.
        rootPos = mc.xform(root, q = True, t = True, ws = True)
        rootJoint = mc.joint(radius = 4, p = rootPos, name = rN()+"_jnt_Root")
        
        for i, s in enumerate(spine):
            pos = mc.xform(s, q = True, t = True, ws = True)
            j = mc.joint(radius = 4, p = pos, name = rN()+"_jnt_Spine_"+str(i))
'''

def createJoints(dictArray, side):
    rigSwitch = ["IK", "FK", "Bind"]
    if mc.objExists(rN()+"_jnt_GRP"):
        print "Rig already exists"
    else:
        jointGRP = mc.group(em = True, name = rN()+"_jnt_GRP") #Creates joint group
        #defines locations of all the spine locators
        root = mc.ls("*_Loc_ROOT")
        allSpines = mc.ls("*_Loc_*", type = "locator")
        spine = mc.listRelatives(*allSpines, p = True, f= True)
        
        #create spine joints based on locations of spine locators.
        rootPos = mc.xform(root, q = True, t = True, ws = True)
        rootJoint = mc.joint(radius = 4, p = rootPos, name = rN()+"_jnt_Root")
        
        for switch in rigSwitch:
            for dictionary in dictArray:
                for dict in dictionary:
                    for key, v in dict.items():
                        joint = mc.joint(radius = 4, n = rN() + "_jnt_" + v[1] + "_" + side + "_" + v[2] + switch)                
                        mc.move(rN() + "_Loc_" + v[1] + "_" + side + "_" + v[2], joint)
                        
                        if key != "claviclePos" and key != "hipPos":
                            mc.parent(joint , rN()+"_jnt_"+ v[1] + "_" + side + "_" + v[3] + switch)
                        elif key == "claviclePos":
                            mc.parent(joint, rN()+"_jnt_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2))
                        else:                    
                            mc.parent(joint, rN()+"_jnt_ROOT")







'''        
        ##HELP##       
        for i in sides:
            for key, value in dictThumbJnts.items():
                for v in value:
                    j = mc.joint(radius = 4, p = [0], name = rN()+"_jnt_"+ v[2] + "_" + i + "_" + v[1]) #NO! these lines are for spawning locators, not joints.
                    mc.parent(j , rN()+"_jnt_"+ v[2] + "_" + i + "_" + v[3])
'''