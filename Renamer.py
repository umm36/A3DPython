import maya.cmds as mc

if mc.window("Renamer", query = True, exists = True):
    mc.deleteUI("Renamer")
mc.window("Renamer", title = "Renamer", widthHeight = (175, 40))
mc.rowColumnLayout("Column1", parent = "Renamer", adjustableColumn = True, nc = 2)
#UI to enter in what text you want replaced with what
mc.text("OldName", l = "replace")
mc.textField("OldNameField", parent = "Column1", placeholderText = "")
mc.text("NewName", l = "with...")
mc.textField("NewNameField", parent = "Column1", placeholderText = "")
mc.button(l = "Rename", c = "rename()")

mc.showWindow()
def rename():
    selection = mc.ls(sl=True)
    oldname = mc.textField("OldNameField", query = True, text = True) #gets the 'replace' text field
    newname = mc.textField("NewNameField", query = True, text = True) #gets the 'with...' text field

    for i in selection:
        newitemname = i.replace(oldname, newname) #replaces the pieces of text
        mc.rename(i, newitemname)