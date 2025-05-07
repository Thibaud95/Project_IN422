import pygame


from ui import Button, InputBox, Text
from FCFS_algo import FCFS
from EDF_algo import EDF
from RM_algo import RM
from RR_algo import RR
from SJN_algo import SJN


font = pygame.font.Font(None, 21)


def draw_homepage(screen):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (screen.get_width() - button_width) // 2  # Centré horizontalement

    buttons = [
        Button(button_center_on_x, 100, button_width, button_height, "First Come First Serve", "fcfs"),
        Button(button_center_on_x, 200, button_width, button_height, "Shortest Job Next", "sjn"),
        Button(button_center_on_x, 300, button_width, button_height, "Round Robin", "rr"),
        Button(button_center_on_x, 400, button_width, button_height, "Rate Monotonic", "rm"),
        Button(button_center_on_x, 500, button_width, button_height, "Earliest Deadline First", "edf"),
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
    value_text = "Init"
    if algo_name == "Round Robin":
        value_text = "Set quantum"
    elif algo_name == "Earliest Deadline First":
        value_text = "Set time limit"
    elif algo_name == "Rate Monotonic":
        value_text = "Set total time"
    quantum_limit_button = Button(screen.get_width() - 250, 100, 200, 50, value_text, "set_values")
    quantum_limit_button.visibility = False


    # Titre de la page
    title = font.render(algo_name, True, (255, 255, 255))


    # Création de l'InputBox pour le nombre de processus
    input_box = InputBox(screen.get_width() - 250, 50, 200, 50)

    # Liste pour stocker les InputBox de la colonne "Arrival Time"
    arrival_time_boxes = []
    burst_time_boxes = []
    period_boxes = []
    deadline_boxes = []
    if algo_name == "FCFS" or algo_name == "Shortest Job Next":
        table_data = [["Process", "Arrival Time", "Burst Time"]]
    elif algo_name == "Round Robin":
        table_data = [["Process", "Arrival Time", "Burst Time"]]
    elif algo_name == "Rate Monotonic":
        table_data = [["Process", "Arrival Time", "Burst Time", "Period"]]
    elif algo_name == "Earliest Deadline First":
        table_data = [["Process", "Arrival Time", "Burst Time",  "Period", "Deadline"]]
  
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
                    num_processes = int(input_box.text)
                    # Réinitialiser le tableau et les InputBox
                    arrival_time_boxes = []
                    burst_time_boxes = []
                    period_boxes = []
                    deadline_boxes = []
                    validate_button.visibility = True
                    add_button.visibility = False
                    input_box.visibility = False 

                    for i in range(1, num_processes + 1):
                        if algo_name == "FCFS" or algo_name == "Shortest Job Next":
                            table_data.append([f"P{i}", "", ""])
                        elif algo_name == "Round Robin":
                            table_data.append([f"P{i}", "", ""])
                            quantum_limit_button.visibility = True
                            input_box.visibility = True
                        elif algo_name == "Rate Monotonic":
                            table_data.append([f"P{i}", "", "", ""])
                            period_boxes.append(InputBox(425, 150 + i * 50, 125, 50))
                            quantum_limit_button.visibility = True
                            input_box.visibility = True
                        elif algo_name == "Earliest Deadline First":
                            table_data.append([f"P{i}", "", "", "", ""])
                            period_boxes.append(InputBox(425, 150 + i * 50, 125, 50))
                            deadline_boxes.append(InputBox(550, 150 + i * 50, 125, 50))
                            quantum_limit_button.visibility = True
                            input_box.visibility = True
                        # Ajouter une InputBox pour chaque ligne dans la colonne "Arrival Time"
                        arrival_time_boxes.append(InputBox(175, 150 + i * 50, 125, 50))
                        burst_time_boxes.append(InputBox(300, 150 + i * 50, 125, 50))

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
            
            if algo_name == "Rate Monotonic":
                period = []
                for box in period_boxes:
                    box.handle_event(event)
                    period.append(box.text)
            elif algo_name == "Earliest Deadline First":
                period = []
                for box in period_boxes:
                    box.handle_event(event)
                    period.append(box.text)
                deadline = []
                for box in deadline_boxes:
                    box.handle_event(event)
                    deadline.append(box.text)
            
            # Gestion du bouton "Set_values"
            action = quantum_limit_button.handle_event(event)
            if action == "set_values":
                try:
                    quantum_limit_value = int(input_box.text)
                    print(f"Quantum limit set to: {quantum_limit_value}")
                except ValueError:
                    print("Error: Please enter a valid integer.")

            # Gestion du bouton "Validate"
            action = validate_button.handle_event(event)
            if action == "validate":
                for i in range(num_processes):
                    if arrival_time[i] != "" and burst_time[i] != "":
                        process_list = []
                        if algo_name == "FCFS" or algo_name=="Shortest Job Next":                         
                            for i in range(len(arrival_time)):
                                process_list.append(("P"+str(i+1),int(arrival_time[i]), int(burst_time[i])))
                            if algo_name == "FCFS":
                                result = FCFS(process_list)
                            elif algo_name == "Shortest Job Next":
                                result = SJN(process_list)
                            print(result) 
                            validate_button.visibility = False
                            table_data = [["Process", "Arrival Time", "Burst Time","Completion Time", "Turnaround Time", "Waiting Time"]]
                            for i in range(1, num_processes + 1):
                                table_data.append([f"P{i}", "", "", str(result["Completion Time"][f"P{i}"]), str(result["Turnaround Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                        elif algo_name == "Round Robin":                         
                            for i in range(len(arrival_time)):
                                process_list.append(("P"+str(i+1),int(arrival_time[i]), int(burst_time[i])))
                            result = RR(process_list,quantum_limit_value)
                            print(result) 
                            validate_button.visibility = False
                            quantum_limit_button.visibility = False
                            input_box.visibility = False
                            table_data = [["Process", "Arrival Time", "Burst Time","Completion Time", "Turnaround Time", "Waiting Time"]]
                            for i in range(1, num_processes + 1):
                                table_data.append([f"P{i}", "", "", str(result["Completion Time"][f"P{i}"]), str(result["Turnaround Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                        elif algo_name == "Rate Monotonic":
                            process_list = []
                            arrival_times = []
                            burst_times = []
                            periods = []                       
                            for i in range(len(arrival_time)):
                                process_list.append("P"+str(i+1))
                                arrival_times.append(int(arrival_time[i]))
                                burst_times.append(int(burst_time[i]))
                                periods.append(int(period[i]))
                            result = RM(process_list,arrival_times, burst_times, periods, quantum_limit_value)
                            print(result) 
                            validate_button.visibility = False
                            quantum_limit_button.visibility = False
                            input_box.visibility = False
                            table_data = [["Process", "Arrival Time", "Burst Time", "Period", "Completion Time", "Turnaround Time", "Waiting Time"]]
                            for i in range(1, num_processes + 1):
                                table_data.append([f"P{i}", "", "", "", str(result["Completion Time"][f"P{i}"]), str(result["Turnaround Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                        elif algo_name == "Earliest Deadline First":
                            process_list = []
                            arrival_times = []
                            burst_times = []
                            deadlines = [] 
                            periods = []                      
                            for i in range(len(arrival_time)):
                                process_list.append("P"+str(i+1))
                                arrival_times.append(int(arrival_time[i]))
                                burst_times.append(int(burst_time[i]))
                                deadlines.append(int(deadline[i]))
                                periods.append(int(period[i]))
                            result = EDF(process_list,arrival_times, burst_times, deadlines, periods, quantum_limit_value)
                            print(result) 
                            validate_button.visibility = False
                            quantum_limit_button.visibility = False
                            input_box.visibility = False
                            table_data = [["Process", "Arrival Time", "Burst Time", "Period", "Completion Time", "Turnaround Time", "Waiting Time"]]
                            for i in range(1, num_processes + 1):
                                table_data.append([f"P{i}", "", "", "", str(result["Completion Time"][f"P{i}"]), str(result["Turnaround Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                        result_text_box.text= "Average Turnaround Time : " + str(result["Average Turnaround Time"])
                        result_text_box2.text= "Average Waiting Time : " + str(result["Average Waiting Time"])
                        result_text_box.visibility = True
                        result_text_box2.visibility = True
                    else : print("Enter the parameters before validate")


        # Dessiner les boutons
        back_button.draw(screen)
        add_button.draw(screen)

        validate_button.draw(screen)
        quantum_limit_button.draw(screen)


        # Dessiner la table
        cell_width = 125
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
                elif col_index == 2 and row_index > 0:  # Colonne "Burst Time"    
                    burst_time_boxes[row_index - 1].draw(screen)
                elif algo_name == "Rate Monotonic":
                    if col_index == 3 and row_index > 0:  # Colonne "Quantum or Period"    
                        period_boxes[row_index - 1].draw(screen)
                    else :
                        text_surface = font.render(cell, True, (0, 0, 0))
                        text_rect = text_surface.get_rect(center=cell_rect.center)
                        screen.blit(text_surface, text_rect)
                elif algo_name == "Earliest Deadline First":
                    if col_index == 3 and row_index > 0:  # Colonne "Quantum or Period"    
                        period_boxes[row_index - 1].draw(screen)
                    elif col_index == 4 and row_index > 0:  # Colonne "Deadline"    
                        deadline_boxes[row_index - 1].draw(screen)
                    else :
                        text_surface = font.render(cell, True, (0, 0, 0))
                        text_rect = text_surface.get_rect(center=cell_rect.center)
                        screen.blit(text_surface, text_rect)
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
        pygame.time.Clock().tick(360)


