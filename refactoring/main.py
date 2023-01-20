# this file is the main file needed to run the simulation.



# importing packages and initialisng 
#from turtle import color
from pygame.locals import *
import pygame
import math
from colours import *
import planet_class
from planet_class import Planet

#from orbital_velocity import orbital_velocity
pygame.init()

pygame.display.set_caption("Travel to Pluto") #name of pygame window

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

