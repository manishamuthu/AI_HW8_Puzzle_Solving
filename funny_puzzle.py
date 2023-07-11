import heapq


def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    # [2,5,1,4,3,6,7,0,0]
    # 0 3 6 mod=0
    # 1 4 7 mod=1
    # 2 5 8 mod=2
    # 251
    # 436
    # 700
    # # [1,2,3,4,5,6,7,0,0]
    # 123
    # 456
    # 700
    # for y split it up: first three, second three, last three (divide index+1 by 3
    # for x split it up by index 1 2 or 3, and what the index is supposed to be
    # use mod and // 7/2 would give you 3
    distance = 0;
    for n in from_state:
        xdist = 0
        ydist = 0
        #first calc y dist

        fromIndex= from_state.index(n)
        toIndex= to_state.index(n)
        if(n!=0):
            ydif= abs(fromIndex//3 - (toIndex//3))
            # now calc xdist
            xdif= abs(fromIndex%3 - (toIndex%3))
            distance+=ydif+xdif

        # print(fromIndex)
        # print(toIndex)
    return distance

def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """


    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    # [2,5,1,4,3,6,7,0,0]
    # 0 3 6 mod=0
    # 1 4 7 mod=1
    # 2 5 8 mod=2
    # 251
    # 436
    # 700

    #should give 3 successor states
    # [2,5,1,4,0,6,7,3,0]
    # [2,5,1,4,3,0,7,0,6]
    # [2,5,1,4,3,6,0,7,0]

    # find the index of the 0, then chekc if the y's and x's around it are zeros.
    # if not, switch it.
    succ_states=[]

    for i,n in enumerate (state):
        temp=state.copy()
        if(n==0):
            currIndex=i
            #start with y
            if(currIndex//3==0 and (temp[currIndex+3])!=0):
                #only switch with y below
                temp[currIndex],temp[currIndex+3]=temp[currIndex+3],temp[currIndex]
                succ_states.append(temp)
                temp = state.copy()
            elif (currIndex // 3 == 1):
                # switch with y below and above
                if((temp[currIndex+3])!=0):
                    temp[currIndex], temp[currIndex+ 3] = temp[currIndex+ 3], temp[currIndex]
                    succ_states.append(temp)
                    temp=state.copy()
                if ((temp[currIndex -3]) != 0):
                    temp[currIndex], temp[currIndex -3] = temp[currIndex - 3], temp[currIndex]
                    succ_states.append(temp)
                    temp=state.copy()
            elif (currIndex // 3 == 2 and (temp[currIndex-3])!=0):
                # only switch with y above
                temp[currIndex], temp[currIndex-3] = temp[currIndex -3 ], temp[currIndex]
                succ_states.append(temp)
                temp=state.copy()
            #now x
            if (currIndex % 3 == 0 and (temp[currIndex+1])!=0):
                    # only switch with x to risucc_states.append(temp)ght
                    temp[currIndex], temp[currIndex + 1] = temp[currIndex + 1], temp[currIndex]
                    succ_states.append(temp)
                    temp = state.copy()
            elif (currIndex %3 == 1 ):
                    # switch with x to right and left
                    if(temp[currIndex + 1]!=0):
                        temp[currIndex], temp[currIndex + 1] = temp[currIndex + 1], temp[currIndex]
                        succ_states.append(temp)
                        temp = state.copy()
                    if(temp[currIndex-1]!=0):
                        temp[currIndex], temp[currIndex - 1] = temp[currIndex - 1], temp[currIndex]
                        succ_states.append(temp)
                        temp = state.copy()
            elif (currIndex %3 == 2 and (temp[currIndex-1])!=0):
                    # only switch with x to left
                    temp[currIndex], temp[currIndex - 1] = temp[currIndex - 1], temp[currIndex]
                    succ_states.append(temp)
                    temp = state.copy()

    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """


    # #instruction of A* from slides:
    # #put starting node on priority called OPEN
    # #if open==empty, exit
    # #n=pop OPEN; so that the cost is a min (so priority queue should be dictated by cost)
    # # if n is goal the exit
    # # else get all successors (n') of n, pointing back to n
    # #    if n' isn't in open or closed, get g, h, and f of n'
    # #      put n' on open
    # #    else if n' is on open or closed already, check if g(n') is lower for the new n'
    #         # if g(n') is lower then redirect the pointers to this g(n')
    #         # put n' on open
    # #repeat
    #
    # OPENpq=[]
    # CLOSEDpq=[]
    # g=0;#cost from the starting node, number of moves so far
    # h=get_manhattan_distance(state)
    # cost=g+h
    # parent_index=-1
    # heapq.heappush(OPENpq, (cost, state, (g, h, parent_index)))
    # #OPENpq.append(state)
    # pointerDict={}
    # #currState=state.copy()
    # #repeat below until the goal state has been reached
    # if(len(OPENpq)==0):
    #     return 0; #change this so that it makes sense
    # x,n,z=heapq.heappop(OPENpq)
    # heapq.heappush(CLOSEDpq, (cost, n, (g, h, parent_index)))
    # if(n==goal_state):
    #     return 1; #change this so that it makes en
    # successors = get_succ(n)
    # g=g+1
    # #COME BACK TO THIS pointerDict[n]=successors,g #may or may not work
    # childSuccessors=get_succ(successors)
    # for s in childSuccessors:
    #     if OPENpq.count(s)==0 and CLOSEDpq.count(s)==0: #idk if this will work cause theres tech 2 items in each pq pos
    #         h = get_manhattan_distance(s)
    #         cost=g+1+h
    #         heapq.heappush(OPENpq, (cost, s, (g+1, h, g)))
    #    #elif OPENpq.count(s)!=0:
    #
    #
    #
    #
    # h=get_manhattan_distance(state) #the val of heuristic function (manhattan)
    # cost=g+h
    # parent_index=-1 #initial state w/o parent
    # heapq.heappush(OPENpq, (cost, state, (g, h, parent_index)))
    # print(OPENpq)
    #
    #
    #
    # for s in successors:
    #     get_manhattan_distance(s)
    #
    #
    # #what is the man_dist is the same for multiple?
    #

    openpq = []
    closepq = []
    track = []  # trace exists to track the nodes we consider part of the best solution
    g = 0
    h = get_manhattan_distance(state)
    parent_index = -1
    childNum = 0
    parentNum = -1
    #declared all the variables we need
    mlength = 0

    heapq.heappush(openpq, (g + h, state, (g, h, parent_index), childNum, parentNum))
    #push the child and paret numb rn so that we can track it later ..... too complicated to do in other ways
    closepq.append(state)
    childNum +=1
    finalState=[]
    finalPop=[]
    finalPI=0
    #need to declare final vars to use outside of the below while
    while openpq:
        mlength = max(mlength, len(openpq))

        currPop = heapq.heappop(openpq)
        currState = currPop[1]
        closepq.append(currState)
        tempG = currPop[2][0]
        currChild = currPop[3]
        currPI = currPop[2][2]

        #pop the first one and get the info you need from that using the []

        if currState != goal_state:
            #find the nect poss best move
            g = tempG + 1
            currSuccessors = get_succ(currState)
            parent_index = currPI + 1
            parentNum = currChild
            for successor in currSuccessors:
                if successor not in closepq:
                    h = get_manhattan_distance(successor)
                    heapq.heappush(openpq, (g + h, successor, (g, h, parent_index), childNum, parentNum))
                    childNum += 1
            track.append(currPop)
        else:
            finalState=currState
            finalPop=currPop
            finalPI=currPI
            break

    final_path = [finalState]
    track_PI = finalPop[4]
    while finalPI != -1:
        for t in track:
            if t[2][2] == finalPI - 1 :
                if t[3] == track_PI:
                    final_path.append(t[1])
                    track_PI = t[4]
                    finalPI= t[2][2]
                    break
    #write out the whole final path
    moveNumber = 0
    while final_path:
        current = final_path.pop()
        print(current, "h={}".format(get_manhattan_distance(current)), "moves:", moveNumber)
        moveNumber += 1
    print("Max queue length:", mlength)


if __name__ == "__main__":
    """
    Feel free to write your own test code here to examine the correctness of your functions. 
    Note that this part will not be graded.
    """