
'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
##################################################################################################################
'''-----------------------------------------------------------------------------------------------------------------
 pretty much of the stuffs are already separated out into different python files for better understanding
------------------------------------------------------------------------------------------------------------------'''
##################################################################################################################
'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''






import cv2
import numpy as np
from routecoordinatelength import *  ## to find length and path using A-Star algo

def detectCellVal(img_gray,grid_map):

        for j in range(0,2):                    ## as there are only two images 0 and 1
        ##-------------------------------------------------------------
        ##      READ DIGITS HERE
            digits='digits/'+str(j)+'.jpg'
            check_digits=cv2.imread(digits)
            check_digits_gray=cv2.cvtColor(check_digits,cv2.COLOR_BGR2GRAY) ## converting RGB image to GRAY format
        ##-------------------------------------------------------------
        ##      TEMPLATE MATCHING HERE
            check_digits=cv2.imread(digits)
            check_digits_gray=cv2.cvtColor(check_digits,cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray,check_digits_gray,cv2.TM_CCOEFF_NORMED)

        ##--------------------------------------------------------------
        ##      THRESHOLDING
            if j==0:
                thresh=.45
            else:
                thresh=.42

        ##---------------------------------------------------------------
        ##      COMPARISON FOR INTERESTED REGION
            loc = np.where(res>thresh)
        ##---------------------------------------------------------------
        ##      WRITING ON GRID_MAP
            for k in range(0,len(loc[0])):
                a=loc[0][k]/50
                b=loc[1][k]/50
                grid_map[a][b]=j
	return grid_map

############################################################################################
# solveGrid finds the shortest path,
# between valid grid cell in the start row
# and valid grid cell in the destination row
# solveGrid(grid_map)
# Return the route_path and route_length

def solveGrid(grid_map):
	route_length=False
	path=[]
	route_path=[]
	#your code here
	path,route_length = CoordinateAndLength(grid_map) ## CoordinateAndLength() is a user defined function in routecoordinatelength.py and  what it does is written in respective snippets
        if route_length!=0:              
                for i in range(len(path)-1,-1,-1):              ##The path returned was starting from uppermost row thus changing it here to start from end row i.e. Start Row
                        route_path.append(path[i]) 
        return route_path, route_length
############################################################################################

