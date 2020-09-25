#IKFK Ctrl first
#FK second
#IK third
#Bind last

#your IK Switch doesn't need a already made IKFK attribute, it will make one if one doesn't exist

import maya.cmds as cmds

selection = cmds.ls(sl=True)
FK = selection[1]
IK = selection[2]
bind = selection[3]
ctrl = selection[0]

if cmds.objExists(ctrl+".IKFK"):
    pass
else:
    cmds.select(ctrl)
    cmds.addAttr(ln="IKFK", at="double", min=0, max=1, dv=0, k=True)
    
switch = cmds.shadingNode("blendColors", au=True, n= bind+"_switch")
cmds.connectAttr(FK+".rotate", switch+".color1")
cmds.connectAttr(IK+".rotate", switch+".color2")
cmds.connectAttr(switch+".output", bind+".rotate")
cmds.connectAttr(ctrl+".IKFK", switch+".blender")
cmds.select(ctrl)