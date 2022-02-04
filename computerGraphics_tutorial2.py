import maya.cmds as cmds 
import random

#Create UI

if'UI'in globals():
   if cmds.window(UI, exists=True):
       cmds.deleteUI(UI, window=True)

UI = cmds.window(title='House Generator',width=400)

cmds.columnLayout(rowSpacing=10)

cmds.text(label='House Generator')

cmds.showWindow(UI)

#Sliders

cmds.intSliderGrp('width', label='Width', min=1, max=5)
cmds.intSliderGrp('height', label='Height', min=1, max=5)
cmds.intSliderGrp('depth', label='Depth', min=1, max=5)

cmds.checkBox('includeChimney', label='Include Chimney')
cmds.checkBox('includeWindows', label='Include Windows')

cmds.button(label= 'Generate House', command='generateHouse()')
cmds.button(label= 'Generate Random House', command='generateRandomHouse()')

cmds.showWindow(UI)

#Functions

def generateChimney(dimensions):
   chimney =  cmds.polyCube(width=0.2, height=1, depth=0.2)
   cmds.move(dimensions[0]/3.0, dimensions[1] +0.2, dimensions[2]/3.0)

   return chimney

def generateWindowsPrimitives():

   A = cmds.polyCube(width=0.1, height=0.1, depth=0.1)
   cmds.move(0.1,0,0)

   B = cmds.polyCube(width=0.1, height=0.1, depth=0.1)
   cmds.move(-0.1,0,0)

   C = cmds.polyCube(width=0.1, height=0.1, depth=0.1)
   cmds.move(0.1,0.2,0)

   D = cmds.polyCube(width=0.1, height=0.1, depth=0.1)
   cmds.move(-0.1,0.2,0)


   cmds.select(A,B,C,D)
   windowPrimitives = cmds.polyUnite()
   cmds.move(0,0.2,0.5)

   return windowPrimitives

def generateWindows(dimensions,wallSet):

   wallResult = wallSet
   rotation= 0

   for i in range(4):
       windowObject = generateWindowsPrimitives()
       cmds.rotate(0, rotation, 0, pivot=(0,0,0))
       wallResult = cmds.polyCBoolOp(wallResult, windowObject[0], op=2)
       rotation += 90
       
       return wallResult
       
def generateParametricHouse(houseWidth, houseHeight, houseDepth):
    
   #Generate house from incoming parameters

    #Debugging: making sure that the values are correct
    print(houseWidth, houseHeight, houseDepth)

    #Create base
    base= cmds.polyCube(width=houseWidth, height=0.1, depth=houseDepth)

    #Create wall A
    wallA = cmds.polyCube(width=0.05, height=houseHeight, depth=houseDepth)

    #Moving position of wall
    cmds.move(houseWidth/2.0,houseHeight/2.0,0)

    #Wall B
    wallB = cmds.polyCube(width=0.05, height=houseHeight, depth=houseDepth)
    cmds.move(houseWidth/-2.0,houseHeight/2.0,0)

    #Wall C
    wallC = cmds.polyCube(width=houseWidth, height=houseHeight, depth=0.05)
    cmds.move(0,houseHeight/2.0,houseDepth/2.0)

    #Wall D
    wallD = cmds.polyCube(width=houseWidth, height=houseHeight, depth=0.05)
    cmds.move(0,houseHeight/2.0,houseDepth/-2.0)

    cmds.select(wallA, wallB, wallC, wallD)
    #uniting all the walls into one obj

    wallSet=cmds.polyUnite()

    #Create Roof
    roof= cmds.polyCube(width=houseWidth, height=0.35, depth=houseDepth)
    cmds.scale(1.2, 1.2, 1.2)
    cmds.move(0,houseHeight + 0.2,0)
    cmds.select(roof[0] + '.f[1]')
    cmds.polyBevel(offset=0.3)


    #Create chimney

    chimney = []
    if(cmds.checkBox('includeChimney', query=True, value=True) == True):
        chimney = generateChimney([houseWidth, houseHeight, houseDepth])


    #Create Windows
    if(cmds.checkBox('includeWindows', query=True, value=True) == True):
        wallSet= generateWindows ([houseWidth, houseHeight, houseDepth], wallSet)

    if(cmds.checkBox('includeChimney', query=True, value=True) == True):
        finalHouse=cmds.group(base[0], wallSet[0], roof[0], chimney[0])

    else:
        finalHouse=cmds.group(base[0], wallSet[0], roof[0])


def generateHouse():
   #Generating the parametric house

   houseWidth=cmds.intSliderGrp('width', query=True, value=True)
   houseHeight=cmds.intSliderGrp('height', query=True, value=True)
   houseDepth=cmds.intSliderGrp('depth', query=True, value=True)

   #Debugging: making sure that the values are correct
   print(houseWidth, houseHeight, houseDepth)

   generateParametricHouse(houseWidth, houseHeight, houseDepth)
   


def generateRandomHouse():
   #Generating the parametic random house
   
   houseWidth=random.randint(1,5)
   houseHeight=random.randint(1,5)
   houseDepth=random.randint(1,5)
   
   generateParametricHouse(houseWidth, houseHeight, houseDepth)