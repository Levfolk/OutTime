#乌龟走迷宫问题

#Code_4.10 迷宫搜索函数
def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    #检查基本情况
    #1.遇到墙
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    #2.遇到已经走过的格子
    if maze[startRow][startColumn] == TRIED:
        return False
    #3.找到出口
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    #否则，依次尝试向4哥方向移动
    found = searchFrom(maze, startRow - 1, startColumn) or searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or searchFrom(maze, startRow, startColumn + 1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found

#Code_4.11 Maze类 init方法
class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startColumn = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = Turtle(shape = 'turtle')
        setup(width = 600, height = 600)
        setworldcoordinates(-(columnsInMaze - 1) / 2-.5, -(rowsInMaze - 1) / 2-.5,
                            (columnsInMaze - 1) / 2+.5, (rowsInMaze - 1) / 2+.5)

#Code_4.12 Maze类 drawMaze方法
    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMzae):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'tan')
        self.t.color('black', 'blue')

    def drawCenteredBox(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x-.5, y-.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(color)

    def updatePosition(self, row, col, val = None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

#Code_4.13 Maze类 isExit方法
    def isExit(self, row, col):
        return (row == 0 or row == self.rowsInMaze - 1 or col == 0 or col == self.columnsInMaze - 1)

    def __getitem__(self, idx):
        return self.mazelist[idx]
