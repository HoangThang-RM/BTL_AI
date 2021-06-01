import heapq
import copy
DEPTH = 30

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
    if(startNode not in pointList.keys()):
        #print('Khong co start Node tuong ung voi de bai')
        return []
    MO = []
    visited = []
    visited.append(startNode)
    heapq.heappush(MO,pointList[startNode])
    DONG = []
    while(len(MO) > 0):
        tmp = heapq.heappop(MO)
        #print(f'**{tmp.name}**')
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
            #print(trueWay)
            return trueWay
        # neighborNodes = tmp.distanceTo.keys()
        for neighborNode in tmp.distanceTo.keys():
            if(neighborNode not in visited):
                visited.append(neighborNode)
                heapq.heappush(MO,pointList[neighborNode])
    return []

#=======================================A*===========================================#

def starA(pointList,startNode,endNode):
    if(startNode not in pointList.keys()):
        #print('Khong co start Node tuong ung voi de bai')
        return []

    MO = [] #hang doi uu tien - cay nhi phan
    DONG = [] # chuoi binh thuong
    start = pointList[startNode]
    heapq.heappush(MO,Way(' ',start.name,[],start.heuristic,0.0))
    while(len(MO) > 0):
        tmpW = heapq.heappop(MO) ## Way not Node
        
        #print(f'{tmpW._lastNode} : {tmpW._cost} --------{tmpW._heuEN}')
        if(tmpW._lastNode in DONG):
            continue
        if(tmpW._lastNode in endNode):
            #print(f'{tmpW._firstNode}'+ tmpW._lastNode)
            return tmpW._way
        DONG.append(tmpW._lastNode)
        for neighborNode in pointList[tmpW._lastNode].distanceTo.keys():
            myFloat = tmpW._cost + pointList[tmpW._lastNode].distanceTo[neighborNode]
            #print(f'{myFloat}' + f' == {pointList[tmpW._lastNode].distanceTo[neighborNode]}')
            newWay = tmpW._way.copy()
            pushItem = Way(
                tmpW._firstNode+tmpW._lastNode,
                neighborNode,
                newWay,
                pointList[neighborNode].heuristic,
                myFloat
            )
            heapq.heappush(MO,pushItem)
        #for x in MO:
            #print(x._firstNode, ' - ', x._lastNode , ' - ' , x._heuEN , ' - ' , x._cost)
    return []

#=======================================At===========================================#

def At(pointList,startNode,endNode):
    if(startNode not in pointList.keys()):
        #print('Khong co start Node tuong ung voi de bai')
        return []
    
    MO = [] #hang doi uu tien - cay nhi phan
    DONG = [] # chuoi binh thuong
    start = pointList[startNode]
    heapq.heappush(MO,Way(' ',start.name,[],0.0,0.0))
    while(len(MO) > 0):
        tmpW = heapq.heappop(MO) ## Way not Node
        
        #print(f'{tmpW._lastNode} : {tmpW._cost} --------{tmpW._heuEN}')
        if(tmpW._lastNode in DONG):
            continue
        if(tmpW._lastNode in endNode):
            #print(f'{tmpW._firstNode}'+ tmpW._lastNode)
            return tmpW._way
        DONG.append(tmpW._lastNode)
        for neighborNode in pointList[tmpW._lastNode].distanceTo.keys():
            myFloat = tmpW._cost + pointList[tmpW._lastNode].distanceTo[neighborNode]
            #print(f'{myFloat}' + f' == {pointList[tmpW._lastNode].distanceTo[neighborNode]}')
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
    h = 0
    g = cal_cost(matrix,matrixEnd,height,width)
    f = h + g
    firstWay = {"coor":target,"h":h,"g":g,"f":f}
    #Khởi tạo MO với ma trận ban đầu và Way
    MO = [[matrix,[firstWay]]]  
    depth = 0
    while(MO != []):
        depth = depth + 1
        newMO = []
        for mtx in MO:
            if(cal_cost(mtx[0],matrixEnd,height,width) == 0): 
                return {"matrix":matrix,"listWay":mtx[1],"height":height,"width":width,"isResult":True}
        
        #Lặp MO để tìm hướng đi tiếp theo
        for mtx in MO:
            way = mtx[1]
            newMO.extend(move(mtx[0],matrixEnd,way,h,height,width))

        #Thuật toán lập nài DEPTH lần nếu vẫn chưa tìm được
        #thông báo đã tìm depth lần vãn chưa tìm được đích
        if(depth >= DEPTH):
            break
        
        MO = newMO
        h = h + 1
    
    return {"matrix":matrix,"listWay":MO.pop(0)[1],"height":height,"width":width,"isResult":False}

#hàm chọn vị trí tiếp theo cần di chuyển
def move(matrix,matrixEnd,way,h,height,width):
    #vị trí ô hiện tại
    row = way[-1]["coor"][0]
    column = way[-1]["coor"][1]
    #vị trí cha trc khi di chuyển đến ô hiện tại
    if(len(way) < 2):
        oldTarget = way[-1]["coor"]
    else:
        oldTarget = way[-2]["coor"]

    h = h + 1
    g = 0
    f = 0
    listMatrix = []
    tmpListMatrix = []
    first = True

    #4 vị trí ô có thể di chuyển lên,xuống,trái,phải
    move = [(row-1,column),(row+1,column),(row,column-1),(row,column+1)]

    for coor in move:
        #nếu mà trùng với vị trí cha thì bỏ qua
        if(coor == oldTarget):
            continue
        
        #nếu toa độ ô di chuyển không đúng thì bỏ qua
        if(coor[0] < 0 or coor[0] >= height or coor[1] < 0 or coor[1] >= width):
            continue

        row_ = coor[0]
        column_ = coor[1]
        tmpMatrix = copy.deepcopy(matrix)
        
        #swap
        tempVal = tmpMatrix[row][column]
        tmpMatrix[row][column] = tmpMatrix[row_][column_]
        tmpMatrix[row_][column_] = tempVal
        
        tmpG = cal_cost(tmpMatrix,matrixEnd,height,width)
        tmpF = h + tmpG

        #nếu f chưa là min thì ta đổi lại giá trị cho f
        if(f >= tmpF or first):
            f = tmpF
            tmpWay = copy.deepcopy(way)
            first = False
            #thêm vị trí vào danh sách đường đi và giá trị các hàm f,g,h
            tmpWay.append({"coor":coor,"h":h,"g":tmpG,"f":f})
            tmpListMatrix.append([tmpMatrix,tmpWay,f])
    
    #lọc lại những vị trí mà có giá trị bằng min
    for mtx in tmpListMatrix:
        if(mtx[2] == f):
            listMatrix.append([mtx[0],mtx[1]])
    
    return listMatrix

#Tính số ô không đúng so với đáp án
def cal_cost(matrix,matrixEnd,height,width):
    cost = 0
    for i in range(height):
        for j in range(width):
            if(matrix[i][j] != matrixEnd[i][j] and matrixEnd[i][j] != ''):
                cost = cost + 1
    return cost
