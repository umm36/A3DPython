import maya.cmds as mc

##setup##
#def loadUI():

if mc.window("HAR", query = True, exists = True):
    mc.deleteUI("HAR")
mc.window("HAR", title = "Human Auto Rigger", widthHeight = (200, 40))
mc.rowColumnLayout("Column1", parent = "HAR", adjustableColumn = True)
mc.button(l = "Create Locators", w = 200, c = "createLocators()")
mc.button(l = "Delete Locators", w = 200, c = "deleteLocators()")  
      
mc.text("Spine Count", l = "Spine Count")
spineCount = mc.intField(minValue = 1, maxValue = 10, value = 4) 
       
mc.text("Finger Count", l = "Finger Count")
fingerCount = mc.intField(minValue = 1, maxValue = 10, value = 4)  
      
mc.text("Finger Joints", l = "Finger Joints")
fingerJoints = mc.intField(minValue = 1, maxValue = 10, value = 3) 
       
mc.text("Rig Name", l = "Rig Name")    
mc.textField("rigName", parent = "Column1", placeholderText = "Character Name/IDCode")
mc.showWindow()

#loadUI()

def rN(): #   rN()+
    userInput = mc.textField("rigName", query = True, text = True)
    return userInput

def bS(side):
    if side == 1:
        bodyside = "L"
    else:
        bodyside = "R"
    return bodyside

##Scripting##

def createLocators():
    if mc.objExists(rN()+"_Loc_Master"):
        print 'Loc_Master already exists.'
    else:
        baseGroup = mc.group(em = True, name = rN()+"_Loc_Master")        
        mc.scale(10,10,10, baseGroup)
        root = mc.spaceLocator(n = rN()+"_Loc_ROOT")
        mc.move(0,95,2, rN()+"_Loc_ROOT")
        mc.parent(root, rN()+"_Loc_Master")
        createSpine()

def createSpine():
    for i in range (0, mc.intField(spineCount, query = True, value = True)):
        spine = mc.spaceLocator(n = rN()+"_Loc_SPINE_" + str(i+1))
        if i == 0:
            mc.parent(spine, rN()+"_Loc_ROOT")            
        else:
            mc.parent(spine, rN()+"_Loc_SPINE_"+str(i))
        mc.scale(1,1,1, spine)
        mc.move(0, 110 + (15 * i), 2, spine)
    createArms(1)
    createArms(-1)
    createLegs(1)
    createLegs(-1)

def createArms(side):
    if side == 1:
        if mc.objExists(rN()+"_L_Arm_GRP"):
            print "Arms already exist."
        else:
            L_arm = mc.group(em = True, name = rN()+"_L_Arm_GRP")
            mc.scale(side,1,1,L_arm)
            mc.parent(L_arm, rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 1))
            mc.move(12.3*side,148,-1.4,L_arm)
            mc.rotate(0,0,0,L_arm)
            
            L_clavicle = mc.spaceLocator(n = rN()+"_Loc_L_Arm_Clavicle")
            mc.move(12.3*side,148,-1.4, L_clavicle)
            mc.parent(L_clavicle, L_arm)
            mc.scale(1,1,1,L_clavicle)
            mc.rotate(0,0,0,L_clavicle)

            L_shoulder = mc.spaceLocator(n = rN()+"_Loc_L_Arm_Shoulder")
            mc.move(19.8*side,143,-1.4, L_shoulder)
            mc.parent(L_shoulder, L_clavicle)
            mc.scale(1,1,1,L_shoulder)
            mc.rotate(0,0,0,L_shoulder)
            
            L_elbow = mc.spaceLocator(n = rN()+"_Loc_L_Arm_Elbow") #Elbow
            mc.move(30.3*side,117.6,-2.6, L_elbow)
            mc.parent(L_elbow, L_shoulder)
            mc.scale(1,1,1,L_elbow)
            mc.rotate(0,0,0,L_elbow)
            
            L_wrist = mc.spaceLocator(n = rN()+"_Loc_L_Arm_Wrist") #Wrist
            mc.move(43*side,93.7,3.3, L_wrist)
            mc.parent(L_wrist, L_elbow)
            mc.scale(1,1,1,L_wrist)
            mc.rotate(0,0,0,L_wrist)
            
    else:
        if mc.objExists(rN()+"_R_Arm_GRP"):
            print "Arms already exist."
        else:
            R_arm = mc.group(em = True, name = rN()+"_R_Arm_GRP")
            mc.parent(R_arm, rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 1))
            mc.scale(side,1,1,R_arm)
            mc.move(12.3*side,148,-1.4,R_arm)
            mc.rotate(0,0,0,R_arm)            
 
            R_clavicle = mc.spaceLocator(n = rN()+"_Loc_R_Arm_Clavicle")
            mc.move(12.3*side,148,-1.4, R_clavicle)
            mc.parent(R_clavicle, R_arm)           
            mc.scale(1,1,1,R_clavicle)
            mc.rotate(0,0,0,R_clavicle)

            R_shoulder = mc.spaceLocator(n = rN()+"_Loc_R_Arm_Shoulder")
            mc.move(19.8*side,143,-1.4, R_shoulder)
            mc.parent(R_shoulder, R_clavicle)
            mc.scale(1,1,1,R_shoulder)
            mc.rotate(0,0,0,R_shoulder)
            
            R_elbow = mc.spaceLocator(n = rN()+"_Loc_R_Arm_Elbow") #Elbow
            mc.move(30.3*side,117.6,-2.6, R_elbow)
            mc.parent(R_elbow, R_shoulder)
            mc.scale(1,1,1,R_elbow)
            mc.rotate(0,0,0,R_elbow)
            
            R_wrist = mc.spaceLocator(n = rN()+"_Loc_R_Arm_Wrist") #Wrist
            mc.move(43*side,93.7,3.3, R_wrist)
            mc.parent(R_wrist, R_elbow)
            mc.scale(1,1,1,R_wrist)
            mc.rotate(0,0,0,R_wrist)
            
def createLegs(side):
    if side == 1:
        if mc.objExists(rN()+"_L_Leg_GRP"):
            print "Arms already exist."
        else:
            L_leg = mc.group(em = True, name = rN()+"_L_Leg_GRP")
            mc.scale(side,1,1,L_leg)
            mc.parent(L_leg, rN()+"_Loc_ROOT")
            mc.move(9.9*side,87.8,1.7,L_leg)
            mc.rotate(0,0,0,L_leg)
            
            L_hip = mc.spaceLocator(n = rN()+"_Loc_L_Leg_Hip")
            mc.move(9.9*side,87.8,1.7, L_hip)
            mc.parent(L_hip, L_leg)
            mc.scale(1,1,1,L_hip)
            mc.rotate(0,0,0,L_hip)

            L_knee = mc.spaceLocator(n = rN()+"_Loc_L_Leg_Knee")
            mc.move(11.9*side,46.4,1.1, L_knee)
            mc.parent(L_knee, L_hip)
            mc.scale(1,1,1,L_knee)
            mc.rotate(0,0,0,L_knee)
            
            L_ankle = mc.spaceLocator(n = rN()+"_Loc_L_Leg_Ankle") #Elbow
            mc.move(14.8*side,2.4,-3.8, L_ankle)
            mc.parent(L_ankle, L_knee)
            mc.scale(1,1,1,L_ankle)
            mc.rotate(0,0,0,L_ankle)
            
            L_toes = mc.spaceLocator(n = rN()+"_Loc_L_Leg_Toes") #Wrist
            mc.move(17*side,2.7,7.8, L_toes)
            mc.parent(L_toes, L_ankle)
            mc.scale(1,1,1,L_toes)
            mc.rotate(0,0,0,L_toes)
    else:
        if mc.objExists(rN()+"_R_Leg_GRP"):
            print "Legs already exist."
        else:
            R_leg = mc.group(em = True, name = rN()+"_R_Leg_GRP")
            mc.scale(side,1,1,R_leg)
            mc.parent(R_leg, rN()+"_Loc_ROOT")
            mc.move(9.9*side,87.8,1.7,R_leg)
            mc.rotate(0,0,0,R_leg)
            
            R_hip = mc.spaceLocator(n = rN()+"_Loc_R_Leg_Hip")
            mc.move(9.9*side,87.8,1.7, R_hip)
            mc.parent(R_hip, R_leg)
            mc.scale(1,1,1,R_hip)
            mc.rotate(0,0,0,R_hip)

            R_knee = mc.spaceLocator(n = rN()+"_Loc_R_Leg_Knee")
            mc.move(11.9*side,46.4,1.1, R_knee)
            mc.parent(R_knee, R_hip)
            mc.scale(1,1,1,R_knee)
            mc.rotate(0,0,0,R_knee)
            
            R_ankle = mc.spaceLocator(n = rN()+"_Loc_R_Leg_Ankle") #Elbow
            mc.move(14.8*side,2.4,-3.8, R_ankle)
            mc.parent(R_ankle, R_knee)
            mc.scale(1,1,1,R_ankle)
            mc.rotate(0,0,0,R_ankle)
            
            R_toes = mc.spaceLocator(n = rN()+"_Loc_R_Leg_Toes") #Wrist
            mc.move(17*side,2.7,7.8, R_toes)
            mc.parent(R_toes, R_ankle)
            mc.scale(1,1,1,R_toes)
            mc.rotate(0,0,0,R_toes)
    
    
    print bS(side)
    



def deleteLocators():
    nodes = mc.ls(rN()+"_Loc_*")
    mc.delete(nodes)