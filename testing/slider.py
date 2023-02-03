import pygame

# pygame window initialisation
pygame.init()
window_size = (600, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Slider')
font = pygame.font.Font(None, 36)

# constants
# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (125, 125, 125)
value = 0

# slide initialisation
dragging = False
slider_width = 200
slider_height = 1
slider_x = (window_size[0] - slider_width) // 2
slider_y = (window_size[1] - slider_height) // 2

# slider handle size and x position (movement)
handle_radius = 10 
min_handle_x = slider_x - handle_radius
max_handle_x = slider_x + slider_width - handle_radius
handle_x = min_handle_x

# Set the title text
slider_name = "Slider"

# create the title text surface and rectangle for it
title_surface = font.render(slider_name, True, black)
title_rect = title_surface.get_rect()

# window loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # if user clicks on handle then drag the handle
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (handle_x - handle_radius <= mouse_x <= handle_x + handle_radius and
                    slider_y - handle_radius <= mouse_y <= slider_y + handle_radius):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP: # stop dragging when no click
            dragging = False

    # update the slider position when it is being dragged
    if dragging:
        mouse_x, _ = pygame.mouse.get_pos()
        handle_x = max(min_handle_x, min(mouse_x, max_handle_x))
        value = int((handle_x - min_handle_x) / (max_handle_x - min_handle_x) * 100)

    # drawing the slider
    screen.fill(white)
    pygame.draw.rect(screen, gray, (slider_x, slider_y, slider_width, slider_height))
    pygame.draw.circle(screen, black, (handle_x, slider_y), handle_radius)

    # updating the value of the slider (actual numerical value)
    value_text = font.render(str(value), True, black)
    value_rect = value_text.get_rect()
    value_rect.center = (slider_x + slider_width + handle_radius * 2, slider_y - handle_radius)
    screen.blit(value_text, (value_rect.centerx, value_rect.centery))

    # draw the title and centre it
    title_rect.centerx = slider_x + slider_width // 2
    title_rect.bottom = slider_y - handle_radius
    
    screen.blit(title_surface, title_rect)

    pygame.display.update()