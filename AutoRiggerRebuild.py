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

locatorDictionary = {}
jointDictionary = {}
controllerDictionary = {}

jntParentDict = {}