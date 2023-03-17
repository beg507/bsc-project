import math
import pygame
from pygame.locals import *
import colours

pygame.font.init()

SCALE = 3000 #controls the zooming (rescaling) of the simulation in the window

# setting font
font = pygame.font.SysFont("Arial", 12)

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
        resize_scale = height/SCALE

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
            distance_text = font.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, colours.white)
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
        print("force y: ", F_y)
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

            print("Force y net: ", F_y_net)

        # F=ma velocity calculation
        self.x_v += F_x_net / self.mass * self.timestep
        self.y_v += F_y_net / self.mass * self.timestep

        print("y velocity: ", self.y_v)

        # position calculation
        self.x += self.x_v * self.timestep
        self.y += self.y_v * self.timestep

        print("y position: ", self.y)
        
        # appending x and y positions of orbits
        self.orbit.append((self.x, self.y))
