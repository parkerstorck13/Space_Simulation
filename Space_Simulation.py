import pygame, time, sys

class Simulation:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Space Inertia Simulation")
        self.rocket = Rocket()
        self.running = True
        self.marks = []
        self.paused = False

    def clear(self):
        self.window.fill((0, 0, 0))

    def reset(self):
        self.clear()
        self.rocket.reset()

    def zoomOut(self):
        self.clear()
        self.rocket.halfVars()
        for mark in self.marks:
            mark.halfVars()

    def zoomIn(self):
        self.clear()
        self.rocket.doubleVars()
        for mark in self.marks:
            mark.doubleVars()

    def endSim(self):
        pygame.quit()
        sys.exit()

    def getInput(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endSim()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        self.endSim()
                    if event.key == pygame.K_UP:
                            self.rocket.accelUp()
                    if event.key == pygame.K_DOWN:
                            self.rocket.accelDown()
                    if event.key == pygame.K_RIGHT:
                            self.rocket.accelRight()
                    if event.key == pygame.K_LEFT:
                            self.rocket.accelLeft()
                    if event.key == pygame.K_r:
                        self.reset()
                        self.marks = []
                    if event.key == pygame.K_o:
                        self.zoomOut()
                    if event.key == pygame.K_i:
                        self.zoomIn()

    def drawMarks(self):
        for mark in self.marks:
            pygame.draw.circle(self.window, (255, 255, 255), (int(mark.posX), int(mark.posY)), int(self.rocket.radius / 2), 1)

    def simLoop(self):
            self.getInput()
            self.rocket.update()
            self.clear()
            self.drawMarks()
            pygame.draw.circle(self.window, (255, 255, 255), (int(self.rocket.posX),int(self.rocket.posY)), int(self.rocket.radius))
            self.marks.append(Mark(self.rocket.posX, self.rocket.posY))
            pygame.display.flip()
            time.sleep(.1)

class Axis:
    pass

class Mark:
    def __init__(self, X, Y):
        self.posX = X
        self.posY = Y

    def halfVars(self):
        self.posX, self.posY = (self.posX - 350) / 2 + 350, (self.posY - 350) / 2 + 350

    def doubleVars(self):
        self.posX, self.posY = (self.posX - 350) * 2 + 350, (self.posY - 350) * 2 + 350

class Rocket:
    def __init__(self):
        self.posX, self.posY = 350, 350
        self.velX, self.velY = 0, 0
        self.accX, self.accY = 0, 0
        self.radius = 10

    def update(self):
        self.velX += self.accX
        self.velY += self.accY
        self.posX += self.velX
        self.posY += self.velY

    def halfVars(self):
        self.posX, self.posY = (self.posX - 350) / 2 + 350, (self.posY - 350) / 2 + 350
        self.velX /= 2
        self.velY /= 2
        self.accX /= 2
        self.accY /= 2
        self.radius /= 2

    def doubleVars(self):
        self.posX, self.posY = (self.posX - 350) * 2 + 350, (self.posY - 350) * 2 + 350
        self.velX *= 2
        self.velY *= 2
        self.accX *= 2
        self.accY *= 2
        self.radius *= 2

    def accelUp(self):
        self.accY -= 0.25

    def accelDown(self):
        self.accY += 0.25

    def accelRight(self):
        self.accX += 0.25

    def accelLeft(self):
        self.accX -= 0.25

    def reset(self):
        self.posX, self.posY = 350, 350
        self.velX, self.velY = 0, 0
        self.accX, self.accY = 0, 0


def main():
    sim = Simulation()
    while sim.running:
        sim.simLoop()

main()
