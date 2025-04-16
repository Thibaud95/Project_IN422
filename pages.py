import pygame
from ui import Button

font = pygame.font.Font(None, 48)

def draw_homepage(screen):
    buttons = [
        Button(540, 200, 200, 50, "FCFS", "fcfs"),
        Button(540, 270, 200, 50, "Round Robin", "rr"),
        Button(540, 340, 200, 50, "Rate Monotonic", "rm"),
        Button(540, 410, 200, 50, "EDF", "edf"),
        Button(540, 480, 200, 50, "SJN", "sjn"),
    ]
    
    title = font.render("Ordonnancement CPU", True, (255, 255, 255))
    screen.blit(title, (480, 100))
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons:
            action = button.handle_event(event)
            if action:
                return action

    return "home"

def draw_fcfs_page(screen):
    return draw_fcfs_algorithm_page(screen, "FCFS")

def draw_rr_page(screen):
    return draw_algorithm_page(screen, "Round Robin")

def draw_rm_page(screen):
    return draw_algorithm_page(screen, "Rate Monotonic")

def draw_edf_page(screen):
    return draw_algorithm_page(screen, "Earliest Deadline First")

def draw_sjn_page(screen):
    return draw_algorithm_page(screen, "Shortest Job Next")

def draw_algorithm_page(screen, algo_name):
    back_button = Button(50, 50, 150, 50, "Retour", "home")
    
    title = font.render(algo_name, True, (255, 255, 255))
    screen.blit(title, (540, 100))
    
    back_button.draw(screen)

    for event in pygame.event.get():
        action = back_button.handle_event(event)
        if action:
            return action

    return algo_name.lower()

# Variables globales pour conserver l'état de la boîte de saisie
input_active = False
user_text = ""

def draw_fcfs_algorithm_page(screen, algo_name):
    global input_active, user_text  # Utiliser les variables globales

    # Bouton "Retour"
    back_button = Button(50, 50, 150, 50, "Retour", "home")
    add_button = Button(screen.get_width() - 250, 50, 200, 50, "Add Processes", "add_processes")

    # Titre de la page
    title = font.render(algo_name, True, (255, 255, 255))
    screen.blit(title, (540, 50))

    # Boite de texte
    input_box = pygame.Rect(screen.get_width() - 250, 200, 200, 50)
    input_color_active = (255, 255, 255)  # Blanc
    input_color_inactive = (200, 200, 200)  # Gris
    input_color = input_color_active if input_active else input_color_inactive

    table_font = pygame.font.Font(None, 28)
    table_data = [["Process", "Arrival Time", "Burst Time"]]

    # Gestion des événements
    for event in pygame.event.get():
        action = back_button.handle_event(event)
        if action:
            return action

        action = add_button.handle_event(event)
        if action == "add_processes":
            try:
                num_processes = int(user_text)
                table_data = [["Process", "Arrival Time", "Burst Time"]]
                for i in range(1, num_processes + 1):
                    table_data.append([f"P{i}", "", ""])
            except ValueError:
                print("Please enter a valid integer.")

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifie si la boîte de saisie est cliquée
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False

        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    print(f"User entered: {user_text}")
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    # Ajoute uniquement les caractères numériques
                    if event.unicode.isdigit():
                        user_text += event.unicode

    # Dessiner les boutons
    back_button.draw(screen)
    add_button.draw(screen)

    # Dessiner la table
    cell_width = 200
    cell_height = 50
    table_x = 50
    table_y = 150

    for row_index, row in enumerate(table_data):
        for col_index, cell in enumerate(row):
            cell_rect = pygame.Rect(
                table_x + col_index * cell_width,
                table_y + row_index * cell_height,
                cell_width,
                cell_height
            )
            pygame.draw.rect(screen, (255, 255, 255), cell_rect)
            pygame.draw.rect(screen, (0, 0, 0), cell_rect, 2)
            text_surface = table_font.render(cell, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=cell_rect.center)
            screen.blit(text_surface, text_rect)

    # Dessiner la boîte de saisie
    pygame.draw.rect(screen, input_color, input_box)
    input_text_surface = font.render(user_text, True, (0, 0, 0))
    input_text_rect = input_text_surface.get_rect(center=input_box.center)
    screen.blit(input_text_surface, input_text_rect)

    return algo_name.lower()
