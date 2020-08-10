import maya.cmds as mc

##setup##
if mc.window("HAR", query = True, exists = True):
    mc.deleteUI("HAR")
mc.window("HAR", title = "Human Auto Rigger", widthHeight = (175, 40))
mc.rowColumnLayout("Column1", parent = "HAR", adjustableColumn = True, nc = 2)
mc.button(l = "Create Locators", c = "createLocators()")
mc.button(l = "Delete Locators", w = 175, c = "deleteLocators()")  
mc.button(l = "Create Joints", c = "createJoints()")
mc.button(l = "Delete Joints", w = 175, c = "deleteJoints()")      
mc.text("Spine Count", l = "Spine Count")
spineCount = mc.intField(minValue = 1, maxValue = 10, value = 4)        
mc.text("Finger Count", l = "Finger Count")
fingerCount = mc.intField(minValue = 1, maxValue = 10, value = 4)      
mc.text("Finger Joints", l = "Finger Joints")
fingerJoints = mc.intField(minValue = 1, maxValue = 10, value = 3)

mc.button(l = "GenerateControls", w = 175, c = "BuildControls()")
mc.button(l = "Delete Controls", w = 175, c = "DeleteControls()")

mc.text("Rig Name", l = "Rig Name")    
mc.textField("NameOfRig", parent = "Column1", placeholderText = "Character Name/IDCode")
mc.showWindow()

locListArms = []
locListLegs = []
locListHands = []


parentDict = {}

def rN(): #Rig Name
    userInput = mc.textField("NameOfRig", query = True, text = True)
    return str(userInput)
        
def createLocators():
    #print "Making Locators"
    CreateDictionaries("_Loc_")
    
def createJoints():
    #print "Making Joints"
    CreateDictionaries("_jnt_")
    #reparentBones()
    
def createControls():
    #print "Making Controls"
    CreateDictionaries("_ctl_")

def CreateDictionaries(function):
    sides = ["L", "R"]    
    axis = ["X", "Y", "Z"]
    locScale = 10
    offset = 1

    for side in sides: #runs the whole dictionary script twice, once with side set to "L" once again with "R"
        if function == "_Loc_":
            if side == "R":
                offset = -1        

            clavicalParent = rN()+ function + "SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2)
            hipParent = rN()+ function + "ROOT"
            
            #Dictionary of details for all points. <<dictionary Key:[Coordinates (needs input), "Limb", "Name of this joint", "Name of the parent joint"]>>

            #Arm joint dictionary.
            dictArmArray = [
            {"claviclePos":[(12.3*offset,148, -1.4), "Arm", "Clavicle", clavicalParent]},
            {"shoulderPos":[(19.8*offset,143, -1.4), "Arm", "Shoulder", "Clavicle"]},
            {"elbowPos":[(30.3*offset,117.6, -2.6), "Arm", "Elbow", "Shoulder"]},
            {"wristPos":[(43*offset,93.7, 3.3), "Arm", "Wrist", "Elbow"]},
            {"armEndPos":[(43.7*offset,89.3, 3.5), "Arm", "ZZZ", "Wrist"]}
            ]
            
            #Thumb finger joints
            dictThumbJnts = [
            {"thumbBasePos":[(41.5*offset, 93, 7.2), "Hand", "ThumbBase", "Wrist"]},
            {"thumb1Pos":[(40.8*offset, 89.7, 9.4), "Hand", "Thumb1", "ThumbBase"]},
            {"thumb2Pos":[(40.4*offset, 85.6, 11), "Hand", "Thumb2", "Thumb1"]},
            {"TumbTipPos":[(39.8*offset, 83.1, 12.2), "Hand", "ThumbTip", "Thumb2"]}
            ]
            
            #Index finger joints
            dictIndexJnts = [
            {"indexBasePos":[(43.9*offset, 92.6, 5.3), "Hand", "IndexFingerBase", "Wrist"]},
            {"index1Pos":[(45.8*offset, 84.4, 8.7), "Hand", "IndexFinger1", "IndexFingerBase"]},
            {"index2Pos":[(46*offset, 81.3, 9.6), "Hand", "IndexFinger2", "IndexFinger1"]},
            {"index3Pos":[(45.3*offset, 78.3, 10.9), "Hand", "IndexFinger3", "IndexFinger2"]},
            {"indexTipPos":[(44.3*offset, 76.7, 11.3), "Hand", "IndexFingerTip", "IndexFinger3"]}
            ]
            
            #Middle finger joints
            dictMiddleJnts = [
            {"middleBasePos":[(44.7*offset, 92.1, 3.6), "Hand", "MiddleFingerBase", "Wrist"]},
            {"middle1Pos":[(46.5*offset, 84.2, 5.7), "Hand", "MiddleFinger1", "MiddleFingerBase"]},
            {"middle2Pos":[(46.8*offset, 80.1, 6.6), "Hand", "MiddleFinger2", "MiddleFinger1"]},
            {"middle3Pos":[(45.7*offset, 76.2, 7.8), "Hand", "MiddleFinger3", "MiddleFinger2"]},
            {"middleTipPos":[(44.6*offset, 74.5, 8.6), "Hand", "MiddleFingerTip", "MiddleFinger3"]}
            ]
            
            #Ring finger joints
            dictRingJnts = [
            {"ringBasePos":[(44.2*offset, 91.7, 2.4), "Hand", "RingFingerBase", "Wrist"]},
            {"ring1Pos":[(46*offset, 83.4, 3.1), "Hand", "RingFinger1", "RingFingerBase"]},
            {"ring2Pos":[(45.9*offset, 79.8, 3.7), "Hand", "RingFinger2", "RingFinger1"]},
            {"ring3Pos":[(44.5*offset, 75.6, 5), "Hand", "RingFinger3", "RingFinger2"]},
            {"ringTipPos":[(43.5*offset, 74.2, 5.9), "Hand", "RingFingerTip", "RingFinger3"]}
            ]
            
            #Pinky finger joints
            dictPinkyJnts = [
            {"pinkyBasePos":[(42.9*offset, 91.1, 0.7), "Hand", "PinkyFingerBase", "Wrist"]},
            {"pinky1Pos":[(44.4*offset, 83.5, 0.7), "Hand", "PinkyFinger1", "PinkyFingerBase"]},
            {"pinky2Pos":[(44*offset, 80.1, 0.8), "Hand", "PinkyFinger2", "PinkyFinger1"]},
            {"pinky3Pos":[(43.1*offset, 77.7, 1.3), "Hand", "PinkyFinger3", "PinkyFinger2"]},
            {"pinkyTipPos":[(42*offset, 76.1, 2.2), "Hand", "PinkyFingerTip", "PinkyFinger3"]}
            ]
            
            #Arm joint dictionary
            dictLegJnts = [
            {"hipPos":[(9.9*offset, 87.8, 1.7), "Leg", "Hip", hipParent]},
            {"kneePos":[(11.9*offset, 46.4, 1.1), "Leg", "Knee", "Hip"]},
            {"anklePos":[(14.8*offset, 2.4, -3.8), "Leg", "Ankle", "Knee"]},
            {"toesPos":[(17*offset, 2.7, 7.8), "Leg", "Toes", "Ankle"]}
            ]
            
            fullDictArray = [
            dictArmArray,
            dictThumbJnts,
            dictIndexJnts,
            dictMiddleJnts,
            dictRingJnts,
            dictPinkyJnts,
            dictLegJnts
            ]        
            limbDictArray = [
            dictArmArray,
            dictLegJnts
            ]        
            handDictArray = [
            dictThumbJnts,
            dictIndexJnts,
            dictMiddleJnts,
            dictRingJnts,
            dictPinkyJnts
            ]
            
            spawnLocators(limbDictArray, side, function)
            spawnLocators(handDictArray, side, function)
    if function == "_jnt_": 
        spawnJoints(function)
        #spawnHandJoints(function)
    elif function == "_ctrl_":
        BuildControls(fullDictArray, side, function)
    mc.select(clear = True)



def spawnLocators(dictArray, side, function):                                                   
    if function == "_Loc_" and side == "L":                                                         #Only run this once.
        if mc.objExists(rN()+"_Loc_Master"):                                                        #if the master group already exists
            print '_Loc_Master already exists.'                                                     #do nothing
        else:                                                                                       #otherwise
            baseGroup = mc.group(em = True, name = rN() + "_Loc_Master")                            #make the master group
            root = mc.spaceLocator(n = rN()+"_Loc_ROOT")                                            #defines and creates the ROOT locator.
            mc.move(0,95,2, rN()+"_Loc_ROOT")                                                       #moves it into the correct position
            mc.parent(root, rN()+"_Loc_Master")                                                     #parent the root to the Master group.
            for i in range (0, mc.intField(spineCount, query = True, value = True)):                #for each entry in the list of spines.
                spine = mc.spaceLocator(n = rN()+"_Loc_SPINE_" + str(i))                            #make a spine locator with procedural name.
                if i == 0:                                                                          #if it's the first entry in the spine,
                    mc.parent(spine, rN()+"_Loc_ROOT")                                              #parent to the root.
                else:                                                                               #otherwise
                    mc.parent(spine, rN()+"_Loc_SPINE_"+str(i-1))                                   #parent under the previous spine joint
                mc.move(0, 110 + (15 * i), 2, spine)                                                #move the spine locator into position.
    
    for dictionary in dictArray:                                                                    #look at the collection of dictionaries.
        for dict in dictionary:                                                                     #look at the actual dictionary in the collection.
            for key, v in dict.items():                                                             #look at the items in the dictionaries.
                jntloc = mc.spaceLocator(n = rN() + function + v[1] + "_" + side + "_" + v[2])      #create a locator with appropriate naming conventions.
                mc.move(v[0][0],v[0][1],v[0][2], jntloc)                                            #move the locator into the correct position.
                if "Base"  not in key:                                                              #if the locator is NOT the base of a finger so such:                    
                    if key != "claviclePos" and key != "hipPos":                                    #if it is anything but the hip or clavicle:
                        mc.parent(jntloc , rN()+ function + v[1] + "_" + side + "_" + v[3])         #parent it as the dictionary dictates.
                    elif key == "claviclePos":                                                      #if it's the clavicle:
                        mc.parent(jntloc, rN()+ function + "SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 2))   #parent it to the second to last spine joint
                    else:                                                                           #else
                        mc.parent(jntloc, rN()+ function + "ROOT")                                  #it must be a hip, parent to the root.
                else:                                                                               #if it DOES have 'base' in the name, it's a finger soooooooooooo
                    mc.parent(jntloc, rN()+ function + "Arm" + "_" + side + "_" + "Wrist")          #parent to the wrist.
                    
##############################################################################################################################
def spawnJoints(function):
    rigSwitch = ["_IK", "_FK", "_Bind"]#### Add "_Core" or add _Bind to hands and spine?            #defines the types of rigs
    if mc.objExists(rN()+"_jnt_GRP"):                                                               #if the joint group already exists
        print "Rig already exists"                                                                  #do nothing
    elif mc.objExists(rN()+"_Loc_Master"):                                                          #otherwise if the loc master group works, 
        jointGRP = mc.group(em = True, name = rN()+"_jnt_GRP")                                      #Creates joint group

        for armJnts in mc.listRelatives(rN()+ "_Loc_Arm*", type = "locator"):                            #for every object that has Loc_Arm in it:
            locListArms.append(mc.pickWalk(armJnts, direction = "Up")[0])                           #add it to the list of arm joints
        for legJnts in mc.listRelatives(rN()+ "_Loc_Leg*", type = "locator"):                            #Likewise for Leg
            locListLegs.append(mc.pickWalk(legJnts, direction = "Up")[0])                           #""
        for handJnts in mc.listRelatives(rN()+ "_Loc_Hand*", type = "locator"):                          #for every object that has Loc_Hand in it:
            locListHands.append(mc.pickWalk(handJnts, direction = "Up")[0])                         #add it to the list of hand joints

############################################################################################################################################
        ####Build Spine
        mc.select(clear = True)                                                                     #clear selection.
        root = mc.ls(rN()+"_Loc_ROOT")                                                                  #defines the root locator
        allSpines = mc.ls(rN()+ "_Loc_SPINE*", type = "locator")                                         #lists all spine locators
        spine = mc.listRelatives(allSpines, parent = True, fullPath= True)                          #lists all parents of the spineShape
        rootPos = mc.xform(root, q = True, t = True, ws = True)                                     #get the position of the root locator
        rootJoint = mc.joint(radius = 4, position = rootPos, name = rN()+ function + "ROOT")        #creates the root joint
        mc.parent (rootJoint, jointGRP)                                                             #Parents root joint to the joint group
        for i, s in enumerate(spine):                                                               #for each of the spines in the list
            pos = mc.xform(s, q = True, t = True, ws = True)                                        #set the position of the spine locators
            j = mc.joint(radius = 4, position = pos, name = rN()+ function + "SPINE_"+str(i+1))     #create a spine joint there.
############################################################################################################################################
        ####Build Limbs
        #print locListArms
        for rig in rigSwitch:                                                                       #for each rig of IK FK or Bind            
            makeLimbs(locListArms, rig)                                                             #make the limbs using the list of Arm locators
            makeLimbs(locListLegs, rig)                                                             #make the limbs using the list of Leg locators

        makeHands(locListHands) ##HELP## How do MAKE HANDS ADSLHFASLJDFHDHKFZLSKHT

        for key, value in parentDict.items():                                                       #for everything in the parent dictionary
            if "Clavicle" in key:                                                                   #if the key has 'Clavicle' in it
                mc.parent(key, rN()+"_jnt_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 1)) #parent it to the second to last spine joint.
            elif "Hip" in key:                                                                      #if the key has 'Hip' in it
                mc.parent(key, rN()+"_jnt_ROOT")                                                    #parent it to the root joint.
            elif "Tip" in key or "ZZZ" in key:                
                mc.delete(key)
            else:                                                                                   #if it's not either of these,
                mc.parent(key, "humanBody", absolute = True)                                        #"un-parent" it
                mc.parent(key, value, absolute = True)                                              #then parent it according to the dictionary entry.
            mc.select(clear = True)                                                                 #deselect.

def makeLimbs(jointList, rig):                                                                      
    for counter, loc in enumerate(jointList):                                                       #for each thing and location in the locator list
            jParent = mc.pickWalk(loc, direction = "Up")[0].replace("_Loc_","_jnt_") + rig          #parent is whatever the locator is parented to, but joint, rather than locator, and add the rig.           
            pos = mc.xform(loc, query = True, translation = True, worldSpace = True)                #get the position of the locator
            jointName = loc.replace("_Loc_","_jnt_")                                                #set the name of the joint
            mc.select(clear = True)                                                                 #clear selection.
            jnt = mc.joint(name = jointName + rig, radius = 4)                                      #creates jnt as a joint with the correct name and a radius of 4.
            print jointName ##HELP## #Why does the list get generated alphabetically? I have to name the end of the arm ZZZ so it gets added AFTER the Wrist.
            mc.xform(jnt, translation = pos)                                                        #move the joint to the position it belongs.
            if "ZZZ" not in jnt and "Toes" not in jnt:  ##HELP## #debug: #Replace "ZZZ" with "End"
                conDelete = mc.aimConstraint(jointList[counter+1], jnt)                             #creates an aim constraint from the joint just made looking at the next item in the list.
                mc.delete(conDelete)                                                                #delete the constraint
            parentDict.update({jnt: jParent})                                                       #add the parent and the joint to a dictionary
            mc.select(clear = True)
############################################################################################################################################


def makeHands(handDictionary):
    for i, loc in enumerate(handDictionary):                                                        #for each locator in LocListHands,
        jointName = loc.replace("_Loc_","_jnt_")                                                    #
        pos = mc.xform(loc, query = True, translation = True, worldSpace = True)                    #
        jnt = mc.joint(name = jointName, radius = 1)                                                #spawn a joint based on the name,
        mc.xform(jnt, translation = pos)                                                            #
        mc.select(clear = True)                                                                     #
        if "Tip" not in jnt:                                                                        #if the finger is not a finger tip,
            conDelete = mc.aimConstraint(handDictionary[i+1], jnt)                                  #creates an aim constraint from the joint just made looking at the next item in the list.
            mc.delete(conDelete)                                                                    #delete the constraint
        
        if "Base" in jnt:                                                                           #if locator's parent is a finger "base")
            jParent = mc.pickWalk(loc, direction = "Up")[0].replace("_Loc_","_jnt_") + "_Bind"      #parent the joint to the wrist_bind.
        else:                                                                                       #if locator's parent is not a wrist or a finger "base")
            jParent = mc.pickWalk(loc, direction = "Up")[0].replace("_Loc_","_jnt_")                #parent each joint to the associated join of the locators parent
        parentDict.update({jnt: jParent})                                                           #add the parent and the joint to a dictionary       
        mc.select(clear = True)                                                                     #deselect the pickWalk.

####Delete####
def deleteLocators():
    nodes = mc.ls(rN()+"_Loc_*")
    mc.delete(nodes)

def deleteJoints():
    nodes = mc.ls(rN()+"_jnt_*")
    mc.delete(nodes)

def SetScale(component, axis): #Currently unused.
    for i in axis:
        mc.setAttr(component + ".localScale" + i, locScale)
        
def BuildControls():
    if mc.objExists(rN()+"Controls Group"):
        print "Controls already generated for " + rN()
    else:
        CtrlGrp = mc.group(em = True, name = rN()+"Controls Group")
        allJoints = mc.ls(rN()+"_jnt_*" + "*FK")
        
        for joint in allJoints:            
            
            jntPos = mc.xform(joint, query = True, translation = True, worldSpace = True)
            jntRot = mc.xform(joint, query = True, rotation = True, worldSpace = True)
            ctrl = mc.circle(r = 5, name = rN()+"_ctrl_bob")
            mc.xform(ctrl, translation = jntPos, rotation = jntRot, worldSpace = True)
            mc.rotate(0,90,0,ctrl, relative = True, componentSpace = True)
            
    
    ##HELP## #How do I edit curves to make them look fancy so I can align them to the joints and colour them?
    
def DeleteControls():
    nodes = mc.ls(rN()+"_ctrl*")
    mc.delete(nodes)