import maya.cmds as mc

ctrl = mc.circle(c=(0,1,0), nr=(0,1,0))



setRGBColor(ctrl, color)



def setRGBColor(ctrl, color = (1,1,1)):
    
    rgb = ("R","G","B")
    
    mc.setAttr(ctrl + ".overrideEnabled",1)
    mc.setAttr(ctrl + ".overrideRGBColors",1)
    
    for channel, color in zip(rgb, color):
        
        mc.setAttr(ctrl + ".overrideColor%s" %channel, color)