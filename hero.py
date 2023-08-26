class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.pos = pos
        self.hero = loader.loadModel("smiley")
        self.hero.setScale(0.5)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.CameraBind()
        self.accept_events()

    def CameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.CameraOn = True

    def CameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1] + 5, -pos[2]-2)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.CameraOn = False
    def ChangeViev(self):
        if self.CameraOn:
            self.CameraUp()
        else:
            self.CameraBind()

    def look_at(self, angle):
        x_from = self.hero.getX()
        y_from = self.hero.getY()
        z_from = self.hero.getZ()

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from
    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def turn_left(self):
        angle = self.hero.getH()
        self.hero.setH((angle + 5) % 360)
    def turn_right(self):
        angle = self.hero.getH()
        self.hero.setH((angle - 5) % 360)
    def forward(self):
        angle = self.hero.getH()
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def backward(self):
        angle = (self.hero.getH() + 180) %360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def right(self):
        angle = (self.hero.getH() + 270) %360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def left(self):
        angle = (self.hero.getH() + 90) %360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def build(self):
        angle = self.hero.getH()
        pos = self.look_at(angle)
        self.land.addBlock(pos)
    def up(self):
        z_cor = self.hero.getZ()
        self.hero.setZ(z_cor + 1) 
    def down(self):
        z_cor = self.hero.getZ()
        self.hero.setZ(z_cor - 1)
    def destroy(self):
        angle = self.hero.getH()
        pos = self.look_at(angle)
        self.land.delBlock(pos)
    def wood(self):
        self.land.texture = "textures/1.png"
    def sand(self):
        self.land.texture = "textures/2.png"
    def cobblestone(self):
        self.land.texture = "textures/3.png"
    def accept_events(self):
        base.accept("tab", self.ChangeViev) 
        base.accept("arrow_left", self.turn_left) 
        base.accept("arrow_left" + "-repeat", self.turn_left)
        base.accept("arrow_right", self.turn_left)
        base.accept("arrow_right" + "-repeat", self.turn_right)
        base.accept("w", self.forward)
        base.accept("w" + "-repeat", self.forward)
        base.accept("s", self.backward)
        base.accept("s" + "-repeat", self.backward)
        base.accept("d", self.right)
        base.accept("d" + "-repeat", self.right)
        base.accept("a", self.left)
        base.accept("a" + "-repeat", self.left)
        base.accept("mouse1", self.build)
        base.accept("space", self.up)
        base.accept("space" + "-repeat", self.up)
        base.accept("lcontrol", self.down)
        base.accept("lcontrol" + "-repeat", self.down)
        base.accept("mouse3", self.destroy)
        base.accept("1", self.wood)
        base.accept("2", self.sand)
        base.accept("3", self.cobblestone)