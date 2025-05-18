import pygame


from ui import Button, InputBox, Text
from FCFS_algo import FCFS
from EDF_algo import EDF
from RM_algo import RM
from RR_algo import RR
from SJN_algo import SJN


font = pygame.font.Font(None, 21)
# Variable globale pour stocker les données de comparaison
comparison_data = None

def draw_homepage_1(screen):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (screen.get_width() - button_width) // 2  # Centré horizontalement

    buttons = [
        Button(button_center_on_x, 100, button_width, button_height, "Beginner", "beginner1"),
        Button(button_center_on_x, 300, button_width, button_height, "Expert", "home2"),
        Button(button_center_on_x, 500, button_width, button_height, "Quit", "quit"),
    ]
    
    title = font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(1920 // 2, 100)))
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            page = button.handle_event(event)
            if page:
                if page == "quit":
                    pygame.quit()
                    exit()
                else:
                    return page
    return "home"

def draw_homepage_2(screen, action=None):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (screen.get_width() - button_width) // 2  # Centré horizontalement

    if action == None:
        buttons = [
            Button(100, 100, 200, 50, "Back", "home"),
            Button(button_center_on_x, 100, button_width, button_height, "First Come First Serve", "fcfs"),
            Button(button_center_on_x, 200, button_width, button_height, "Shortest Job Next", "sjn"),
            Button(button_center_on_x, 300, button_width, button_height, "Round Robin", "rr"),
            Button(button_center_on_x, 400, button_width, button_height, "Rate Monotonic", "rm"),
            Button(button_center_on_x, 500, button_width, button_height, "Earliest Deadline First", "edf"),
        ]
    elif action == "preemption":
        buttons = [
            Button(100, 100, 200, 50, "Back", "beginner2"),
            Button(button_center_on_x, 100, button_width, button_height, "First Come First Serve", "fcfs"),
            Button(button_center_on_x, 200, button_width, button_height, "Shortest Job Next", "sjn"),
        ]
    elif action == "non_preemption":
        buttons = [
            Button(100, 100, 200, 50, "Back", "beginner2"),
            Button(button_center_on_x, 300, button_width, button_height, "Round Robin", "rr"),
            Button(button_center_on_x, 400, button_width, button_height, "Rate Monotonic", "rm"),
            Button(button_center_on_x, 500, button_width, button_height, "Earliest Deadline First", "edf"),
        ]
    elif action == "soft_real_time":
        buttons = [
            Button(100, 100, 200, 50, "Back", "beginner3"),
            Button(button_center_on_x, 300, button_width, button_height, "Round Robin", "rr"),
        ]
    elif action == "hard_real_time":
        buttons = [
            Button(100, 100, 200, 50, "Back", "beginner3"),
            Button(button_center_on_x, 400, button_width, button_height, "Rate Monotonic", "rm"),
            Button(button_center_on_x, 500, button_width, button_height, "Earliest Deadline First", "edf"),
        ]
    elif action == "static_priority":
        buttons = [
            Button(100, 100, 200, 50, "Back", "beginner4"),
            Button(button_center_on_x, 400, button_width, button_height, "Rate Monotonic", "rm"),
        ]
    elif action == "dynamic_priority":
        buttons = [
            Button(100, 100, 200, 50, "Back", "beginner4"),
            Button(button_center_on_x, 500, button_width, button_height, "Earliest Deadline First", "edf"),
        ]
    
    title = font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(1920 // 2, 100)))

    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            page = button.handle_event(event)
            if page:
                return page
    return "home2"

def draw_beginner_page_1(screen):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (screen.get_width() - button_width) // 2  # Centré horizontalement

    buttons = [
        Button(button_center_on_x, 200, button_width, button_height, "Based on Preemption", "beginner2"),
        Button(button_center_on_x, 400, button_width, button_height, " Based on Timing Constraints", "beginner3"),
        Button(button_center_on_x, 600, button_width, button_height, " Based on Priority Assignments", "beginner4"),
        Button(100, 100, 200, 50, "Back", "home"),
    ] 
    
    title = font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(1920 // 2, 100)))
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                return action
    return "beginner1"

def draw_beginner_page_2(screen):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (screen.get_width() - button_width) // 2  # Centré horizontalement

    buttons = [
        Button(button_center_on_x, 300, button_width, button_height, "Preemptive Scheduling", "preemption"),
        Button(button_center_on_x, 500, button_width, button_height, "Non-Preemptive Scheduling", "non_preemption"),
        Button(100, 100, 200, 50, "Back", "beginner1"),
    ]
    
    title = font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(1920 // 2, 100)))

    text = Text(100, 200, 400, 50, "Choose the preemption type")
    text.draw(screen)
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                if action == "beginner1":
                    return (action, None)
                return ("home2", action)
    return ("beginner2", None)

def draw_beginner_page_3(screen):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (screen.get_width() - button_width) // 2  # Centré horizontalement

    buttons = [
        Button(button_center_on_x, 300, button_width, button_height, "Soft Real-Time Scheduling", "soft_real_time"),
        Button(button_center_on_x, 500, button_width, button_height, "Hard Real-Time Scheduling", "hard_real_time"),
        Button(100, 100, 200, 50, "Back", "beginner1"),
    ]
    
    title = font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(1920 // 2, 100)))

    text = Text(100, 200, 400, 50, "Choose the timing constraints type")
    text.draw(screen)
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                if action == "beginner1":
                    return (action, None)
                return ("home2", action)
    return ("beginner3", None)

def draw_beginner_page_4(screen):
    button_width = 660
    button_height = 136
    button_spacing = 25
    button_center_on_x = (screen.get_width() - button_width) // 2  # Centré horizontalement

    buttons = [
        Button(button_center_on_x, 300, button_width, button_height, "Static Priority Scheduling", "static_priority"),
        Button(button_center_on_x, 500, button_width, button_height, "Dynamic Priority Scheduling", "dynamic_priority"),
        Button(100, 100, 200, 50, "Back", "beginner1"),
    ]
    
    title = font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(1920 // 2, 100)))

    text = Text(100, 200, 400, 50, "Choose the priority assignment type")
    text.draw(screen)
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                if action == "beginner1":
                    return (action, None)
                return ("home2", action)
    return ("beginner4", None)

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

def compare_results(screen, original_algo, original_params, original_result):
    global comparison_data
    # Stocker les données originales pour comparaison
    comparison_data = {
        'original_algo': original_algo,
        'original_params': original_params,
        'original_result': original_result,
        'target_algo': None,
        'target_result': None
    }
    
    # Créer les boutons pour les autres algorithmes
    algorithms = [
        ("First Come First Serve", "fcfs"),
        ("Shortest Job Next", "sjn"),
        ("Round Robin", "rr"),
        ("Rate Monotonic", "rm"),
        ("Earliest Deadline First", "edf")
    ]
    buttons = []
    y = 200
    for name, page in algorithms:
        original_algo_lower = original_algo.lower().replace(' ', '_')
        if page != original_algo_lower:
            btn = Button((screen.get_width() - 660) // 2, y, 600, 50, name, f"compare_{page}")
            buttons.append(btn)
            y += 100

    back_btn = Button(100, 600, 200, 50, "Back", "home2")

    while True:
        screen.fill((30, 30, 30))
        title = Text((screen.get_width() - 660) // 2, 100, 400, 50, "Select Algorithm to Compare:")
        title.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Gestion des boutons
            action = back_btn.handle_event(event)
            if action:
                comparison_data = None
                return action
            
            for btn in buttons:
                action = btn.handle_event(event)
                if action and action.startswith("compare_"):
                    target_algo = action.split("_")[1]
                    comparison_data['target_algo'] = target_algo

                    # Récupère les paramètres de base
                    param1 = comparison_data['original_params']
                    # Adapte les paramètres selon l'algo cible
                    if target_algo == "fcfs":
                        parameters = [param1[0], param1[1], param1[2]] 
                        comparison_data['target_result'] = FCFS(*parameters)

                    elif target_algo == "sjn":
                        parameters = [param1[0], param1[1], param1[2]]
                        comparison_data['target_result'] = SJN(*parameters)
                    elif target_algo == "rr":
                        if original_algo == "FCFS" or original_algo == "Shortest Job Next" :
                            parameters = [param1[0],param1[1],param1[2],2]
                        elif original_algo == "Rate Monotonic" or original_algo == "Earliest Deadline First":
                            parameters = [param1[0], param1[1], param1[2],param1[-1]] 
                        comparison_data['target_result'] = RR(*parameters)
                    elif target_algo == "rm":
                        if original_algo == "FCFS" or original_algo == "Shortest Job Next" :
                            parameters = [param1[0],param1[1],param1[2], [20, 5, 10] , 2]
                        elif original_algo == "Round Robin" or original_algo == "Earliest Deadline First":
                            parameters = [param1[0], param1[1], param1[2], [20, 5, 10] , param1[-1]]
                        comparison_data['target_result'] = RM(*parameters)
                    elif target_algo == "edf":
                        if original_algo == "FCFS" or original_algo == "Shortest Job Next" :
                            parameters = [param1[0],param1[1],param1[2], [7, 4, 8] , [20, 5, 10] , 2]
                        elif original_algo == "Round Robin" :
                            parameters = [param1[0], param1[1], param1[2], [7, 4, 8], [20, 5, 10] , param1[-1]]
                        elif original_algo == "Rate Monotonic":
                            parameters = [param1[0], param1[1], param1[2], [7, 4, 8], param1[-2] , param1[-1]]
                        comparison_data['target_result'] = EDF(*parameters)
                    return "comparison"


        # Dessiner les éléments
        for btn in buttons:
            btn.draw(screen)
        back_btn.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

def draw_comparison_page(screen):
    global comparison_data
    if not comparison_data or not comparison_data['target_result']:
        return "home2"
    
    # Récupérer les données
    algo1 = comparison_data['original_algo'].lower()
    print(algo1)
    res1 = comparison_data['original_result']
    algo2 = comparison_data['target_algo'].lower()
    res2 = comparison_data['target_result']

    algo_name = {
        'fcfs': "First Come First Serve",
        'sjn': "Shortest Job Next",
        'rr': "Round Robin",
        'rm': "Rate Monotonic",
        'edf': "Earliest Deadline First",
        'first come first serve': "First Come First Serve",
        'shortest job next': "Shortest Job Next",
        'round robin': "Round Robin",
        'rate monotonic': "Rate Monotonic",
        'earliest deadline first': "Earliest Deadline First",
    }
    print(algo_name[algo1])
    print(algo_name[algo2])
    # Configuration de l'affichage
    back_btn = Button(50, 50, 150, 50, "Back", "home2")
    tables_y = 150
    cell_width = 250
    cell_height = 50
    
    while True:
        screen.fill((30, 30, 30))
        
        # Titres
        Text((screen.get_width() - 660) // 2, 100, 400, 50, algo_name[algo1]).draw(screen)
        Text((screen.get_width() - 660) // 2, 400, 400, 50, algo_name[algo2]).draw(screen)

        # Tableau pour l'algorithme original
        draw_result_table(screen, algo1, res1, 400, tables_y, cell_width, cell_height)
        
        # Tableau pour l'algorithme cible
        draw_result_table(screen, algo2, res2, 400, tables_y+300, cell_width, cell_height)
        
        # Comparaison des moyennes
        avg_y = tables_y + (len(res1['Completion Time']) + 2) * cell_height
        draw_avg_comparison(screen, algo_name[algo1], res1, algo_name[algo2], res2, (screen.get_width() - 660) // 2, avg_y)

        # Bouton de retour
        back_btn.draw(screen)
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            action = back_btn.handle_event(event)
            if action:
                comparison_data = None
                return action
        
        pygame.display.flip()
        pygame.time.Clock().tick(30)

def draw_result_table(screen, algo_name, result, x, y, cell_w, cell_h):
    # En-têtes
 columns = ["Process", "Completion Time", "Turnaround Time", "Waiting Time"]
 for i, col in enumerate(columns):
     Text(x + i*cell_w, y, cell_w, cell_h, col).draw(screen)
 
 # Données
 for row, (proc, ct) in enumerate(result['Completion Time'].items()):
     tat = result['Turnaround Time'][proc]
     wt = result['Waiting Time'][proc]
     Text(x, y + (row+1)*cell_h, cell_w, cell_h, proc).draw(screen)
     Text(x + cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(ct)).draw(screen)
     Text(x + 2*cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(tat)).draw(screen)
     Text(x + 3*cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(wt)).draw(screen)

def draw_avg_comparison(screen, algo1, res1, algo2, res2, x, y):
    avg_tat1 = res1['Average Turnaround Time']
    avg_wt1 = res1['Average Waiting Time']
    avg_tat2 = res2['Average Turnaround Time']
    avg_wt2 = res2['Average Waiting Time']
    
    # Affichage des moyennes
    Text(x, y, 300, 30, f"Average Turnaround Time: {avg_tat1:.2f}").draw(screen)
    Text(x+200, y, 300, 30, f"Average Waiting Time: {avg_wt1:.2f}").draw(screen)
    Text(x, y+500, 300, 30, f"Average Turnaround Time: {avg_tat2:.2f}").draw(screen)
    Text(x + 200, y + 500, 300, 30, f"Average Waiting Time: {avg_wt2:.2f}").draw(screen)

    # Déterminer le meilleur algorithme
    tat_winner = algo1 if avg_tat1 < avg_tat2 else algo2
    wt_winner = algo1 if avg_wt1 < avg_wt2 else algo2
    Text(x, y + 520, 400, 30, f"Best Turnaround Time: {tat_winner}").draw(screen)
    Text(x + 200, y + 520, 400, 30, f"Best Waiting Time: {wt_winner}").draw(screen)


def draw_algorithm_page(screen, algo_name):
    global comparison_data
    # Bouton "Retour"
    back_button = Button(50, 50, 150, 50, "Back", "home2")
    add_button = Button(screen.get_width() - 250, 100, 200, 50, "Add Processes", "add_processes")
    validate_button = Button(screen.get_width() - 250, 200, 200, 50, "Validate", "validate")
    validate_button.visibility = False
    compare_button = Button(screen.get_width() - 250, 200, 200, 50, "Compare", "compare")
    compare_button.visibility = False
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

            # Gestion du bouton "Compare"
            if compare_button.visibility:
                action = compare_button.handle_event(event)
                if action == "compare":
                    return compare_results(screen, algo_name, parameters, result)
            # Gestion du bouton "Validate"
            action = validate_button.handle_event(event)
            if action == "validate":
                for i in range(num_processes):
                    if arrival_time[i] != "" and burst_time[i] != "":
                        process_list = []
                        if algo_name == "FCFS" or algo_name=="Shortest Job Next":                         
                            process_list = []
                            arrival_times = []
                            burst_times = []                     
                            for i in range(len(arrival_time)):
                                process_list.append("P"+str(i+1))
                                arrival_times.append(int(arrival_time[i]))
                                burst_times.append(int(burst_time[i]))
                            if algo_name == "FCFS":
                                parameters = [process_list, arrival_times, burst_times]
                                result = FCFS(*parameters)
                                if comparison_data is not None :
                                    comparison_data['original_params'] = parameters
                                    comparison_data['original_result'] = result
                            elif algo_name == "Shortest Job Next":
                                parameters = [process_list, arrival_times, burst_times]
                                result = SJN(*parameters)
                                if comparison_data is not None :
                                    comparison_data['original_params'] = parameters
                                    comparison_data['original_result'] = result
                            print(result)
                            validate_button.visibility = False
                            compare_button.visibility = True
                            table_data = [["Process", "Arrival Time", "Burst Time","Completion Time", "Turnaround Time", "Waiting Time"]]
                            for i in range(1, num_processes + 1):
                                table_data.append([f"P{i}", "", "", str(result["Completion Time"][f"P{i}"]), str(result["Turnaround Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                        elif algo_name == "Round Robin":                         
                            process_list = []
                            arrival_times = []
                            burst_times = []                      
                            for i in range(len(arrival_time)):
                                process_list.append("P"+str(i+1))
                                arrival_times.append(int(arrival_time[i]))
                                burst_times.append(int(burst_time[i]))
                            parameters = [process_list, arrival_times, burst_times, quantum_limit_value]
                            result = RR(*parameters)
                            if comparison_data is not None :
                                    comparison_data['original_params'] = parameters
                                    comparison_data['original_result'] = result
                            print(result)
                            compare_button.visibility = True
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
                            parameters = [process_list,arrival_times, burst_times, periods, quantum_limit_value]
                            result = RM(*parameters)
                            if comparison_data is not None :
                                    comparison_data['original_params'] = parameters
                                    comparison_data['original_result'] = result
                            print(result)
                            compare_button.visibility = True 
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
                            parameters = [process_list,arrival_times, burst_times, deadlines, periods, quantum_limit_value]
                            result = EDF(*parameters)
                            if comparison_data is not None :
                                    comparison_data['original_params'] = parameters
                                    comparison_data['original_result'] = result
                            print(result)
                            compare_button.visibility = True 
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
        compare_button.draw(screen)
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


