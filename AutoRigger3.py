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

            #spineNum = str(mc.intField(spineCount, query = True, value = True) -1) #Needless currently.
            
            #Arm Locators
            #claviclePos = [12.3*offset,148,-1.4]
            #shoulderPos = [19.8*offset,143,-1.4]
            #elbowPos = [30.3*offset,117.6,-2.6]
            #wristPos = [43*offset,93.7,3.3]
            
            #Leg Locators
            #hipPos = [9.9*offset, 87.8, 1.7]
            #kneePos = [11.9*offset, 46.4, 1.1]
            #anklePos = [14.8*offset, 2.4, -3.8]
            #toesPos = [17*offset, 2.7, 7.8]
            
            
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

            
 
            
            
            
            
            '''
            #Thumb finger joints
            dictThumbJnts = {
            "thumbBasePos":[(1*offset, 1 ,1), "Arm", "ThumbBase", "Wrist"],
            "thumb1Pos":[(1*offset, 2 ,1), "Arm", "Thumb1", "Arm", "ThumbBase"],
            "thumb2Pos":[(1*offset, 3 ,1), "Arm", "Thumb2", "Arm", "Thumb1"]
            }
            
            #Index finger joints
            dictIndexJnts = {
            "indexBasePos":[(2*offset, 1 ,1), "Arm", "IndexFingerBase", "Wrist"],
            "index1Pos":[(2*offset, 2 ,1), "Arm", "IndexFinger1", "IndexBase"],
            "index2Pos":[(2*offset, 3 ,1), "Arm", "IndexFinger2", "Index1"],
            "index3Pos":[(2*offset, 4 ,1), "Arm", "IndexFinger3", "Index2"]
            }
            
            #Middle finger joints
            dictMiddleJnts = {
            "middleBasePos":[(3*offset, 1 ,1), "Arm", "MiddleFingerBase", "Wrist"],
            "middle1Pos":[(3*offset, 2 ,1), "Arm", "MiddleFinger1", "MiddleBase"],
            "middle2Pos":[(3*offset, 3 ,1), "Arm", "MiddleFinger2", "Middle1"],
            "middle3Pos":[(3*offset, 4 ,1), "Arm", "MiddleFinger3", "Middle2"]
            }
            
            #Ring finger joints
            dictRingJnts = {
            "ringBasePos":[(4*offset, 1 ,1), "Arm", "RingFingerBase", "Wrist"],
            "ring1Pos":[(4*offset, 2 ,1), "Arm", "RingFinger1", "RingBase"],
            "ring2Pos":[(4*offset, 3 ,1), "Arm", "RingFinger2", "Ring1"],
            "ring3Pos":[(4*offset, 4 ,1), "Arm", "RingFinger3", "Ring2"]
            }
            
            #Pinky finger joints
            dictPinkyJnts = {
            "pinkyBasePos":[(5*offset, 1 ,1), "Arm", "PinkyFingerBase", "Wrist"],
            "pinky1Pos":[(5*offset, 2 ,1), "Arm", "PinkyFinger1", "PinkyBase"],
            "pinky2Pos":[(5*offset, 3 ,1), "Arm", "PinkyFinger2", "Pinky1"],
            "pinky3Pos":[(5*offset, 4 ,1), "Arm", "PinkyFinger3", "Pinky2"]
            }
            
            #Arm joint dictionary
            dictLegJnts = {
            "hipPos":[(9.9*offset, 87.8, 1.7), "Arm", "Hip", "hipParent"], ##HELP## #hipParent #how to link this?
            "kneePos":[(11.9*offset, 46.4, 1.1), "Arm", "Knee", "Hip"],
            "anklePos":[(14.8*offset, 2.4, -3.8), "Arm", "Ankle", "Knee"],
            "toesPos":[(17*offset, 2.7, 7.8), "Arm", "Toes", "Ankle"]
            }
            '''
            
            
            #prevLoc = ""
            if side == "L":
                createSpine()
            
            clavicalParent = rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2)
            hipParent = rN()+"_Loc_ROOT"
            
            
            #Dictionary of details for thumb joints. <<dictionary Key:[Coordinates (needs input), "Limb", "Name of this joint", "Name of the parent joint"]>>
            
            ##HELP## #Set up dictionaries outside Create Locators function so both create locators and create Joints functions can call the data inside. ##Done?
            
            #Arm joint dictionary.
            dictArray = [{"claviclePos":[(12.3*offset,148,-1.4), "Arm", "Clavicle", clavicalParent]}, ##HELP## #clavicalParent #how to link this?
            {"shoulderPos":[(19.8*offset,143,-1.4), "Arm", "Shoulder", "Clavicle"]},
            {"elbowPos":[(30.3*offset,117.6,-2.6), "Arm", "Elbow", "Shoulder"]},
            {"wristPos":[(43*offset,93.7,3.3), "Arm", "Wrist", "Elbow"]}
            ]
            
            #array = [1,2,3,4,5]
            
            #print dictArmJnts[0] 
            
            
            
            
            '''
            ####CBB: could be refined/optimised using dictionaries
            Clavicle = spawnLocators(clavicalParent, claviclePos, "Arm", "Clavicle", side)
            Shoulder = spawnLocators(Clavicle, shoulderPos, "Arm", "Shoulder", side)
            Elbow = spawnLocators(Shoulder, elbowPos, "Arm", "Elbow", side)
            Wrist = spawnLocators(Elbow, wristPos, "Arm", "Wrist", side)
            Hip = spawnLocators(hipParent, hipPos, "Leg", "Hip", side)
            Knee = spawnLocators(Hip, kneePos, "Leg", "Knee", side)
            Ankle = spawnLocators(Knee, anklePos, "Leg", "Ankle", side)
            Toes = spawnLocators(Ankle, toesPos, "Leg", "Toes", side)
            '''
            
            spawnLocators(dictArray, side)
            
def spawnLocators(array, side):
    
    for dict in array:
        for key, v in dict.items():         #for key, value in dict.items():
            #for v in value: ##HELP##       #code breaks if this is here, but only spawns a single wrist locator.

            '''
            print "\n"
            print "--------------------"
            print key, "\n"
            #print (v[0][0]*offset,v[0][1],v[0][2]), "\n"
            print v[0]
            print v[1]
            print v[2]
            print v[3]
            print "--------------------"
            '''
                   
            jntloc = mc.spaceLocator(n = rN() + "_Loc_" + v[1] + "_" + side + "_" + v[2], position = v[0]) #Add indentation

            if key != "claviclePos" and key != "hipPos":
                print key
                mc.parent(jntloc , rN()+"_Loc_"+ v[1] + "_" + side + "_" + v[3])                               #Add indentation                
            elif key == "claviclePos":
                mc.parent(jntloc, rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2))
            else:
                mc.parent(jntloc, rN()+"_Loc_ROOT")
            
            
            

''' 
####Old spawnLocators, pre dictionary
def spawnLocators(parent, pos, limb, joint, side):
    jntloc = mc.spaceLocator(n = rN()+"_Loc_" + i + "_" + limb + "_" + joint, position = pos)
    #mc.parent(jntloc, parent)
    mc.parent(jntloc , rN()+"_Loc_"+ v[2] + "_" + i + "_" + v[3])
    ##SetScale(jntloc, axis)
    return jntloc
'''

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
    #sides = ["L", "R"] ##HELP## #pass in the function, or sit in here?
    if mc.objExists(rN()+"_jnt_GRP"):
        print "Rig already exists"
    else:
        jointGRP = mc.group(em = True, name = rN()+"_jnt_GRP") #Creates joint group

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
        
        
        ##HELP##
        
        for i in sides:
            for key, value in dictThumbJnts.items():
                for v in value:
                    j = mc.joint(radius = 4, p = [0], name = rN()+"_jnt_"+ v[2] + "_" + i + "_" + v[1]) #NO! these lines are for spawning locators, not joints.
                    mc.parent(j , rN()+"_jnt_"+ v[2] + "_" + i + "_" + v[3])