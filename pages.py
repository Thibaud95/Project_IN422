import pygame
from ui import Button, InputBox  # Import de la classe InputBox
from algorithms.fcfs import FCFS
font = pygame.font.Font(None, 48)

# Initialize global variables

table_data = [["Process", "Arrival Time", "Burst Time"]]

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
            page = button.handle_event(event)
            if page:
                return page

    return "home"

def draw_fcfs_page(screen):
    return draw_algorithm_page(screen, "FCFS")

def draw_rr_page(screen):
    return draw_algorithm_page(screen, "Round Robin")

def draw_rm_page(screen):
    return draw_algorithm_page(screen, "Rate Monotonic")

def draw_edf_page(screen):
    return draw_algorithm_page(screen, "Earliest Deadline First")

def draw_sjn_page(screen):
    return draw_algorithm_page(screen, "Shortest Job Next")


def draw_algorithm_page(screen, algo_name):
    global table_data  # Utiliser les variables globales

    # Bouton "Retour"
    back_button = Button(50, 50, 150, 50, "Retour", "home")
    add_button = Button(screen.get_width() - 250, 100, 200, 50, "Add Processes", "add_processes")
    validate_button = Button(screen.get_width() - 250, 200, 200, 50, "Validate", "validate")
    validate_button.visibility = False

    # Titre de la page
    title = font.render(algo_name, True, (255, 255, 255))

    # Création de l'InputBox pour le nombre de processus
    input_box = InputBox(screen.get_width() - 250, 50, 200, 50)

    # Liste pour stocker les InputBox de la colonne "Arrival Time"
    arrival_time_boxes = []
    burst_time_boxes = []
    # Boucle interne pour gérer les événements
    while True:
        screen.fill((30, 30, 30))  # Fond gris foncé
        screen.blit(title, (540, 50))  # Dessiner le titre

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Gestion du bouton "Retour"
            action = back_button.handle_event(event)
            if action:
                return action  # Sortir de la fonction si "Retour" est cliqué

            # Gestion du bouton "Add Processes"
            action = add_button.handle_event(event)
            if action == "add_processes":
                try:
                    num_processes = int(input_box.text)
                    # Réinitialiser le tableau et les InputBox
                    reset_table_data()

                    arrival_time_boxes = []
                    burst_time_boxes = []
                    validate_button.visibility = True
                    add_button.visibility = False
                    input_box.visibility = False 
                    for i in range(1, num_processes + 1):
                        table_data.append([f"P{i}", "", ""])
                        # Ajouter une InputBox pour chaque ligne dans la colonne "Arrival Time"
                        arrival_time_boxes.append(InputBox(250, 150 + i * 50, 200, 50))
                        burst_time_boxes.append(InputBox(450, 150 + i * 50, 200, 50))
                except ValueError:
                    print("Please enter a valid integer.")
            
            
            # Gestion de l'InputBox pour le nombre de processus
            input_box.handle_event(event)

            # Gestion des InputBox de la colonne "Arrival Time"
            arrival_time = []
            for box in arrival_time_boxes:
                box.handle_event(event)
                arrival_time.append(box.text)
            
            # Gestion des InputBox de la colonne "Burst Time"
            burst_time = []
            for box in burst_time_boxes:
                box.handle_event(event)
                burst_time.append(box.text)

            # Gestion du bouton "Validate"
            action = validate_button.handle_event(event)
            if action == "validate":
                process_list = []
                for i in range(len(arrival_time)):
                    process_list.append(("P"+str(i+1),int(arrival_time[i]), int(burst_time[i])))
                result = FCFS(process_list)
                print(result)  

        # Dessiner les boutons
        back_button.draw(screen)
        add_button.draw(screen)
        validate_button.draw(screen)

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
                if col_index == 1 and row_index > 0:  # Colonne "Arrival Time" (ignorer l'en-tête)
                    arrival_time_boxes[row_index - 1].draw(screen)
                if col_index == 2 and row_index > 0:  # Colonne "Burst Time"    
                    burst_time_boxes[row_index - 1].draw(screen)
                else:
                    text_surface = font.render(cell, True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    screen.blit(text_surface, text_rect)

        # Dessiner l'InputBox pour le nombre de processus
        input_box.draw(screen)

        # Mettre à jour l'affichage
        pygame.display.flip()
        pygame.time.Clock().tick(60)

def reset_table_data():
    """Réinitialise les données du tableau et les InputBox."""
    global table_data
    table_data = [["Process", "Arrival Time", "Burst Time"]]
