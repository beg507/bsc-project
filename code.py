# importing packages and initialisng 
from turtle import color
import pygame
import math
pygame.init()

# setting up pygame visualistation window (width and height of window, as well as window title)
width, height = 900, 900
pygame_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Travel to Pluto")

# creating a planet class
class Planet:
    AU = 149.6e6*1000 # astronomical unit in metres
    G = 6.67428e-11 # gravitational constant
    scale = 250 / AU # 1AU = 100px
    timestep = 3600*24 # seconds in a day (this is how much movement is updated every 60 FPS)

    # initialisation of class asstributes
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        # initial velocity
        self.x_v = 0
        self.y_v = 0

        self.sun = False # the sun isn't a planet
        self.distance_to_sun = 0
        self.orbit = [] # array of orbit paths

    def draw(self, win):
        # centering
        x = self.x * self.scale + width / 2
        y = self.y * self.scale + height / 2

        updated_points = []

        # drawing the orbit lines if there are more than two position points
        if len(self.orbit) > 2:
            
            for point in self.orbit:
                x, y = point
                x = x * self.scale + width / 2
                y = y * self.scale + width / 2
                updated_points.append((x,y))

            pygame.draw.lines(win, self.color, False, updated_points, 2) # drawing the orbit lines
        
        pygame.draw.circle(win, self.color, (x,y), self.radius) # drawing the planets

        # displaying the distance to the sun on the planets as they move
        if not self.sun:
            distance_text = font.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, white)
            # setting the text position to be in the centre of the planets
            win.blit(distance_text,(x-distance_text.get_width()/2, y+distance_text.get_height()))
   
    def grav_attraction(self, other_body):
        other_body_x, other_body_y = other_body.x, other_body.y
        # x and y distances between two bodies
        distance_x = other_body_x - self.x
        distance_y = other_body_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2) # distance between bodies
        
        if other_body.sun:
            self.distance_to_sun = distance

        # calculation of graviational force, force components, and theta    
        F = self.G * self.mass * other_body.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        F_x = math.cos(theta) * F
        F_y = math.sin(theta) * F
        return F_x, F_y

    # updating planet positions considering the graviational force
    def update_position(self, planets):
        F_x_net = F_y_net = 0 # inital force on planet is zero
        # calculating the total force on the planet from all the other planets (and sun)
        for planet in planets:
            if self == planet: # don't calculate the force with the planet and itself
                continue

            fx, fy = self.grav_attraction(planet) # taking F_x and F_y from grav_attraction
            # summing the forces
            F_x_net += fx
            F_y_net += fy

        # F=ma velocity calculation
        self.x_v += F_x_net / self.mass * self.timestep
        self.y_v += F_y_net / self.mass * self.timestep

        # position calculation
        self.x += self.x_v * self.timestep
        self.y += self.y_v * self.timestep
        
        # appending x and y positions of orbits
        self.orbit.append((self.x, self.y))

# defining colours
yellow = (255,255,0)
blue = (100, 149, 237)
red = (188, 39, 50)
grey = (80, 78, 81)
white = (255, 255, 255)

# setting font
font = pygame.font.SysFont("Arial", 12)

# creating pygame event loop to keep the visualtion window open while the simulation is running

def window_loop():
    running = True
    clock = pygame.time.Clock()

    # sun and planets initialisation (x, y, radius, color, mass)
    sun = Planet(0,0, 30, yellow, 1.98892*10**30)
    sun.sun = True

    earth = Planet(1*Planet.AU, 0, 16, blue, 5.9742*10**24)
    earth.y_v = 29.783 * 1000 
    
    mars = Planet(1.524 * Planet.AU, 0, 12, red, 6.39 * 10**23)
    mars.y_v = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, grey, 3.30 * 10**23)
    mercury.y_v = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, white, 4.8685 * 10**24)
    venus.y_v = -35.02 * 1000
    
    planets = [sun, earth, mars, mercury, venus]

    while running:
        clock.tick(60) # set frame rate to 60 FPS
        pygame_window.fill((0,0,0)) # so planets don't have a planet size trail
        # until the user closes the window, continue running the visualisation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(pygame_window)
        
        pygame.display.update() # continuously update the display

    pygame.quit()

# call the function
window_loop()

