#waterflow problem

#input starting position [x,y]
#input 2-d array with each value representing a height.

class Point(object):
	def __init__(self,x, y):
		self.x = x
		self.y = y

class Path(object):
	def __init__(self):
		self.path = []

	def setPath(self, path):
		self.path = path

	def travelTo(self,point):
		self.path += [point]

	def printPath(self):
		count = 0
		while count < len(self.path):
			print(str(self.path[count].x)+", "+str(self.path[count].y))
			count+=1

	def getLastPoint(self):
		return self.path[len(self.path)-1]


class Terrain(object):

	def __init__(self,fullTerrain):
		self.fullTerrain = fullTerrain
		self.allPossiblePaths = []
		self.cache = {}

	def validPointOnTerrain(self, point):
		if point.x < 0 and point.y < 0:
			#print ("invalid starting point: x="+str(point.x) + " y=" + str(point.y))
			return False

		if point.x < 0:
			#print ("invalid starting point: x="+str(point.x))
			return False

		if point.y < 0:
			#print ("invalid starting point: x="+str(point.y))
			return False

		if len(self.fullTerrain) <= point.x:
			#print ("invalid starting point: x="+str(point.x))
			return False

		if len(self.fullTerrain[0]) <= point.y:
			#print ("invalid starting point: y="+str(point.y))
			return False

		return True;

	def printAllPaths(self):
		for i in range(0, len(self.allPossiblePaths)):
			print("==Path " + str(i+1)+"==")
			self.allPossiblePaths[i].printPath()

	def pathFrom(self,point):
		#validate point
		if not self.validPointOnTerrain(point):
			print("can't find path")

		#if path is null, create one
		if len(self.allPossiblePaths) == 0:
			path = Path()
			path.path = [point]
			self.allPossiblePaths = [path]

		stillNeedToExplore = True
		while (stillNeedToExplore):
			stillNeedToExplore = self.findPaths()


	def findPaths(self):
		foundMorePaths = False

		for i in range(0, len(self.allPossiblePaths)):
			point = self.allPossiblePaths[i].getLastPoint()
			
			#get all possible next steps, and create copies of original path if more than one
			nextSteps = self.findNextSteps(point)

			#no steps found
			if len(nextSteps) == 0:
				continue

			#one or more paths found
			currentPath = list(self.allPossiblePaths[i].path)
			foundMorePaths = True

			for j in range(0, len(nextSteps)):
				if j == 0:
					self.allPossiblePaths[i].travelTo(nextSteps[j])
					continue

				tempPath = Path()
				tempPath.setPath(list(currentPath))
				tempPath.travelTo(nextSteps[j])
				self.allPossiblePaths += [tempPath]

		return foundMorePaths


	def findNextSteps(self, point):
		if not self.validPointOnTerrain(point):
			print("invalid point")
			return []

		x = point.x
		y = point.y
		xy = str(x)+"-"+str(y)

		# check cache to see if it's already there
		if (xy in self.cache):
			return self.cache[xy]

		possiblePaths = []

		for i in range(x-1,x+2):
			for j in range(y-1,y+2):
				if not self.validPointOnTerrain(Point(i,j)):
					continue
				if i == x and j == y:
					continue
				if self.fullTerrain[i][j] >= self.fullTerrain[x][y]:
					continue

				possiblePaths += [Point(i,j)]

		# add to cache
		self.cache[xy] = possiblePaths
		return possiblePaths




#===================
#terrain = Terrain([[1,1],[1,2]])
terrain = Terrain([[1,1,1],[1,1,2],[1,2,3]])

point = Point(2,2)

terrain.pathFrom(point)

terrain.printAllPaths()