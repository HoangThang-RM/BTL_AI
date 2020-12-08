import heapq
import copy
DEPTH = 10

class Way:
    def __init__(self,firstNode = '',lastNode = '',way = [],heuEN=0.0,cost=0.0):
        self._firstNode = firstNode
        self._lastNode = lastNode
        self._heuEN = heuEN
        self._cost = cost
        self._way = way
        if(self._way == None):
            self._way = []
        self._way.append(lastNode)

    def __lt__(self,other):
        return self._heuEN + self._cost < other._heuEN + other._cost
    def __eq__(self,other):
        return self._heuEN + self._cost == other._heuEN + other._cost

#=======================================BeFS===========================================#

def BeFS(pointList,startNode,endNode):
    MO = []
    if(startNode not in pointList.keys()):
        print('Khong co start Node tuong ung voi de bai')
        return
    visited = []
    visited.append(startNode)
    heapq.heappush(MO,pointList[startNode])
    DONG = []
    while(len(MO) > 0):
        tmp = heapq.heappop(MO)
        print(f'**{tmp.name}**')
        DONG.append(tmp.name)
        if(tmp.name in endNode):
            track = {}
            preNodes = []
            preNodes.append(DONG.pop(0))
            trueWay = []
            for d in DONG:
                for preNode in preNodes:
                    if(d in pointList[preNode].distanceTo.keys()):
                        track[d] = preNode
                preNodes.append(d)
            # cac
            iter = tmp.name
            trueWay.append(iter)
            while track[iter] != startNode:
                trueWay.append(track[iter])
                iter = track[iter]
            trueWay.append(startNode)
            trueWay.reverse()
            print(trueWay)
            return trueWay
        # neighborNodes = tmp.distanceTo.keys()
        for neighborNode in tmp.distanceTo.keys():
            if(neighborNode not in visited):
                visited.append(neighborNode)
                heapq.heappush(MO,pointList[neighborNode])
    return []

#=======================================A*===========================================#

def starA(pointList,startNode,endNode):


    for p in pointList.keys():
        print(pointList[p])
        #print(p._name + '->' + p._heuristic)
        #for neighborNode in p._distanceTo.keys():
        #    print(neighborNode + '==' + p._distanceTo[neighborNode])
    MO = [] #hang doi uu tien - cay nhi phan
    DONG = [] # chuoi binh thuong
    start = pointList[startNode]
    heapq.heappush(MO,Way(' ',start.name,[],start.heuristic,0.0))
    while(len(MO) > 0):
        tmpW = heapq.heappop(MO) ## Way not Node
        
        print(f'{tmpW._lastNode} : {tmpW._cost} --------{tmpW._heuEN}')
        if(tmpW._lastNode in DONG):
            continue
        if(tmpW._lastNode in endNode):
            print(f'{tmpW._firstNode}'+ tmpW._lastNode)
            return tmpW._way
        DONG.append(tmpW._lastNode)
        for neighborNode in pointList[tmpW._lastNode].distanceTo.keys():
            myFloat = tmpW._cost + pointList[tmpW._lastNode].distanceTo[neighborNode]
            print(f'{myFloat}' + f' == {pointList[tmpW._lastNode].distanceTo[neighborNode]}')
            newWay = tmpW._way.copy()
            pushItem = Way(
                tmpW._firstNode+tmpW._lastNode,
                neighborNode,
                newWay,
                pointList[neighborNode].heuristic,
                myFloat
            )
            heapq.heappush(MO,pushItem)
        for x in MO:
            print(x._firstNode, ' - ', x._lastNode , ' - ' , x._heuEN , ' - ' , x._cost)
    return []

#=======================================At===========================================#

def At(pointList,startNode,endNode):
    MO = [] #hang doi uu tien - cay nhi phan
    DONG = [] # chuoi binh thuong
    start = pointList[startNode]
    heapq.heappush(MO,Way(' ',start.name,[],0.0,0.0))
    while(len(MO) > 0):
        tmpW = heapq.heappop(MO) ## Way not Node
        
        print(f'{tmpW._lastNode} : {tmpW._cost} --------{tmpW._heuEN}')
        if(tmpW._lastNode in DONG):
            continue
        if(tmpW._lastNode in endNode):
            print(f'{tmpW._firstNode}'+ tmpW._lastNode)
            return tmpW._way
        DONG.append(tmpW._lastNode)
        for neighborNode in pointList[tmpW._lastNode].distanceTo.keys():
            myFloat = tmpW._cost + pointList[tmpW._lastNode].distanceTo[neighborNode]
            print(f'{myFloat}' + f' == {pointList[tmpW._lastNode].distanceTo[neighborNode]}')
            newWay = tmpW._way.copy()
            pushItem = Way(
                tmpW._firstNode+tmpW._lastNode,
                neighborNode,
                newWay,
                0.0,
                myFloat
            )
            heapq.heappush(MO,pushItem)
    return []

#=======================================Akt===========================================#

def Akt_matrix(matrix,matrixEnd,target,height,width):
    MO = can_move(target,target,height,width) #DS cac vi tri di tiep theo
    h = 0
    g = cal_cost(matrix,matrixEnd,height,width)
    f = h + g
    result = {"matrix" : [[copy.deepcopy(matrix),h,g,f]],"height" : height,"width" : width, "isResult" : False,"depth" : DEPTH}
    depth = 0
    while(MO != []):
        depth = depth + 1
        oldTarget = target
        target,f,g,h = move_min(MO,h,matrix,matrixEnd,target,height,width)
        resultMatrix = copy.deepcopy(matrix)
        resTmp = [resultMatrix,h,g,f]
        result["matrix"].append(resTmp)
        
        if(cal_cost(matrix,matrixEnd,height,width) == 0): 
            #print('Da tim duoc ket qua')
            result["isResult"] = True
            break

        if(depth >= DEPTH):
            #print('Da tim',depth,'lan ko tim duoc ket qua')
            break
        MO = can_move(target,oldTarget,height,width) #DS cac vi tri di tiep theo
    
    return result

def move_min(MO,h,matrix,matrixEnd,target,height,width):
    row = target[0]
    column = target[1]
    h = h + 1
    g = 0
    f = 0
    result = (None,None)
    first = True
    for coor in MO:
        row_ = coor[0]
        column_ = coor[1]
        tmpMatrix = copy.deepcopy(matrix)
        #swap
        tempVal = tmpMatrix[row][column]
        tmpMatrix[row][column] = tmpMatrix[row_][column_]
        tmpMatrix[row_][column_] = tempVal
        
        tmpG = cal_cost(tmpMatrix,matrixEnd,height,width)
        tmpF = h + tmpG
        if(f > tmpF or first):
            first = False
            f = tmpF
            g = tmpG
            result = coor

    reI = result[0]
    reJ = result[1]
    
    #swap
    temp = matrix[row][column]
    matrix[row][column] = matrix[reI][reJ]
    matrix[reI][reJ] = temp 
    
    return result,f,g,h

def cal_cost(matrix,matrixEnd,height,width):
    cost = 0
    for i in range(height):
        for j in range(width):
            if(matrix[i][j] != matrixEnd[i][j] and matrixEnd[i][j] != ''):
                cost = cost + 1
    return cost

def can_move(target,oldTarget,height,width):
    i = target[0]
    j = target[1]
    move = []
    if(i == 0):
        if((i+1,j) != oldTarget):
            move.append((i+1,j))
    
    if(i == height-1):
        if((i-1,j) != oldTarget):
            move.append((i-1,j))

    if(j == 0):
        if((i,j+1) != oldTarget):
            move.append((i,j+1))
    
    if(j == width-1):
        if((i,j-1) != oldTarget):
            move.append((i,j-1))

    if(i > 0 and i < height-1):
        if((i+1,j) != oldTarget):
            move.append((i+1,j))
        if((i-1,j) != oldTarget):
            move.append((i-1,j))

    if(j > 0 and j < width-1):
        if((i,j+1) != oldTarget):
            move.append((i,j+1))
        if((i,j-1) != oldTarget):
            move.append((i,j-1))
    
    return move