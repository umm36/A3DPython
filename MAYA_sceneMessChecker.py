# -----------------------------------------------------------------------------
# Is it a mess?  The Maya scene file mess checker
# Kevin Phillips, September 2018
#
# Checks all files loaded into the Maya scene.  Will determine any messed
# up paths and look for missing files.  Use this check pre-Renderfarm or
# use on another workstation to identify issues early.
# -----------------------------------------------------------------------------
# Checks for:
# * What files are loaded
# * If files exist
# * Files use the correct project paths
# * Externally pathed files - naughty!
# -----------------------------------------------------------------------------
# To use in Maya (Shelf):
# 1: Copy this file to documents/maya/####/scripts
# 2: Use this code and save to shelf
#
# try:
#     reload(SceneContentCheck)
# except:
#     import SceneContentCheck
#
# 3: That's it!
# -----------------------------------------------------------------------------

import maya.cmds as cmds
import os.path

# Get the current workspace
prjFolder = cmds.workspace(fn=True, q=True)

# get a list of all files loaded into scene (images, etc)
allFiles = cmds.file(list=True, q=True)

# Get a list of all referenced files currently in the scene
refFiles = []
rf = [ref for ref in cmds.ls(type='reference') if 'RN' in ref]
for r in rf:
    try:
        refFiles.append(cmds.referenceQuery(r,f=True))
    except:
        print "Hmmmm, cannot see a file related to this reference"
        print "Ref was : ",r

# Lets grab the workspace name itself.
wsPath = prjFolder.split("/")
prjWSpace = wsPath[len(wsPath)-1]
wsPath.pop()
prjWSPath = '/'.join(wsPath)

# Log list.  This collects the issues and writes them to disk/display
logList = []
sepLine = '-'*80
sepSS = '. '*40
sepSect = '='*80

logList.append(sepSect)

# The general project details
logList.append('PROJECT DIRECTORY :\n'+prjWSPath)
logList.append('WORKSPACE NAME    :\n'+prjWSpace)

# 01 : Current scene + stats
if 'untitled' in allFiles[0]:
    logList.append('MAYA SCENE :\nNot Saved Yet')
else:
    if prjFolder in allFiles[0]:
        scnName = allFiles[0][len(prjFolder):]
    else:
        scnName = allFiles[0]
    logList.append('MAYA SCENE :\n'+scnName)

logList.append(sepSS)
logList.append('SCENE STATS : ')
logList.append('Total files in Scene : '+str(len(allFiles)-1))
logList.append('Referenced files     : '+str(len(rf)))

# List stats on how many of the files in Maya are scenes, images or other
imgTypes = ['.jpg','.tex','.tx','.png','.exr','.jpeg','.tif','.tiff','.bmp','.psd']
scnTypes = ['.ma','.mb']
othTypes = imgTypes + scnTypes

scnCount = othCount = imgCount = 0
for f in allFiles:
    for typ in imgTypes:
        if typ in f: imgCount+=1
    for typ in scnTypes:
        if typ in f: scnCount+=1
    for typ in othTypes:
        if not typ in f: othCount+=1

logList.append('       > Image files : '+str(imgCount))
logList.append('       > Scene files : '+str(scnCount - 1))
logList.append('       > Other files : '+str(imgCount))

logList.append(sepSect)

# 02 : File paths checked
logList.append('FILE PATH HEALTH CHECK')    

# Check files loaded - externals, and those that exist, but have incorrectly
# been loaded using a physical file path that is different to the project path
chkFiles = True
invPaths = extFiles = invalidFiles = 0
for testFile in allFiles:
    if prjFolder not in testFile:
        if prjWSpace in testFile:
            llMsg = 'Invalid path  : '+testFile
            if testFile in refFiles: llMsg = '(REFERENCE) '+llMsg
            logList.append(llMsg)
            invPaths += 1
            chkFiles = False
        else:
            llMsg = 'External file  : '+testFile
            if testFile in refFiles: llMsg = '(REFERENCE) '+llMsg
            logList.append(llMsg)
            extFiles += 1
            chkFiles = False

if chkFiles: logList.append('No problems detected')
logList.append(sepSS)        
logList.append('FILE PATH SUMMARY : Invalid ('+str(invPaths)+'), External ('+str(extFiles)+')')

logList.append(sepLine)

# 03 : File list and existance checking
# Loop through all the files that were loaded into this Maya project
logList.append('PHYSICAL FILE CHECK')
chkFiles = True
for eachFile in allFiles:
    # Strip any {#} from end of filename.  This occurs when multiple files with same name were bought
    # in (internal Maya numbering, not file name - eg. references, etc)
    if "{" in eachFile: eachFile = eachFile[:eachFile.index("{")]

    # Test to see if there are non-existant files - remapped to the base workspace
    if prjWSpace in eachFile:
        eachFile = prjWSPath + "/" + eachFile[eachFile.index(prjWSpace):]
        if not os.path.exists(eachFile):
            logList.append('Missing : '+eachFile)
            invalidFiles += 1
            chkFiles = False
    else:
        # Test external file paths exist on this machine...
        if not os.path.exists(eachFile):
            logList.append("Missing : "+eachFile)
            invalidFiles += 1
            chkFiles = False
            
if chkFiles: logList.append('No problems detected') 
logList.append(sepSS)       
logList.append('MISSING FILES : ('+str(invalidFiles)+')')
logList.append(sepSect)

# 04 : Print the report...

for line in logList:
    print line

# 05 : Alert the user...

if (invalidFiles + extFiles + invPaths) > 0:    
    cmds.confirmDialog(m='Check Complete - Found Errors - see Script Editor for details',t='DOH!')
else:
    cmds.confirmDialog(m="Check Complete - No file issues detected",t="Awesome!")

# Test done.  If problems...  Give yourself a slap!
