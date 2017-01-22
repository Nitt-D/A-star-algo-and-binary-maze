import numpy
from heapq import *

## A* ALGO IS USED BY US TO FIND THE COORDINATES BETWEEN GIVEN SOURCE SINK PAIR
## AS A* IS FAST PERFORMING WHEN SOURCE AND SINK ARE KNOWN
## AND SOURCE AND SINK PAIR IS FOUND BY DIJSKTRA ALGO IN OUR PROGRAM
'''---------------------------------------------------------------------------
    The path returned here does not have its starting point(or initial point)
    appended here because then path_length would be counted one more as the
    function len() returns length starting from 1(min) thus one node is counted
    even though it doesn't add to path(either starting point or ending point)
----------------------------------------------------------------------------'''
def dist_between(a,b):
    c = numpy.array(a)^2 + numpy.array(b)^2
    return int(c[0])                            ##HEURISTIC DISTANCE BETWEEN POINTS (as specified in PROBLEM-STATEMENT).
                                                ##It can be changed to heuristics distance if diagonal carries different weight of movement

def astar(array, start, goal):                  ##Main Program

    adjacent_neighbours = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)] ## ADJACENT BLOCKS

    closed_set = set()
    from_where_it_came = {}
    gscores = {start:0}                         ## The gscores is the base score of the block and is
                                                ## simply the incremental cost of moving from the start block to next block
    
    fscores = {start:dist_between(start, goal)} ##The fscores is simply the addition of gscores and Heuristic distance and represents
                                                ##the total cost of the path via the current block
    our_heap = []

    heappush(our_heap, (fscores[start], start)) ##Push the block onto the heap, maintaining the heap invariant
    
    while our_heap:

        current = heappop(our_heap)[1]          ##POP UNTIL EMPTY

        if current == goal: 
            data = []
            while current in from_where_it_came:
                data.append(current)
                current = from_where_it_came[current]
            return data,len(data)               ##return path and length of path


        closed_set.add(current)                 ##ADD TO CLOSED SET 
        for i, j in adjacent_neighbours:
            adjacent_neighbour = current[0] + i, current[1] + j            
            tentative_g_score = gscores[current] + dist_between(current, adjacent_neighbour) ##tentative gscores
            if 0 <= adjacent_neighbour[0] < array.shape[0]:
                if 0 <= adjacent_neighbour[1] < array.shape[1]:                
                    if array[adjacent_neighbour[0]][adjacent_neighbour[1]] == 0:             ## Wall Detected(non traverseval)  
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if adjacent_neighbour in closed_set and tentative_g_score >= gscores.get(adjacent_neighbour, 0):
                continue
                
            if  tentative_g_score < gscores.get(adjacent_neighbour, 0) or adjacent_neighbour not in [i[1]for i in our_heap]:
                from_where_it_came[adjacent_neighbour] = current
                gscores[adjacent_neighbour] = tentative_g_score
                fscores[adjacent_neighbour] = tentative_g_score + dist_between(adjacent_neighbour, goal)
                heappush(our_heap, (fscores[adjacent_neighbour], adjacent_neighbour))               
                
    return False,200            ##return false if path does not found and 200 for length of path for comparison
