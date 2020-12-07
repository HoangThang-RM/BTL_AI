import heapq

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
            iter = endNode
            while track[iter] != startNode:
                trueWay.append(iter)
                iter = track[iter]
            trueWay.append(startNode)
            trueWay.reverse()
            print(trueWay)
            return
        # neighborNodes = tmp.distanceTo.keys()
        for neighborNode in tmp.distanceTo.keys():
            if(neighborNode not in visited):
                visited.append(neighborNode)
                heapq.heappush(MO,pointList[neighborNode])
    return []

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