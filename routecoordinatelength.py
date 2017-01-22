import numpy as np
from astaralgo import *

##AStar algo is used over dijsktra algo because of the weigths that can be easily assigned to heuristics and also just
##by changing heuristics we can set different weights to path i.e diagonal path and straight path can be assigned
##different cost of movements

def CoordinateAndLength(grid_map):
    grid_map=np.array(grid_map)
    length_compare=200                                                  ## IF NO PATH FOUND PATH VALUE WILLL BE 200 (just for comparison purposes(it can be any value but greater than maximum length of path that can exist)) 
    for i in range(0,grid_map.shape[0]):                                ## if shape of the grid_map is not square or of fixed length
        if grid_map[13][i]==1:                                          ## CHECKING IF TRAVERSEVAL
            temp_init=(13,i)                                            ## INITIAL COORDINATE  TO COMPARED WITH SEVERAL STARTS FOR ANY SHORTEST PATH
            for j in range(0,grid_map.shape[1]):        
                if grid_map[0][j]==1:                                   ## CHECKING IF TRAVERSEVAL
                    temp_goal=(0,j)                                     ## INITIALIZING GOAL, ONE OF SEVERAL GOALS FOR ANY SHORTEST PATH
                    path,length=astar(grid_map,temp_init,temp_goal)     ## STORING RETURNED VALUE
                    if length < length_compare:                         ## COMPARING RETURNED VALUE
                        length_compare=length
                        init=temp_init                                  ##final starting point
                        goal=temp_goal                                  ##final ending point

    path2=[]
    if length_compare<200:
        path,length_compare=astar(grid_map,init,goal)
        path.append(init)                   ## appending initial starting point as it was not appended
                                            ## in A-Star algo from where it was returned and the reason is given at top of astaralgo.py file
        for i in range(0,len(path)):          ##exchanging of row and column i.e Swapping and adding 1 to both to make it as per given by eYantra    
            path2.append((path[i][1]+1,path[i][0]+1))

        del path    
        return path2,length_compare          ## returning path and length between starting and goal coordinates 
    else:
        return False,0                      ## returning false if no coordinates are found and length is set to zero(just for returning purpose)
                    
