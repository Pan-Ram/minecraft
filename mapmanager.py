class Mapmanager():
    def __init__(self):
        self.model = "block.egg"
        self.texture = "block.png"
        #self.color = (0.2, 0.2, 0.35, 1)
        self.startNew()
        #self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTag("at", str(position))
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
    
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def loadLand(self, filename):
        self.clear()
        with open(filename, "r") as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for z in line:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((float(x), float(y), float(z0)))
                    x += 1
                y += 1
            return x, y
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))
    def delBlock(self, pos):
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def loadLinearMap(self, filename):
	    self.clear()
	    with open(filename) as file:
		    x = 0
		    y = 0
		    for line in file:
			    line = line.split()
			    x = int(line[0])
			    y = int(line[1])
			    z = int(line[2])
			    self.texture = line[3]
			    self.addBlock((float(x), float(y), float(z)))
	    return x, y
