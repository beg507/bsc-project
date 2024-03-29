# importing packages and initialisng 
#from turtle import color
from pygame.locals import *
import pygame
import math
#from orbital_velocity import orbital_velocity
pygame.init()

pygame.display.set_caption("Travel to Pluto") #name of pygame window

scale_au = 5.5
CONSTANT = scale_au*250 #controls the zooming (rescaling) of the simulation in the window


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

        self.sun = False # the planets are not suns
        self.distance_to_sun = 0
        self.orbit = [] # array of orbit paths

    def draw(self, win, width, height, pygame_window):
        # centering
        x = self.x * self.scale + width / 2
        y = self.y * self.scale + height / 2

        # resize scaling
        resize_scale = height/CONSTANT

        updated_points = []

        # drawing the orbit lines if there are more than two position points
        if len(self.orbit) > 2:
            
            for point in self.orbit:
                x, y = point
                x = x * self.scale * resize_scale + width / 2
                y = y * self.scale * resize_scale + height / 2

                # scale the orbit of the planets to the size of the screen

                updated_points.append((x,y))

            #pygame.draw.lines(pygame_window, self.color, False, updated_points, 2) # drawing the orbit lines
            pygame.draw.lines(pygame_window, self.color, False, updated_points[-40:], 2) # drawing the orbit lines

        pygame.draw.circle(win, self.color, (x,y), self.radius*resize_scale) # drawing the planets

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
sun_colour = (255,255,0)
earth_colour = (100, 149, 237) #blue
mars_colour = (188, 39, 50) # red
mercury_colour = (80, 78, 81) #grey
venus_colour = (255, 198, 153) #beige
jupter_colour = (92, 64, 51) #dark brown
saturn_colour = (219, 190, 163) # light brown
uranus_colour = (107, 217, 221) #light blue
neptune_colour = (38, 13, 203) # dark blue
pluto_colour = (250, 236, 183) #cream

white = (255, 255, 255)
black = (0,0,0)

# setting font
font = pygame.font.SysFont("Arial", 12)

# creating pygame event loop to keep the visualtion window open while the simulation is running

def window_loop():
    width, height = 600, 600
    pygame_window = pygame.display.set_mode((width, height), RESIZABLE)
    running = True
    clock = pygame.time.Clock()

    # sun and planets initialisation (x, y, radius, color, mass)
    # RADIUS IS NOT PLANET RADIUS, IT IS FOR VISUALIZATION
    sun = Planet(width/2,height/2, 30, sun_colour, 1.98892*10**30)
    sun.sun = True

    mercury = Planet(0.4* Planet.AU, 0, 8, mercury_colour, 3.30 * 10**23)
    mercury.y_v = -47.4 * 1000 #km/s #negative to make planet orbit counter-clockwise
    
    venus = Planet(0.72 * Planet.AU, 0, 12, venus_colour, 4.8685 * 10**24)
    venus.y_v = -35.02 * 1000

    earth = Planet(1*Planet.AU, 0, 15, earth_colour, 5.9742*10**24)
    earth.y_v = -29.783 * 1000 

    mars = Planet(1.5 * Planet.AU, 0, 10, mars_colour, 6.39 * 10**23)
    mars.y_v = -24.077 * 1000

    jupiter = Planet(5.2 * Planet.AU, 0, 30, jupter_colour, 1898*10**24)
    jupiter.y_v = -13.1 * 1000

    saturn = Planet(9.6 * Planet.AU, 0, 25, saturn_colour, 568*10**24)
    saturn.y_v = -9.7 * 1000

    uranus = Planet(19.2 * Planet.AU, 0, 20, uranus_colour, 86.6*10**24)
    uranus.y_v = -6.8 * 1000

    neptune = Planet(30 * Planet.AU, 0, 20, neptune_colour, 102*10**24)
    neptune.y_v = -5.4 * 1000

    pluto = Planet(39.5 * Planet.AU, 0, 4, pluto_colour, 0.0130*10**24)
    pluto.y_v = -4.7 * 1000

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

    while running:
        clock.tick(60) # set frame rate to 60 FPS
        pygame_window.fill((0,0,0)) # so planets don't have a planet size trail
        # until the user closes the window, continue running the visualisation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == WINDOWRESIZED:
                width, height = pygame_window.get_width(), pygame_window.get_height()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                 run = False


        for planet in planets:
            planet.update_position(planets)
            planet.draw(pygame_window, width, height, pygame_window)
        pygame.display.update() # continuously update the display

    pygame.quit()

# call the function
window_loop()

