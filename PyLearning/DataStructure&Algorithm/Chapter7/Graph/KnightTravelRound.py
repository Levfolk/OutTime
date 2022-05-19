#骑士周游问题
from pythonds.graphs import Graph, Vertex

#Code_7.6 knightGraph函数，构建并遍历n x n的棋盘，调用genLegalMoves函数来记录某一格开始的所有合理走法
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1])
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, col, bdSize):
    return row * bdSize + col

#Code7.7 genLegalMoves函数和legalCoord函数，genLegalMoves函数接受骑士在棋盘的位置，并生成8中可能的走法；legalCoord辅助函数确认走法是合理的
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):
    if x >= 0 and x <bdSize:
        return True
    else:
        return False

#Code_7.8 knightTour函数，通过深度优先搜索实现骑士周游
def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i  = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

#Code_7.9 加速搜索过程，选择下一个要访问的顶点至关重要，orderByAvail函数用于替换Code_7.8中的u.getConnections
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.appen((c, v))
    resList.sort(key = lambda x: x[0])
    return[y[1] for y in resList]
