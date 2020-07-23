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

##Scripting##

def createLocators():
    if mc.objExists(rN()+"_Loc_Master"):
        print 'Loc_Master already exists.'
    else:
        baseGroup = mc.group(em = True, name = rN()+"_Loc_Master")        
        mc.scale(1,1,1, baseGroup)
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

def createArms(side):
    if side == 1:
        if mc.objExists(rN()+"_L_Arm_GRP"):
            print "Arms already exist."
        else:
            L_arm = mc.group(em = True, name = rN()+"_L_Arm_GRP")
            mc.parent(L_arm, rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 1))
            mc.move(12.3*side,149,-1.4,L_arm)
            
            L_clavicle = mc.spaceLocator(n = rN()+"_Loc_L_Arm_Clavicle")
            mc.move(19.8*side,143,-1.4, L_clavicle)
            mc.parent(L_clavicle, L_arm)

            L_shoulder = mc.spaceLocator(n = rN()+"_Loc_L_Arm_Shoulder")
            mc.move(12.3*side,148,-1.4, L_shoulder)
            mc.parent(L_shoulder, L_clavicle)
            
    else:
        if mc.objExists(rN()+"_R_Arm_GRP"):
            print "Arms already exist."
        else:
            R_arm = mc.group(em = True, name = rN()+"_R_Arm_GRP")
            mc.parent(R_arm, rN()+"_Loc_SPINE_"+str(mc.intField(spineCount, query = True, value = True) - 1))
            mc.move(12.3*side,149,-1.4,R_arm)
 
            R_clavicle = mc.spaceLocator(n = rN()+"_Loc_R_Arm_Clavicle")
            mc.move(19.8*side,143,-1.4, R_clavicle)
            mc.parent(R_clavicle, R_arm)           

            R_shoulder = mc.spaceLocator(n = rN()+"_Loc_R_Arm_Shoulder")
            mc.move(12.3*side,148,-1.4, R_shoulder)
            mc.parent(R_shoulder, R_clavicle)
            
            


def deleteLocators():
    nodes = mc.ls(rN()+"_Loc_*")
    mc.delete(nodes)