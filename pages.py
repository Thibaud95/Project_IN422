import pygame


from ui import Button, InputBox, Text
from algorithms.fcfs import FCFS

font = pygame.font.Font(None, 34)

def draw_homepage(screen):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (1920 - button_width) // 2  # Centré horizontalement

    buttons = [
        Button(button_center_on_x, 193, button_width, button_height, "First Come First Serve", "fcfs"),
        Button(button_center_on_x, 354, button_width, button_height, "Shortest Job Next", "sjn"),
        Button(button_center_on_x, 515, button_width, button_height, "Round Robin", "rr"),
        Button(button_center_on_x, 676, button_width, button_height, "Rate Monotonic", "rm"),
        Button(button_center_on_x, 837, button_width, button_height, "Earliest Deadline First", "edf"),
    ]
    
    title = font.render("Ordonnancement CPU", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(1920 // 2, 100)))
    
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
    table_data = [["Process", "Arrival Time", "Burst Time"]]
    result_text_box = Text(screen.get_width()/2-450, screen.get_height()/2+300, 400, 50, "Résultat")
    result_text_box.visibility = False
    result_text_box2 = Text(screen.get_width()/2+50, screen.get_height()/2+300, 400, 50, "Résultat")
    result_text_box2.visibility = False

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

                    # if algo_name == "FCFS":
                    #     num_processes = int(user_text)
                    #     # Ajouter les nouvelles lignes au tableau
                    #     table_data = [["Process", "Arrival Time", "Burst Time"]]  # Réinitialiser le tableau
                    #     for i in range(1, num_processes + 1):
                    #         table_data.append([f"P{i}", "", ""])

                    # elif algo_name == "Shortest Job Next":
                    #     num_processes = int(user_text)
                    #     # Ajouter les nouvelles lignes au tableau
                    #     table_data = [["Process", "Arrival Time", "Burst Time"]]
                    #     for i in range(1, num_processes + 1):
                    #         table_data.append([f"P{i}", "", ""])

                    # elif algo_name == "Round Robin":
                    #     num_processes = int(user_text)
                    #     # Ajouter les nouvelles lignes au tableau
                    #     table_data = [["Process", "Arrival Time", "Burst Time", "Quantum Time"]]
                    #     for i in range(1, num_processes + 1):
                    #         table_data.append([f"P{i}", "", ""])

                    # elif algo_name == "Rate Monotonic":
                    #     num_processes = int(user_text)
                    #     # Ajouter les nouvelles lignes au tableau
                    #     table_data = [["Process", "Arrival Time", "Burst Time", "Period"]]
                    #     for i in range(1, num_processes + 1):
                    #         table_data.append([f"P{i}", "", ""])

                    # elif algo_name == "Earliest Deadline First":
                    #     num_processes = int(user_text)
                    #     # Ajouter les nouvelles lignes au tableau
                    #     table_data = [["Process", "Arrival Time", "Burst Time", "Deadline", "Period"]]
                    #     for i in range(1, num_processes + 1):
                    #         table_data.append([f"P{i}", "", ""])

                    num_processes = int(input_box.text)
                    # Réinitialiser le tableau et les InputBox
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
                for i in range(num_processes):
                    if arrival_time[i] != "" and burst_time[i] != "":
                        process_list = []
                        for i in range(len(arrival_time)):
                            process_list.append(("P"+str(i+1),int(arrival_time[i]), int(burst_time[i])))
                        result = FCFS(process_list)
                        print(result) 
                        validate_button.visibility = False
                        table_data = [["Process", "Arrival Time", "Burst Time","Completion Time", "Turnaround Time", "Waiting Time"]]
                        for i in range(1, num_processes + 1):
                            table_data.append([f"P{i}", "", "", str(result["Completion Time"][f"P{i}"]), str(result["Turnaround Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                            result_text_box.text= "Average Turnaround Time : " + str(result["Average Turnaround Time"])
                            result_text_box2.text= "Average Waiting Time : " + str(result["Average Waiting Time"])
                            result_text_box.visibility = True
                            result_text_box2.visibility = True
                    else : print("Enter the parameters before validate")


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
        result_text_box.draw(screen)
        result_text_box2.draw(screen)
        # Mettre à jour l'affichage
        pygame.display.flip()
        pygame.time.Clock().tick(60)


