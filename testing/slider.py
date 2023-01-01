import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (600, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Slider')

# Set the default value of the variable
value = 0

# Set the dimensions of the slider
slider_width = 200
slider_height = 1
slider_x = (window_size[0] - slider_width) // 2
slider_y = (window_size[1] - slider_height) // 2

# Set the dimensions of the slider handle
handle_radius = 10

# Set the limits of the handle's movement
min_handle_x = slider_x - handle_radius
max_handle_x = slider_x + slider_width - handle_radius

# Set the initial position of the handle
handle_x = min_handle_x

# Set the font and font size for the value display
font = pygame.font.Font(None, 36)

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (125, 125, 125)

# Set the title text
title_text = "Slider Title"

# Create the title text surface
title_surface = font.render(title_text, True, black)

# Get the rectangle for the title surface
title_rect = title_surface.get_rect()



# Set the initial state of the handle
dragging = False

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the handle
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (handle_x - handle_radius <= mouse_x <= handle_x + handle_radius and
                    slider_y - handle_radius <= mouse_y <= slider_y + handle_radius):
                # Start dragging the handle
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Stop dragging the handle
            dragging = False

    # Update the value and handle position based on mouse movement
    if dragging:
        mouse_x, _ = pygame.mouse.get_pos()
        handle_x = max(min_handle_x, min(mouse_x, max_handle_x))
        value = int((handle_x - min_handle_x) / (max_handle_x - min_handle_x) * 100)

    # Draw the slider
    screen.fill(white)
    pygame.draw.rect(screen, gray, (slider_x, slider_y, slider_width, slider_height))
    pygame.draw.circle(screen, black, (handle_x, slider_y), handle_radius)

    # Draw the value display
    value_text = font.render(str(value), True, black)
    value_rect = value_text.get_rect()
    value_rect.center = (slider_x + slider_width + handle_radius * 2, slider_y - handle_radius)
    screen.blit(value_text, (value_rect.centerx, value_rect.centery))

    # draw the title
    # Center the title rectangle horizontally above the slider
    title_rect.centerx = slider_x + slider_width // 2
    title_rect.bottom = slider_y - handle_radius
    # Blit the title surface onto the screen
    screen.blit(title_surface, title_rect)

    pygame.display.update()