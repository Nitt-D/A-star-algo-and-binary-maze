import cv2
import numpy as np
from Intermediate import *

N_images=input('input no. of images (max 7): ')
grid_line_x = 15
grid_line_y = 15
m=700/(grid_line_x-1)
n=700/(grid_line_y-1)
###Stores the route lengths detected in all the test images, maximum N route lengths only
route_length_result=[[0 for i in range(grid_line_y-1)] for j in range(N_images)]
###Stores the route paths detected in all the tested images, maximum N route paths only
route_path_result=[[]for k in range(N_images)]
###Stores the numbers detected for all the tested images, maximum N images
grid_map_result = [ [ [0 for i in range(grid_line_y-1)] for j in range(grid_line_x-1) ] for k in range(N_images) ]


for k in range(1,N_images+1):
    grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
    imgpath='task2sets/task2_img_'+str(k)+'.jpg'
    route_length=0#stores the length of the valid route found in the image
    route_path=[] #stores the valid route_path found in the image
    img_rgb = cv2.imread(imgpath)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) #converts RGB to GRAY image
    #calling detectCellVal method to identify numbers in the grid cells and storing those in the grid_map array
    grid_map=detectCellVal(img_gray,grid_map)
    #calling solveGrid method to create a route betwwen the start row and the destination row, returning the route as route_path and length of the route as route_length
    route_path,route_length=solveGrid(grid_map)
    grid_map_result[k-1]=grid_map
    route_length_result[k-1]=route_length
    route_path_result[k-1]=route_path
    #printing the grid_map
    print (grid_map)
    #printing the results of the route detected in the image
    if(route_length==0):
        print "No path found"
    else:
        print " route length", route_length
        print " route path", route_path
            
    #drawing the route path found on the image
    if route_path:
        for i in range(0,len(route_path)-1):
            ci,ri=route_path[i][0]-1,route_path[i][1]-1     ##INITIAL COORDINATE
            cf,rf=route_path[i+1][0]-1,route_path[i+1][1]-1 ##NEXT ADJACENT COORDINATE
            cv2.line(img_rgb,(m*cf+m/2,n*rf+n/2),(m*ci+m/2,n*ri+n/2),[255,0,0],3)       ## converting indexes to coordinating pixel position plus
                                                                                            ## adding the center offset
    else:
        print 'No Path Found'
    ###############################your code snippet ends#############################################
    cv2.imshow('task2_img_'+str(k),img_rgb)
    cv2.imwrite('outputs/task2_img_'+str(k)+'.jpg',img_rgb)
    cv2.waitKey()#press escape to continue
