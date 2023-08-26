from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        x, y = self.land.loadLand("land3.txt")
        #self.model = loader.loadModel("models/environment")
        #self.model.reparentTo(render)
        #self.model.setScale(0.1)
        #self.model.setPos(-2, 25, -3)
        x, y = self.land.loadLinearMap('new_land.txt')
        self.hero = Hero((x // 2, y // 2, 4), self.land)
        base.camLens.setFov(90)
    
game = Game()
game.run()