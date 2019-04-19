import pygame, time, sys

class Simulation:
    #Initiates Pygame display window and class variables
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Space Inertia Simulation")
        self.rocket = Rocket()
        self.running = True
        self.marks = []
        self.paused = False

    #Clears the screen
    def clear(self):
        self.window.fill((0, 0, 0))

    #Clears the screen and resets all objects in simulation to default values
    def reset(self):
        self.clear()
        self.rocket.reset()

    #Halves all sizes and positions on screen to imitate a zoom out
    def zoomOut(self):
        self.clear()
        self.rocket.halfVars()
        for mark in self.marks:
            mark.halfVars()

    #Doubles all sizes and positions on screen to imitate a zoom in
    def zoomIn(self):
        self.clear()
        self.rocket.doubleVars()
        for mark in self.marks:
            mark.doubleVars()

    #Ends the simulation if user clicks GUI X, or types escape or q key
    def endSim(self):
        pygame.quit()
        sys.exit()

    #Scans for user keyboard input and acclerates rocket, resets simulation, zooms in or out or quits simulation
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

    #Redraws all past locations of rocket to show path
    def drawMarks(self):
        for mark in self.marks:
            pygame.draw.circle(self.window, (255, 255, 255), (int(mark.posX), int(mark.posY)), int(self.rocket.radius / 2), 1)

    #Loops to gather user input and update simulation
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
    #Initiates a mark object to track the track of the rocket
    def __init__(self, X, Y):
        self.posX = X
        self.posY = Y

    #Halves variables for zooming out simualtion
    def halfVars(self):
        self.posX, self.posY = (self.posX - 350) / 2 + 350, (self.posY - 350) / 2 + 350

    #Doubles variables for zooming in simulation
    def doubleVars(self):
        self.posX, self.posY = (self.posX - 350) * 2 + 350, (self.posY - 350) * 2 + 350

class Rocket:
    #Initiates rocket object representing object in space
    def __init__(self):
        self.posX, self.posY = 350, 350
        self.velX, self.velY = 0, 0
        self.accX, self.accY = 0, 0
        self.radius = 10

    #Updates velocity and position variables of rocket
    def update(self):
        self.velX += self.accX
        self.velY += self.accY
        self.posX += self.velX
        self.posY += self.velY

    #Halves variables for zooming out simulation
    def halfVars(self):
        self.posX, self.posY = (self.posX - 350) / 2 + 350, (self.posY - 350) / 2 + 350
        self.velX /= 2
        self.velY /= 2
        self.accX /= 2
        self.accY /= 2
        self.radius /= 2

    #Doubles variables for zooming in simulation
    def doubleVars(self):
        self.posX, self.posY = (self.posX - 350) * 2 + 350, (self.posY - 350) * 2 + 350
        self.velX *= 2
        self.velY *= 2
        self.accX *= 2
        self.accY *= 2
        self.radius *= 2

    #Accelerates rocket upward when up key is pressed
    def accelUp(self):
        self.accY -= 0.25

    #Accelerates rocket downward when down key is pressed
    def accelDown(self):
        self.accY += 0.25

    #Accelerates rocket right when right key is pressed
    def accelRight(self):
        self.accX += 0.25

    #Accelerates rocket left when left key is pressed
    def accelLeft(self):
        self.accX -= 0.25

    #Resets class variables to initial values
    def reset(self):
        self.posX, self.posY = 350, 350
        self.velX, self.velY = 0, 0
        self.accX, self.accY = 0, 0

#Inititalizes function and goes through simulation loop
def main():
    sim = Simulation()
    while sim.running:
        sim.simLoop()

main()
