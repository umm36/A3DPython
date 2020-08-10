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

mc.button(l = "Scream", w = 175, c = "HowthefuckdoImakeControls()")
mc.button(l = "GenerateControls", w = 175, c = "HowthefuckdoImakeControls()")

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
            {"wristPos":[(43*offset,93.7, 3.3), "Arm", "Wrist", "Elbow"]}
            ]
            
            #Thumb finger joints
            dictThumbJnts = [
            {"thumbBasePos":[(41.5*offset, 93, 7.2), "Hand", "ThumbBase", "Wrist"]},
            {"thumb1Pos":[(40.8*offset, 89.7, 9.4), "Hand", "Thumb1", "ThumbBase"]},
            {"thumb2Pos":[(40.4*offset, 85.6, 11), "Hand", "ThumbTip", "Thumb1"]}
            ]
            
            #Index finger joints
            dictIndexJnts = [
            {"indexBasePos":[(43.9*offset, 92.6, 5.3), "Hand", "IndexFingerBase", "Wrist"]},
            {"index1Pos":[(45.8*offset, 84.4, 8.7), "Hand", "IndexFinger1", "IndexFingerBase"]},
            {"index2Pos":[(46*offset, 81.3, 9.6), "Hand", "IndexFinger2", "IndexFinger1"]},
            {"index3Pos":[(45.3*offset, 78.3, 10.9), "Hand", "IndexFingerTip", "IndexFinger2"]}
            ]
            
            #Middle finger joints
            dictMiddleJnts = [
            {"middleBasePos":[(44.7*offset, 92.1, 3.6), "Hand", "MiddleFingerBase", "Wrist"]},
            {"middle1Pos":[(46.5*offset, 84.2, 5.7), "Hand", "MiddleFinger1", "MiddleFingerBase"]},
            {"middle2Pos":[(46.8*offset, 80.1, 6.6), "Hand", "MiddleFinger2", "MiddleFinger1"]},
            {"middle3Pos":[(45.7*offset, 76.2, 7.8), "Hand", "MiddleFingerTip", "MiddleFinger2"]}
            ]
            
            #Ring finger joints
            dictRingJnts = [
            {"ringBasePos":[(44.2*offset, 91.7, 2.4), "Hand", "RingFingerBase", "Wrist"]},
            {"ring1Pos":[(46*offset, 83.4, 3.1), "Hand", "RingFinger1", "RingFingerBase"]},
            {"ring2Pos":[(45.9*offset, 79.8, 3.7), "Hand", "RingFinger2", "RingFinger1"]},
            {"ring3Pos":[(44.5*offset, 75.6, 5), "Hand", "RingFingerTip", "RingFinger2"]}
            ]
            
            #Pinky finger joints
            dictPinkyJnts = [
            {"pinkyBasePos":[(42.9*offset, 91.1, 0.7), "Hand", "PinkyFingerBase", "Wrist"]},
            {"pinky1Pos":[(44.4*offset, 83.5, 0.7), "Hand", "PinkyFinger1", "PinkyFingerBase"]},
            {"pinky2Pos":[(44*offset, 80.1, 0.8), "Hand", "PinkyFinger2", "PinkyFinger1"]},
            {"pinky3Pos":[(43.1*offset, 77.7, 1.3), "Hand", "PinkyFingerTip", "PinkyFinger2"]}
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
    rigSwitch = ["_IK", "_FK", "_Bind"]                                                             #defines the types of rigs
    if mc.objExists(rN()+"_jnt_GRP"):                                                               #if the joint group already exists
        print "Rig already exists"                                                                  #do nothing
    elif mc.objExists(rN()+"_Loc_Master"):                                                          #otherwise if the loc master group works, 
        jointGRP = mc.group(em = True, name = rN()+"_jnt_GRP")                                      #Creates joint group

        for armJnts in mc.listRelatives("*_Loc_Arm*", type = "locator"):                            #for every object that has Loc_Arm in it:
            locListArms.append(mc.pickWalk(armJnts, direction = "Up")[0])                           #add it to the list of arm joints
        for legJnts in mc.listRelatives("*_Loc_Leg*", type = "locator"):                            #Likewise for Leg
            locListLegs.append(mc.pickWalk(legJnts, direction = "Up")[0])                           #""
        for handJnts in mc.listRelatives("*_Loc_Hand*", type = "locator"):                          #for every object that has Loc_Hand in it:
            locListHands.append(mc.pickWalk(handJnts, direction = "Up")[0])                         #add it to the list of hand joints

############################################################################################################################################
        ####Build Spine
        mc.select(clear = True)                                                                     #clear selection.
        root = mc.ls("*_Loc_ROOT")                                                                  #defines the root locator
        allSpines = mc.ls("*_Loc_SPINE*", type = "locator")                                         #lists all spine locators
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
            else:                                                                                   #if it's not either of these,
                mc.parent(key, "humanBody", absolute = True)                                        #"un-parent" it
                mc.parent(key, value, absolute = True)                                              #then parent it according to the dictionary entry.
            mc.select(clear = True)                                                                 #deselect.

def makeLimbs(jointList, rig):                                                                      
    for counter, loc in enumerate(jointList):                                                       #for each thing and location in the locator list
        if counter + 1 < len(jointList):                                                            #if the thing isn't the last thing in the list:
            jParent = mc.pickWalk(loc, direction = "Up")[0].replace("_Loc_","_jnt_") + rig          #parent is whatever the locator is parented to, but joint, rather than locator, and add the rig.           
            pos = mc.xform(loc, query = True, translation = True, worldSpace = True)                #get the position of the locator
            jointName = loc.replace("_Loc_","_jnt_")                                                #set the name of the joint
            mc.select(clear = True)                                                                 #clear selection.
            jnt = mc.joint(name = jointName + rig, radius = 4)                                      #creates jnt as a joint with the correct name and a radius of 4.
            mc.xform(jnt, translation = pos)                                                        #move the joint to the position it belongs.
            conDelete = mc.aimConstraint(locListArms[counter+1], jnt)                               #creates an aim constraint from the joint just made looking at the next item in the list.
            parentDict.update({jnt: jParent})                                                       #add the parent and the joint to a dictionary
            mc.delete(conDelete)                                                                    #delete the constraint

        elif counter == len(locListArms)-1:                                                         #if this IS the last thing in the list                
            jParent = mc.pickWalk(loc, direction = "Up")[0].replace("_Loc_","_jnt_") + rig          #do
            pos = mc.xform(loc, query = True, translation = True, worldSpace = True)                #the
            jointName = loc.replace("_Loc_","_jnt_")                                                #same
            mc.select(clear = True)                                                                 #thing
            jnt = mc.joint(name = rN()+ jointName + rig, radius = 4)                                #without
            mc.xform(jnt, translation = pos)                                                        #the
            parentDict.update({jnt: jParent})                                                       #constraint
            mc.select(clear = True)
############################################################################################################################################


def makeHands(handDictionary):
    for i, loc in enumerate(handDictionary):                                                        #for each locator in LocListHands,
        if i + 1 < len(handDictionary):                                                             #if the thing isn't the last thing in the list:
            jointName = loc.replace("_Loc_","_jnt_")
            pos = mc.xform(loc, query = True, translation = True, worldSpace = True)
            jnt = mc.joint(name = jointName, radius = 4)                                            #spawn a joint based on the name,
            mc.xform(jnt, translation = pos)
            mc.select(clear = True)
            conDelete = mc.aimConstraint(handDictionary[i+1], jnt)                                  #creates an aim constraint from the joint just made looking at the next item in the list.
            mc.delete(conDelete)                                                                    #delete the constraint
            #jParent = mc.pickWalk(loc, direction = "Up")[0].replace("_Loc_","_jnt_")
            #parentDict.update({jnt: jParent})                                                       #add the parent and the joint to a dictionary          
        
        elif i == len(handDictionary)-1:
            #jParent = mc.pickWalk(loc, direction = "Up")[0].replace("_Loc_","_jnt_")
            jointName = loc.replace("_Loc_","_jnt_")
            pos = mc.xform(loc, query = True, translation = True, worldSpace = True)
            jnt = mc.joint(name = jointName, radius = 4)                                            #spawn a joint based on the name,
            mc.xform(jnt, translation = pos)
            mc.select(clear = True)
        
        for i, "base" in enumerate(handDicionary):
            
        
            
            
                                                                                                    #make and delete an aim constraint to the next locator to get correct alignment.
                                                                                                    #if locator's parent is wrist, (or if finger is "base")
                                                                                                    #parent joint to "wrist"
                                                                                                    #otherwise if
                                                                                                    #parent each joint to the associated join of the locators parent

    


    print "Making hands bones"
    wrists = mc.ls("*_Wrist", type = "locator")
    print wrists
    for root in wrists:
        for key, v in dict.items():
            print "hi"    
    
    ##Help##
    #What process do I follow to get each finger spawned in a chain and parent the base to the wrist?


####Delete####
def deleteLocators():
    nodes = mc.ls(rN()+"_Loc_*")
    mc.delete(nodes)



def deleteJoints():
    nodes = mc.ls(rN()+"_jnt_*")
    mc.delete(nodes)
    locListArms = []
    locListLegs = []
    locListHands = []
    
    print locListArms, locListLegs, locListHands



def SetScale(component, axis): #Currently unused.
    for i in axis:
        mc.setAttr(component + ".localScale" + i, locScale)
        
def BuildControls(dictArray, side, function):
    print "sob"
    ##HELP## #How do I edit curves to make them look fancy so I can align them to the joints?
    
def HowdoIbindshit():
    print "cry"