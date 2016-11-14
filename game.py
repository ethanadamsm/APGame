running = True
boards = ""
gameBall = ""

class board(object):
	def __init__(self, boardList):
		self.boardList = boardList
		print(boardList[0])
	def getLine(self, pos):
		print()
	def getCharWithPos(self, x, y):
		index = 0
		for z in range(0, 16):
			for g in range(0, 20):
				if(z == x and g == y):
					print(self.boardList[index])
					return self.boardList[index].getText()
				index += 1
	def setCharWithPos(self, x, y, text):
		index = 2
		for z in range(0, 16):
			for g in range(0, 20):
				if(z == x and g == y):
					self.boardList[index] = text
				index += 1
	def getChar(self, index):
		return self.boardList[index].getText()
	def getList(self):
		return self.boardList

class ball(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.VelX = 1
		self.VelY = -1
	def getVelX(self):
		return self.VelX
	def getVelY(self):
		return self.VelY

class spot(object):
	def __init__(self, text):
		self.text = text
	def getText(self):
		return self.text

def createBoard():
	print("Creating board")
	global boards
	boardss = []
	for y in range(0, 16):
		for x in range(0, 20):
			if((y == 6 or y == 7 or y == 8 or y == 9) and (x == 0 or x == 19)):
				boardss.append(spot(" | "))
			elif(y == 7 and x == 9):
				boardss.append(spot(" X "))
			else:
				boardss.append(spot(" _ "))
	boards = board(boardss)
	
def drawBoard():
	print("Drawing board")
	global boards
	line = ""
	lines = []
	index = 0
	for y in range(0, 16):
		for x in range(0, 20):
			line += boards.getChar(index)
			index += 1
			if(x == 19):
				print line
				line = ""

def updateBoard():
	print("Updating board")
	global boards
	global gameBall
	index = 0
	for y in range(0, 16):
		for x in range(0, 20):
			if(boards.getCharWithPos(x, y) == " X "):
				print(gameBall.getVelX())
				print(gameBall.getVelY())
				if(gameBall.getVelX() == 1 and gameBall.getVelY() == -1):
					boards.setCharWithPos(x + 1, y + 1, " X ")
					boards.setCharWithPos(x, y, " _ ")
			index += 1 
				

def start():
	print("Starting game")
	global gameBall
	gameBall = ball(7, 9)
	createBoard()

start()

while(running):
	drawBoard()
	updateBoard()
	key = raw_input("type key")
	