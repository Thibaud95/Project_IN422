import pygame

# pygame setup  thibaud
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Button setup
button_color = (0, 255, 0)  # Green
button_hover_color = (0, 200, 0)  # Darker green
button_rect = pygame.Rect(screen.get_width() - 250, 50, 200, 50)  # x, y, width, height
button_text = "Add Processes"

font = pygame.font.Font(None, 36)  # Default font, size 36

# Table setup
table_font = pygame.font.Font(None, 28)
table_data = [
    ["Process", "Arrival Time", "Burst Time"]
]
dynamic_value = "42"  # Placeholder for the dynamic value

# Input box setup
input_box = pygame.Rect(screen.get_width() - 250, 200, 200, 50)  # x, y, width, height
input_color_active = (255, 255, 255)  # White
input_color_inactive = (200, 200, 200)  # Gray
input_color = input_color_inactive
input_active = False
user_text = ""  # Text entered by the user

def add_processes():
    global table_data
    try:
        num_processes = int(user_text)  # Convert the input to an integer
        # Réinitialiser le tableau avec uniquement les en-têtes
        table_data = [["Process", "Arrival Time", "Burst Time"]]
        # Ajouter les nouvelles lignes pour les processus
        for i in range(1, num_processes + 1):
            table_data.append([f"P{i}", "", ""])  # Ajouter une ligne pour chaque processus
        print(f"Table updated with {num_processes} processes.")
    except ValueError:
        print("Please enter a valid integer.")

def button_action():
    # Action triggered when the button is clicked
    add_processes()

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the input box is clicked
            if input_box.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False
            # Change the color of the input box based on activity
            input_color = input_color_active if input_active else input_color_inactive

            # Check if the button is clicked
            if button_rect.collidepoint(event.pos):
                button_action()
        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    print(f"User entered: {user_text}")
                    input_active = False
                    input_color = input_color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # Remove the last character
                else:
                    # Only allow numeric input
                    if event.unicode.isdigit():
                        user_text += event.unicode

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    # Draw the button
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, button_hover_color, button_rect)
    else:
        pygame.draw.rect(screen, button_color, button_rect)

    # Render button text
    text_surface = font.render(button_text, True, (0, 0, 0))  # Black text
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Draw the table
    cell_width = 200
    cell_height = 50
    table_x = 50  # Starting x position for the table
    table_y = 150  # Starting y position for the table

    for row_index, row in enumerate(table_data):
        for col_index, cell in enumerate(row):
            cell_rect = pygame.Rect(
                table_x + col_index * cell_width,
                table_y + row_index * cell_height,
                cell_width,
                cell_height
            )
            pygame.draw.rect(screen, (255, 255, 255), cell_rect)  # White cell background
            pygame.draw.rect(screen, (0, 0, 0), cell_rect, 2)  # Black border
            text_surface = table_font.render(cell, True, (0, 0, 0))  # Black text
            text_rect = text_surface.get_rect(center=cell_rect.center)
            screen.blit(text_surface, text_rect)

    # Draw the input box
    pygame.draw.rect(screen, input_color, input_box)
    input_text_surface = font.render(user_text, True, (0, 0, 0))  # Black text
    input_text_rect = input_text_surface.get_rect(center=input_box.center)
    screen.blit(input_text_surface, input_text_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()