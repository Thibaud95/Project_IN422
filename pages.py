import pygame
import webbrowser

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

from ui import Button, InputBox, Text, Label, TimelineBox
from FCFS_algo import FCFS # First Come First Serve
from EDF_algo import EDF # Earliest Deadline First
from RM_algo import RM # Rate Monotonic
from RR_algo import RR # Round Robin
from SJN_algo import SJN # Shortest Job Next

clock = pygame.time.Clock()

font = pygame.font.Font(None, 21)
# Variable globale pour stocker les données de comparaison
comparison_data = None

def draw_homepage_1(screen):
    button_width = screen_width/3
    button_height = screen_width/15
    button_spacing = screen_height/21.6
    button_center_on_x = (screen_width - button_width) // 2
    button_center_on_y = button_height 
    button_start_y = screen_height/6 

    button_font_size = int(button_height * 0.4)
    button_font = pygame.font.SysFont("Arial", button_font_size)

    buttons = [
        Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "Beginner", "beginner1",button_font),
        Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Expert", "home2",button_font),
        Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Quit", "quit",button_font),
        Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
    ]
    
    title_font_size = int(button_font_size * 2)
    title_font = pygame.font.SysFont("Arial", title_font_size)
    title = title_font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 10.8)))

    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            page = button.handle_event(event)
            if page:
                if page == "quit":
                    pygame.quit()
                    exit()
                elif page == "help":
                    webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
                else:
                    return page
    return "home"

def draw_homepage_2(screen, action=None):
    button_width = screen_width/3 
    button_height = screen_width/15
    button_spacing = screen_height/43.2
    button_center_on_x = (screen_width - button_width) // 2 
    button_center_on_y = button_height
    button_start_y = screen_height/21.6 

    button_font_size = int(button_height * 0.4)
    button_font = pygame.font.SysFont("Arial", button_font_size)

    if action == None:
        buttons = [
            Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "home", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
            Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "First Come First Serve", "fcfs",button_font),
            Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Shortest Job Next", "sjn",button_font),
            Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Round Robin", "rr",button_font),
            Button(button_center_on_x, button_start_y+4*button_center_on_y+3*button_spacing, button_width, button_height, "Rate Monotonic", "rm",button_font),
            Button(button_center_on_x, button_start_y+5*button_center_on_y+4*button_spacing, button_width, button_height, "Earliest Deadline First", "edf",button_font),
            Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        ]
    elif action == "preemption":
        buttons = [
            Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner2", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
            Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "First Come First Serve", "fcfs", button_font),
            Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Shortest Job Next", "sjn", button_font),
            Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Round Robin", "rr",button_font, active=False),
            Button(button_center_on_x, button_start_y+4*button_center_on_y+3*button_spacing, button_width, button_height, "Rate Monotonic", "rm",button_font, active=False),
            Button(button_center_on_x, button_start_y+5*button_center_on_y+4*button_spacing, button_width, button_height, "Earliest Deadline First", "edf",button_font, active=False),
            Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        ]
    elif action == "non_preemption":
        buttons = [
            Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner2", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
            Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "First Come First Serve", "fcfs", button_font, active=False),
            Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Shortest Job Next", "sjn", button_font, active=False),
            Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Round Robin", "rr", button_font),
            Button(button_center_on_x, button_start_y+4*button_center_on_y+3*button_spacing, button_width, button_height, "Rate Monotonic", "rm", button_font),
            Button(button_center_on_x, button_start_y+5*button_center_on_y+4*button_spacing, button_width, button_height, "Earliest Deadline First", "edf", button_font),
            Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        ]
    elif action == "soft_real_time":
        buttons = [
            Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner3", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
            Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "First Come First Serve", "fcfs", button_font, active=False),
            Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Shortest Job Next", "sjn", button_font, active=False),
            Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Round Robin", "rr", button_font),
            Button(button_center_on_x, button_start_y+4*button_center_on_y+3*button_spacing, button_width, button_height, "Rate Monotonic", "rm", button_font, active=False),
            Button(button_center_on_x, button_start_y+5*button_center_on_y+4*button_spacing, button_width, button_height, "Earliest Deadline First", "edf", button_font, active=False),
            Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        ]
    elif action == "hard_real_time":
        buttons = [
            Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner3", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
            Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "First Come First Serve", "fcfs",button_font, active=False),
            Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Shortest Job Next", "sjn",button_font, active=False),
            Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Round Robin", "rr",button_font, active=False),
            Button(button_center_on_x, button_start_y+4*button_center_on_y+3*button_spacing, button_width, button_height, "Rate Monotonic", "rm", button_font),
            Button(button_center_on_x, button_start_y+5*button_center_on_y+4*button_spacing, button_width, button_height, "Earliest Deadline First", "edf", button_font),
            Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        ]
    elif action == "static_priority":
        buttons = [
            Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner4", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
            Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "First Come First Serve", "fcfs",button_font, active=False),
            Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Shortest Job Next", "sjn",button_font, active=False),
            Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Round Robin", "rr",button_font, active=False),
            Button(button_center_on_x, button_start_y+4*button_center_on_y+3*button_spacing, button_width, button_height, "Rate Monotonic", "rm", button_font),
            Button(button_center_on_x, button_start_y+5*button_center_on_y+4*button_spacing, button_width, button_height, "Earliest Deadline First", "edf", button_font, active=False),
            Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        ]
    elif action == "dynamic_priority":
        buttons = [
            Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner4", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
            Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "First Come First Serve", "fcfs",button_font, active=False),
            Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Shortest Job Next", "sjn",button_font, active=False),
            Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, "Round Robin", "rr",button_font, active=False),
            Button(button_center_on_x, button_start_y+4*button_center_on_y+3*button_spacing, button_width, button_height, "Rate Monotonic", "rm", button_font, active=False),
            Button(button_center_on_x, button_start_y+5*button_center_on_y+4*button_spacing, button_width, button_height, "Earliest Deadline First", "edf", button_font),
            Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        ]

    title_font_size = int(button_font_size * 2)
    title_font = pygame.font.SysFont("Arial", title_font_size)
    title = title_font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 10.8)))

    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            page = button.handle_event(event)
            if page:
                if page == "help":
                    webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
                else :
                    return page
    return "home2"

def draw_beginner_page_1(screen):
    button_width = screen_width/3
    button_height = screen_width/15
    button_spacing = screen_height/21.6
    button_center_on_x = (screen_width - button_width) // 2
    button_center_on_y = button_height 
    button_start_y = screen_height/6 

    button_font_size = int(button_height * 0.4)
    button_font = pygame.font.SysFont("Arial", button_font_size)

    buttons = [
        Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "Based on Preemption", "beginner2", button_font),
        Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, " Based on Timing Constraints", "beginner3", button_font),
        Button(button_center_on_x, button_start_y+3*button_center_on_y+2*button_spacing, button_width, button_height, " Based on Priority Assignments", "beginner4", button_font),
        Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "home", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
    ]

    title_font_size = int(button_font_size * 2)
    title_font = pygame.font.SysFont("Arial", title_font_size)
    title = title_font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 10.8)))

    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                if action == "help":
                    webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
                else :
                    return action
    return "beginner1"

def draw_beginner_page_2(screen):
    button_width = screen_width/3
    button_height = screen_width/15
    button_spacing = screen_height/21.6
    button_center_on_x = (screen_width - button_width) // 2
    button_center_on_y = button_height 
    button_start_y = screen_height/6 

    button_font_size = int(button_height * 0.4)
    button_font = pygame.font.SysFont("Arial", button_font_size)

    buttons = [
        Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "Preemptive Scheduling", "preemption", button_font),
        Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Non-Preemptive Scheduling", "non_preemption", button_font),
        Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner1", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
    ]

    title_font_size = int(button_font_size * 2)
    title_font = pygame.font.SysFont("Arial", title_font_size)
    title = title_font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 10.8)))

    text = Text(screen_width/19.2, screen_height/5.4, screen_width/4.8, screen_height/21.6, "Choose the preemption type")
    text.draw(screen)
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                if action == "beginner1":
                    return (action, None)
                elif action == "help":
                    webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
                else : 
                    return ("home2", action)
    return ("beginner2", None)

def draw_beginner_page_3(screen):
    button_width = screen_width/3
    button_height = screen_width/15
    button_spacing = screen_height/21.6
    button_center_on_x = (screen_width - button_width) // 2
    button_center_on_y = button_height 
    button_start_y = screen_height/6 

    button_font_size = int(button_height * 0.4)
    button_font = pygame.font.SysFont("Arial", button_font_size)

    buttons = [
        Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "Soft Real-Time Scheduling", "soft_real_time", button_font),
        Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Hard Real-Time Scheduling", "hard_real_time", button_font),
        Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner1", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
    ]

    title_font_size = int(button_font_size * 2)
    title_font = pygame.font.SysFont("Arial", title_font_size)
    title = title_font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 10.8)))

    text = Text(screen_width/19.2, screen_height/5.4, screen_width/4.8, screen_height/21.6, "Choose the timing constraints type")
    text.draw(screen)
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                if action == "beginner1":
                    return (action, None)
                elif action == "help":
                    webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
                else: 
                    return ("home2", action)
    return ("beginner3", None)

def draw_beginner_page_4(screen):
    button_width = screen_width/3
    button_height = screen_width/15
    button_spacing = screen_height/21.6
    button_center_on_x = (screen_width - button_width) // 2
    button_center_on_y = button_height 
    button_start_y = screen_height/6 

    button_font_size = int(button_height * 0.4)
    button_font = pygame.font.SysFont("Arial", button_font_size)

    buttons = [
        Button(button_center_on_x, button_start_y+button_center_on_y, button_width, button_height, "Static Priority Scheduling", "static_priority", button_font),
        Button(button_center_on_x, button_start_y+2*button_center_on_y+button_spacing, button_width, button_height, "Dynamic Priority Scheduling", "dynamic_priority", button_font),
        Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "beginner1", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
        Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7))),
    ]
    
    title_font_size = int(button_font_size * 2)
    title_font = pygame.font.SysFont("Arial", title_font_size)
    title = title_font.render("Tasks Manager", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 10.8)))

    text = Text(screen_width/19.2, screen_height/5.4, screen_width/4.8, screen_height/21.6, "Choose the priority assignment type")
    text.draw(screen)
    
    for button in buttons:
        button.draw(screen)

    for event in pygame.event.get():
        for button in buttons :
            action = button.handle_event(event)
            if action:
                if action == "beginner1":
                    return (action, None)
                elif action == "help":
                    webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
                else:
                    return ("home2", action)
    return ("beginner4", None)

def draw_fcfs_page(screen):
    return draw_algorithm_page(screen, "First Come First Serve")

def draw_rr_page(screen):
    return draw_algorithm_page(screen, "Round Robin")

def draw_rm_page(screen):
    return draw_algorithm_page(screen, "Rate Monotonic")

def draw_edf_page(screen):
    return draw_algorithm_page(screen, "Earliest Deadline First")

def draw_sjn_page(screen):
    return draw_algorithm_page(screen, "Shortest Job Next")

# def ask_for_parameter(screen, label):
#     input_box = InputBox(screen_width // 2 - (screen_width/19.2), screen_height // 2, screen_width/9.6, screen_height/21.6, '', font)
#     font = pygame.font.Font(None, 36)
#     validate_button = Button(screen_width // 2 - (screen_width/19.2), screen_height // 2 + (screen_height/15), screen_width/9.6, screen_height/21.6, "Validate", "validate")
#     while True:
#         screen.fill((30, 30, 30))
#         text = font.render(label, True, (255, 255, 255))
#         screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - screen_height // 18))
#         input_box.draw(screen)
#         validate_button.draw(screen)
#         pygame.display.flip()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             input_box.handle_event(event)
#             action = validate_button.handle_event(event)
#             if action == "validate":
#                 try:
#                     return input_box.text
#                 except ValueError:
#                     pass  # Ignore invalid input, let user retry
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
#                 try:
#                     return input_box.text
#                 except ValueError:
#                     pass  # Ignore invalid input, let user retry
#         #clock.tick(360)

# def compare_results(screen, original_algo, original_params, original_result):
#     global comparison_data
#     # Stocker les données originales pour comparaison
#     comparison_data = {
#         'original_algo': original_algo,
#         'original_params': original_params,
#         'original_result': original_result,
#         'target_algo': None,
#         'target_result': None
#     }
    
#     # Créer les boutons pour les autres algorithmes
#     algorithms = [
#         ("First Come First Serve", "fcfs"),
#         ("Shortest Job Next", "sjn"),
#         ("Round Robin", "rr"),
#         ("Rate Monotonic", "rm"),
#         ("Earliest Deadline First", "edf")
#     ]
#     buttons = []
#     y = screen_height/5.4
#     for name, page in algorithms:
#         original_algo_lower = original_algo.lower().replace(' ', '_')
#         if page != original_algo_lower:
#             btn = Button((screen_width - screen_width/2.91) // 2, y, screen_width/3.2, screen_height/21.6, name, f"compare_{page}")
#             buttons.append(btn)
#             y += 100

#     back_btn = Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "home2", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
#     help_btn = Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))

#     while True:
#         screen.fill((30, 30, 30))
#         title = Text((screen_width - screen_width/2.91) // 2, screen_height/10.8, screen_width/4.8, screen_height/21.6, "Select Algorithm to Compare:")
#         title.draw(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
            
#             # Gestion des boutons
#             action = back_btn.handle_event(event)
#             if action:
#                 comparison_data = None
#                 return action
            
#             action = help_btn.handle_event(event)
#             if action:
#                 webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
            
#             for btn in buttons:
#                 action = btn.handle_event(event)
#                 if action and action.startswith("compare_"):
#                     target_algo = action.split("_")[1]
#                     comparison_data['target_algo'] = target_algo

#                     # Récupère les paramètres de base
#                     param1 = comparison_data['original_params']
#                     # Adapte les paramètres selon l'algo cible
#                     if target_algo == "fcfs":
#                         parameters = [param1[0], param1[1], param1[2]] 
#                         comparison_data['target_result'] = FCFS(*parameters)
#                     elif target_algo == "sjn":
#                         parameters = [param1[0], param1[1], param1[2]]
#                         comparison_data['target_result'] = SJN(*parameters)
#                     elif target_algo == "rr":
#                         if len(param1) < 4 :
#                             quantum = int(ask_for_parameter(screen, "Quantum value for Round Robin?"))
#                             parameters = [param1[0], param1[1], param1[2], quantum]
#                         else:
#                             parameters = [param1[0], param1[1], param1[2], param1[-1]]
#                         comparison_data['target_result'] = RR(*parameters)
#                     elif target_algo == "rm":
#                         if len(param1) < 5:
#                             limit = int(ask_for_parameter(screen, "Limit value for Rate Monotonic?"))
#                             period_str = ask_for_parameter(screen, "Period value for Rate Monotonic?")
#                             period = [int(x) for x in period_str.replace(',', ' ').split()]
#                             parameters = [param1[0], param1[1], param1[2], period, limit]
#                         else:
#                             parameters = [param1[0], param1[1], param1[2], param1[-2], param1[-1]]
#                         comparison_data['target_result'] = RM(*parameters)
#                     elif target_algo == "edf":
#                         if len(param1) < 5:
#                             limit = int(ask_for_parameter(screen, "Limit value for Earliest Deadline First?"))
#                             period_str = ask_for_parameter(screen, "Period value for Earliest Deadline First?")
#                             period = [int(x) for x in period_str.replace(',', ' ').split()]
#                         else : 
#                             limit = param1[-1]
#                             period = param1[-2]
#                         deadlines_str = ask_for_parameter(screen, "Deadline value for Earliest Deadline First?")
#                         deadlines = [int(x) for x in deadlines_str.replace(',', ' ').split()]
#                         parameters = [param1[0], param1[1], param1[2], deadlines, period, limit]
#                         comparison_data['target_result'] = EDF(*parameters)
#                     return "comparison"


#         # Dessiner les éléments
#         for btn in buttons:
#             btn.draw(screen)
#         back_btn.draw(screen)
#         help_btn.draw(screen)
#         pygame.display.flip()
#         #clock.tick(360)

# def draw_comparison_page(screen):
#     global comparison_data
#     if not comparison_data or not comparison_data['target_result']:
#         return "home2"
    
#     # Récupérer les données
#     algo1 = comparison_data['original_algo'].lower()
#     res1 = comparison_data['original_result']
#     algo2 = comparison_data['target_algo'].lower()
#     res2 = comparison_data['target_result']

#     algo_name = {
#         'fcfs': "First Come First Serve",
#         'sjn': "Shortest Job Next",
#         'rr': "Round Robin",
#         'rm': "Rate Monotonic",
#         'edf': "Earliest Deadline First",
#         'first come first serve': "First Come First Serve",
#         'shortest job next': "Shortest Job Next",
#         'round robin': "Round Robin",
#         'rate monotonic': "Rate Monotonic",
#         'earliest deadline first': "Earliest Deadline First",
#     }
#     # Configuration de l'affichage
#     back_btn = Button(screen_width/96, screen_height/54, screen_width/12.8, screen_height/21.6, "Back", "home2", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
#     help_btn = Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
#     tables_y = screen_height/7.2
#     cell_width = screen_width/7.68
#     cell_height = screen_height/21.6
    
#     while True:
#         screen.fill((30, 30, 30))
        
#         # Titres
#         Text((screen_width - screen_width/2.91) // 2, screen_height/10.8, screen_width/4.8, screen_height/21.6, algo_name[algo1]).draw(screen)
#         Text((screen_width - screen_width/2.91) // 2, screen_height/2.7, screen_width/4.8, screen_height/21.6, algo_name[algo2]).draw(screen)

#         # Tableau pour l'algorithme original
#         draw_result_table(screen, algo1, res1, screen_width/4.8, tables_y, cell_width, cell_height)
        
#         # Tableau pour l'algorithme cible
#         draw_result_table(screen, algo2, res2, screen_width/4.8, tables_y+screen_height/3.6, cell_width, cell_height)
        
#         # Comparaison des moyennes
#         avg_y = tables_y + (len(res1['Completion Time']) + 2) * cell_height
#         draw_avg_comparison(screen, algo_name[algo1], res1, algo_name[algo2], res2, (screen_width - screen_width/2.91) // 2, avg_y)

#         # Bouton de retour
#         back_btn.draw(screen)
#         help_btn.draw(screen)
        
#         # Gestion des événements
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             action = back_btn.handle_event(event)
#             if action:
#                 comparison_data = None
#                 return action
            
#             action = help_btn.handle_event(event)
#             if action:
#                 webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
        
#         pygame.display.flip()
#         #clock.tick(360)

# def draw_result_table(screen, algo_name, result, x, y, cell_w, cell_h):
#     # En-têtes
#     columns = ["Process", "Completion Time", "Turnaround Time", "Waiting Time"]
#     for i, col in enumerate(columns):
#         Text(x + i*cell_w, y, cell_w, cell_h, col).draw(screen)
    
#     # Données
#     for row, (proc, ct) in enumerate(result['Completion Time'].items()):
#         tat = result['Turnaround Time'][proc]
#         wt = result['Waiting Time'][proc]
#         Text(x, y + (row+1)*cell_h, cell_w, cell_h, proc).draw(screen)
#         Text(x + cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(ct)).draw(screen)
#         Text(x + 2*cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(tat)).draw(screen)
#         Text(x + 3*cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(wt)).draw(screen)
#     #clock.tick(360)

# def draw_avg_comparison(screen, algo1, res1, algo2, res2, x, y):
#     avg_tat1 = res1['Average Turnaround Time']
#     avg_wt1 = res1['Average Waiting Time']
#     avg_tat2 = res2['Average Turnaround Time']
#     avg_wt2 = res2['Average Waiting Time']
    
#     # Affichage des moyennes
#     Text(x, y, screen_width/6.4, screen_height/36, f"Average Turnaround Time: {avg_tat1:.2f}").draw(screen)
#     Text(x + screen_width/9.6*3, y, screen_width/6.4, screen_height/36, f"Average Waiting Time: {avg_wt1:.2f}").draw(screen)
#     Text(x, y + screen_height//3.5, screen_width/6.4, screen_height/36, f"Average Turnaround Time: {avg_tat2:.2f}").draw(screen)
#     Text(x + screen_width/9.6*3, y + screen_height//3.5, screen_width/6.4, screen_height/36, f"Average Waiting Time: {avg_wt2:.2f}").draw(screen)

#     # Déterminer le meilleur algorithme
#     tat_winner = algo1 if avg_tat1 < avg_tat2 else algo2
#     wt_winner = algo1 if avg_wt1 < avg_wt2 else algo2
#     Text(x, y + screen_height//3, screen_width/4.8, screen_height/36, f"Best Turnaround Time: {tat_winner}").draw(screen)
#     Text(x + screen_width/9.6*3, y + screen_height//3, screen_width/4.8, screen_height/36, f"Best Waiting Time: {wt_winner}").draw(screen)
#     #clock.tick(360)

def ask_for_parameter(screen, label):
    input_box = InputBox(screen_width // 2 - screen_width/19.2, screen_width // 2, screen_width/9.6, screen_height/21.6)
    font = pygame.font.Font(None, 36)
    validate_button = Button(screen_width // 2 - screen_width/19.2, screen_width // 2 + screen_height/15, screen_width/9.6, screen_height/21.6, "Validate", "validate")
    help_button = Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
    while True:
        screen.fill((30, 30, 30))
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - screen_height / 18))
        input_box.draw(screen)
        validate_button.draw(screen)
        help_button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            input_box.handle_event(event)
            action = validate_button.handle_event(event)
            if action == "validate":
                try:
                    return input_box.text
                except ValueError:
                    pass  # Ignore invalid input, let user retry
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                try:
                    return input_box.text
                except ValueError:
                    pass  # Ignore invalid input, let user retry
            action = help_button.handle_event(event)
            if action == "help":
                webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
        #clock.tick(360)

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
    y = 1
    for name, page in algorithms:
        original_algo_lower = original_algo.lower().replace(' ', '_')
        if page != original_algo_lower:
            btn = Button((screen_width - screen_width/3) // 2, screen_height/21.6+(screen_width/15)*(y)+(screen_height/43.2)*(y-1), screen_width/3 , screen_width/15, name, f"compare_{page}", pygame.font.SysFont("Arial", int(screen_width/15 * 0.4)))
            buttons.append(btn)
            y += 1

    back_btn = Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "home2", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
    help_btn = Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))

    while True:
        screen.fill((30, 30, 30))
        title = Text((screen_width - screen_width/9.6) // 2, screen_height/21.6, screen_width/9.6, screen_height/10.8, "Select Algorithm to Compare:", pygame.font.SysFont("Arial", int(screen_width/15 * 0.6)))
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
            
            action = help_btn.handle_event(event)
            if action:
                webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")

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
                        quantum = int(ask_for_parameter(screen, "Quantum value for Round Robin?"))
                        parameters = [param1[0], param1[1], param1[2], quantum]
                        comparison_data['target_result'] = RR(*parameters)
                    elif target_algo == "rm":
                        if len(param1) < 5:
                            limit = int(ask_for_parameter(screen, "Limit value for Rate Monotonic?"))
                            period_str = ask_for_parameter(screen, "Period value for Rate Monotonic?")
                            period = [int(x) for x in period_str.replace(',', ' ').split()]
                            parameters = [param1[0], param1[1], param1[2], period, limit]
                        else:
                            parameters = [param1[0], param1[1], param1[2], param1[-2], param1[-1]]
                        comparison_data['target_result'] = RM(*parameters)
                    elif target_algo == "edf":
                        if len(param1) < 5:
                            limit = int(ask_for_parameter(screen, "Limit value for Earliest Deadline First?"))
                            period_str = ask_for_parameter(screen, "Period value for Earliest Deadline First?")
                            period = [int(x) for x in period_str.replace(',', ' ').split()]
                        else : 
                            limit = param1[-1]
                            period = param1[-2]
                        deadlines_str = ask_for_parameter(screen, "Deadline value for Earliest Deadline First?")
                        deadlines = [int(x) for x in deadlines_str.replace(',', ' ').split()]
                        parameters = [param1[0], param1[1], param1[2], deadlines, period, limit]
                        comparison_data['target_result'] = EDF(*parameters)
                    return "comparison"
        #clock.tick(360)


        # Dessiner les éléments
        for btn in buttons:
            btn.draw(screen)
        back_btn.draw(screen)
        help_btn.draw(screen)
        pygame.display.flip()
        #clock.tick(360)

def draw_comparison_page(screen):
    global comparison_data
    if not comparison_data or not comparison_data['target_result']:
        return "home2"
    
    # Récupérer les données
    algo1 = comparison_data['original_algo'].lower()
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
    # Configuration de l'affichage
    back_btn = Button(screen_width/19.2, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Back", "home2", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
    help_btn = Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
    tables_y = screen_height/7.2
    cell_width = screen_width/7.68
    cell_height = screen_height/21.6
    
    while True:
        screen.fill((30, 30, 30))
        
        # Titres
        Text((screen_width - screen_width/2.91) // 2, screen_height/10.8, screen_width/4.8, screen_height/21.6, algo_name[algo1]).draw(screen)
        Text((screen_width - screen_width/2.91) // 2, screen_height/2.7, screen_width/4.8, screen_height/21.6, algo_name[algo2]).draw(screen)

        # Tableau pour l'algorithme original
        draw_result_table(screen, algo1, res1, screen_width/4.8, tables_y, cell_width, cell_height)
        
        # Tableau pour l'algorithme cible
        draw_result_table(screen, algo2, res2, screen_width/4.8, tables_y+screen_height/3.6, cell_width, cell_height)
        
        # Comparaison des moyennes
        if algo1 == "fcfs" or algo1 == "sjn" or algo1 == "rr" or algo1 == "first come first serve" or algo1 == "shortest job next" or algo1 == "round robin":
            avg_y = tables_y + (len(res1['Completion Time']) + 2) * cell_height
        elif algo1 == "rm" or algo1 == "edf" or algo1 == "rate monotonic" or algo1 == "earliest deadline first":
            avg_y = tables_y + (len(res1['Response Time']) + 2) * cell_height
        draw_avg_comparison(screen, algo_name[algo1], res1, algo_name[algo2], res2, (screen_width - screen_width/2.91) // 2, avg_y)

        # Bouton de retour
        back_btn.draw(screen)
        help_btn.draw(screen)
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            action = back_btn.handle_event(event)
            if action:
                comparison_data = None
                return action
            
            action = help_btn.handle_event(event)
            if action:
                webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")
        
        pygame.display.flip()
        #clock.tick(360)

def draw_result_table(screen, algo_name, result, x, y, cell_w, cell_h):
    # En-têtes
    if algo_name == "fcfs" or algo_name == "sjn" or algo_name == "rr" or algo_name == "first come first serve" or algo_name == "shortest job next" or algo_name == "round robin":
        columns = ["Process", "Completion Time", "Turnaround Time", "Waiting Time"]
    elif algo_name == "rm" or algo_name == "edf" or algo_name == "rate monotonic" or algo_name == "earliest deadline first":
        columns = ["Process", "Response Time", "Waiting Time"]
    for i, col in enumerate(columns):
        Text(x + i*cell_w, y, cell_w, cell_h, col).draw(screen)

    # Données
    if algo_name == "fcfs" or algo_name == "sjn" or algo_name == "rr" or algo_name == "first come first serve" or algo_name == "shortest job next" or algo_name == "round robin":
        for row, (proc, ct) in enumerate(result['Completion Time'].items()):
            tat = result['Turnaround Time'][proc]
            wt = result['Waiting Time'][proc]
            Text(x, y + (row+1)*cell_h, cell_w, cell_h, proc).draw(screen)
            Text(x + cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(ct)).draw(screen)
            Text(x + 2*cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(tat)).draw(screen)
            Text(x + 3*cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(wt)).draw(screen)
    elif algo_name == "rm" or algo_name == "edf" or algo_name == "rate monotonic" or algo_name == "earliest deadline first":
        response_times = result.get('Response Time', {})
        waiting_times = result.get('Waiting Time', {})
        procs = list(response_times.keys())
        for row, proc in enumerate(procs):
            rt = response_times.get(proc, "")
            wt = waiting_times.get(proc, "")
            Text(x, y + (row+1)*cell_h, cell_w, cell_h, proc).draw(screen)
            Text(x + cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(rt)).draw(screen)
            Text(x + 2*cell_w, y + (row+1)*cell_h, cell_w, cell_h, str(wt)).draw(screen)

def draw_avg_comparison(screen, algo1, res1, algo2, res2, x, y):
    # Déterminer les clés à utiliser selon l'algo
    def get_keys(algo):
        if algo in ["Rate Monotonic", "Earliest Deadline First", "rate monotonic", "earliest deadline first", "rm", "edf"]:
            return "Response Time", "Waiting Time"
        else:
            return "Turnaround Time", "Waiting Time"

    key1, wait_key1 = get_keys(algo1)
    key2, wait_key2 = get_keys(algo2)

    # Récupérer les valeurs moyennes
    avg1 = res1.get(f'Average {key1}', None)
    avg_wt1 = res1.get('Average Waiting Time', None)
    avg2 = res2.get(f'Average {key2}', None)
    avg_wt2 = res2.get('Average Waiting Time', None)
    
    # Affichage des moyennes
    Text(x, y, screen_width/6.4, screen_height/36, f"Average {key1}: {avg1:.2f}" if avg1 is not None else f"Average {key1}: N/A").draw(screen)
    Text(x+screen_width/9.6*2, y, screen_width/6.4, screen_height/36, f"Average Waiting Time: {avg_wt1:.2f}" if avg_wt1 is not None else "Average Waiting Time: N/A").draw(screen)
    Text(x, y+screen_height//3.5, screen_width/6.4, screen_height/36, f"Average {key2}: {avg2:.2f}" if avg2 is not None else f"Average {key2}: N/A").draw(screen)
    Text(x + screen_width/9.6*2, y + screen_height//3.5, screen_width/6.4, screen_height/36, f"Average Waiting Time: {avg_wt2:.2f}" if avg_wt2 is not None else "Average Waiting Time: N/A").draw(screen)

    # Déterminer le meilleur algorithme)
    if avg1 is not None and avg2 is not None and avg1 == avg2:
        tat_winner = "None"
    else:
        tat_winner = algo1 if (avg1 is not None and avg2 is not None and avg1 < avg2) else algo2

    if avg_wt1 is not None and avg_wt2 is not None and avg_wt1 == avg_wt2:
        wt_winner = "None"
    else:
        wt_winner = algo1 if (avg_wt1 is not None and avg_wt2 is not None and avg_wt1 < avg_wt2) else algo2

    if (algo1 == "First Come First Serve" or algo1 == "Shortest Job Next" or algo1 == "Round Robin") and (algo2 == "First Come First Serve" or algo2 == "Shortest Job Next" or algo2 == "Round Robin"):
        Text(x, y + screen_height//3, screen_width/4.8, screen_height/36, f"Best Turnaround Time: {tat_winner}").draw(screen)
    elif (algo1 == "Rate Monotonic" or algo1 == "Earliest Deadline First") and (algo2 == "Rate Monotonic" or algo2 == "Earliest Deadline First"):
        Text(x, y + screen_height//3, screen_width/4.8, screen_height/36, f"Best Response Time: {tat_winner}").draw(screen)
    else:
        pass
    Text(x + screen_width/9.6*2, y + screen_height//3, screen_width/4.8, screen_height/36, f"Best Waiting Time: {wt_winner}").draw(screen)
    #clock.tick(360)


def draw_algorithm_page(screen, algo_name):
    global comparison_data
    # Bouton "Retour"
    back_button = Button(screen_width/96, screen_height/54, screen_width/12.8, screen_height/21.6, "Back", "home2", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
    help_button = Button(screen_width/19.2, screen_height-(screen_height/10.8+screen_height/21.6), screen_width/9.6, screen_height/21.6, "Help", "help", pygame.font.SysFont("Arial", int(screen_height/21.6 * 0.7)))
    add_button = Button(screen_width - screen_width/7.68, screen_height/10.8, screen_width/9.6, screen_height/21.6, "Add Processes", "add_processes")
    validate_button = Button(screen_width - screen_width/7.68, screen_height/5.4, screen_width/9.6, screen_height/21.6, "Validate", "validate")
    validate_button.visibility = False
    compare_button = Button(screen_width - screen_width/7.68, screen_height/3.6, screen_width/9.6, screen_height/21.6, "Compare", "compare")
    compare_button.visibility = False
    start_simulation_button = Button(screen_width - screen_width/7.68, screen_height/2.7, screen_width/9.6, screen_height/21.6, "Start Simulation", "start_simulation")
    start_simulation_button.visibility = False
    value_text = "Init"
    if algo_name == "Round Robin":
        value_text = "Set quantum"
    elif algo_name == "Earliest Deadline First":
        value_text = "Set time limit"
    elif algo_name == "Rate Monotonic":
        value_text = "Set total time"
    quantum_limit_button = Button(screen_width - screen_width/7.68, screen_height/2.16, screen_width/9.6, screen_height/21.6, value_text, "set_values")
    quantum_limit_button.visibility = False


    # Titre de la page
    title_font_size = int((screen_height // 10.8)*0.7)
    title_font = pygame.font.SysFont("Arial", title_font_size)

    title = title_font.render(algo_name, True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 10.8)))

    # Création de l'InputBox pour le nombre de processus
    input_box = InputBox(screen_width - screen_width/7.68, screen_height/21.6, screen_width/9.6, screen_height/21.6)

    # Liste pour stocker les InputBox de la colonne "Arrival Time"
    arrival_time_boxes = []
    burst_time_boxes = []
    period_boxes = []
    deadline_boxes = []
    if algo_name == "First Come First Serve" or algo_name == "Shortest Job Next":
        table_data = [["Process", "Arrival Time", "Burst Time"]]
    elif algo_name == "Round Robin":
        table_data = [["Process", "Arrival Time", "Burst Time"]]
    elif algo_name == "Rate Monotonic":
        table_data = [["Process", "Arrival Time", "Execution Time", "Period"]]
    elif algo_name == "Earliest Deadline First":
        table_data = [["Process", "Arrival Time", "Execution Time",  "Period", "Deadline"]]
  
    result_text_box = Text(screen_width/2-screen_width//4.27, screen_height/2+screen_width/6.4, screen_width/4.8, screen_height/21.6, "Résultat")
    result_text_box.visibility = False
    result_text_box2 = Text(screen_width/2+screen_width/38.4, screen_height/2+screen_width/6.4, screen_width/4.8, screen_height/21.6, "Résultat")
    result_text_box2.visibility = False

    ##########------------------------------##########
    schedule = []
    simulation_active = False
    simulation_step = 0
    last_update_time = pygame.time.get_ticks()
    ##########------------------------------##########

    # Boucle interne pour gérer les événements
    while True:
        screen.fill((30, 30, 30))  # Fond gris foncé
        screen.blit(title, (screen_width//3.5, screen_height/21.6))  # Dessiner le titre

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Gestion du bouton "Retour"
            action = back_button.handle_event(event)
            if action:
                return action  # Sortir de la fonction si "Retour" est cliqué
            
            action = help_button.handle_event(event)
            if action:
                webbrowser.open("https://github.com/Thibaud95/Project_IN422/blob/main/README.md")

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
                        if algo_name == "First Come First Serve" or algo_name == "Shortest Job Next":
                            table_data.append([f"P{i}", "", ""])
                        elif algo_name == "Round Robin":
                            table_data.append([f"P{i}", "", ""])
                            quantum_limit_button.visibility = True
                            input_box.visibility = True
                        elif algo_name == "Rate Monotonic":
                            table_data.append([f"P{i}", "", "", ""])
                            period_boxes.append(InputBox(screen_width//4.52, screen_height/7.2 + i * screen_height/21.6, screen_width/15.36, screen_height/21.6))
                            quantum_limit_button.visibility = True
                            input_box.visibility = True
                        elif algo_name == "Earliest Deadline First":
                            table_data.append([f"P{i}", "", "", "", ""])
                            period_boxes.append(InputBox(screen_width//4.52, screen_height/7.2 + i * screen_height/21.6, screen_width/15.36, screen_height/21.6))
                            deadline_boxes.append(InputBox(screen_width//3.5, screen_height/7.2 + i * screen_height/21.6, screen_width/15.36, screen_height/21.6))
                            quantum_limit_button.visibility = True
                            input_box.visibility = True
                        # Ajouter une InputBox pour chaque ligne dans la colonne "Arrival Time"
                        arrival_time_boxes.append(InputBox(screen_width/10.97, screen_height/7.2 + i * screen_height/21.6, screen_width/15.36, screen_height/21.6))
                        burst_time_boxes.append(InputBox(screen_width/6.4, screen_height/7.2 + i * screen_height/21.6, screen_width/15.36, screen_height/21.6))

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
                        if algo_name == "First Come First Serve" or algo_name=="Shortest Job Next":
                            process_list = []
                            arrival_times = []
                            burst_times = []                     
                            for i in range(len(arrival_time)):
                                process_list.append("P"+str(i+1))
                                arrival_times.append(int(arrival_time[i]))
                                burst_times.append(int(burst_time[i]))
                            if algo_name == "First Come First Serve":
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
                            execution_times = []
                            periods = []                       
                            for i in range(len(arrival_time)):
                                process_list.append("P"+str(i+1))
                                arrival_times.append(int(arrival_time[i]))
                                execution_times.append(int(burst_time[i]))
                                periods.append(int(period[i]))
                            parameters = [process_list,arrival_times, execution_times, periods, quantum_limit_value]
                            result = RM(*parameters)
                            if comparison_data is not None :
                                    comparison_data['original_params'] = parameters
                                    comparison_data['original_result'] = result
                            print(result)
                            compare_button.visibility = True 
                            validate_button.visibility = False
                            quantum_limit_button.visibility = False
                            input_box.visibility = False
                            table_data = [["Process", "Arrival Time", "Execution Time", "Period", "Completion Time", "Turnaround Time", "Waiting Time"]]
                            for i in range(1, num_processes + 1):
                                table_data.append([f"P{i}", "", "", "", str(result["Response Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                        elif algo_name == "Earliest Deadline First":
                            process_list = []
                            arrival_times = []
                            execution_times = []
                            deadlines = [] 
                            periods = []                      
                            for i in range(len(arrival_time)):
                                process_list.append("P"+str(i+1))
                                arrival_times.append(int(arrival_time[i]))
                                execution_times.append(int(burst_time[i]))
                                deadlines.append(int(deadline[i]))
                                periods.append(int(period[i]))
                            parameters = [process_list,arrival_times, execution_times, deadlines, periods, quantum_limit_value]
                            result = EDF(*parameters)
                            if comparison_data is not None :
                                    comparison_data['original_params'] = parameters
                                    comparison_data['original_result'] = result
                            print(result)
                            compare_button.visibility = True 
                            validate_button.visibility = False
                            quantum_limit_button.visibility = False
                            input_box.visibility = False
                            
                            table_data = [["Process", "Arrival Time", "Execution Time", "Period", "Completion Time", "Turnaround Time", "Waiting Time"]]
                            for i in range(1, num_processes + 1):
                                table_data.append([f"P{i}", "", "", "","", str(result["Response Time"][f"P{i}"]), str(result["Waiting Time"][f"P{i}"])])
                        if algo_name == "FCFS" or algo_name=="Shortest Job Next" or algo_name=="Round Robin":
                            result_text_box.text= "Average Turnaround Time : " + str(result["Average Turnaround Time"])
                        elif algo_name == "Rate Monotonic" or algo_name == "Earliest Deadline First":
                            result_text_box.text= "CPU Utilization : " + str(result["CPU Utilization"])
                        result_text_box2.text = f"Average Waiting Time : {result['Average Waiting Time']:.2f}"
                        result_text_box.visibility = True
                        result_text_box2.visibility = True

                        ##########------------------------------------------------------------##########
                        start_simulation_button.visibility = True
                        simulation_active = False  # Initialise la simulation
                        simulation_step = 0
                        ##########------------------------------------------------------------##########

                    else : print("Enter the parameters before validate")
            ##########------------------------------------------------------------##########
            action = start_simulation_button.handle_event(event)
            if action == "start_simulation":
                if "Schedule" in result:
                    schedule = result["Schedule"]
                    simulation_active = True
                    simulation_step = 0
                    last_update_time = pygame.time.get_ticks()
            ##########------------------------------------------------------------##########




        # Dessiner les boutons
        back_button.draw(screen)
        help_button.draw(screen)
        add_button.draw(screen)

        validate_button.draw(screen)
        compare_button.draw(screen)
        quantum_limit_button.draw(screen)
        start_simulation_button.draw(screen)


        # Dessiner la table
        cell_width = screen_width/15.36
        cell_height = screen_height/21.6
        table_x = screen_width/38.4
        table_y = screen_height/7.2

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
        ##########------------------------------------------------------------##########
        if simulation_active and simulation_step < len(schedule):
            now = pygame.time.get_ticks()
            if now - last_update_time >= 500:
                simulation_step += 1
                last_update_time = now

            if simulation_step < len(schedule):
                # Safely get the current process (can be None)
                current_process = schedule[simulation_step]

                # Ready queue (from next time step onward)
                ready_queue = schedule[simulation_step + 1:] if simulation_step + 1 < len(schedule) else []

                # Display the Ready Queue content or "Empty"
                if ready_queue:
                    formatted_queue = ", ".join([p if p is not None else "None" for p in ready_queue[:5]]) # You can adjust the number of processes displayed in the queue
                else:
                    formatted_queue = "Empty"

                ready_label = Label(screen_width/38.4, screen_height/2.7, screen_width/2.56, screen_height/21.6, "Ready Queue: " + formatted_queue, bg_color=(0, 255, 100))
                ready_label.draw(screen)

                # Display CPU content, even if it's None
                cpu_text = f"CPU: {current_process if current_process is not None else 'None'}"
                cpu_label = Label(screen_width/38.4, screen_height//2.35, screen_width/2.56, screen_height/21.6, cpu_text, bg_color=(0, 255, 100))
                cpu_label.draw(screen)

            # Draw Timeline
            time_x = screen_height/21.6
            timeline_y = screen_height - screen_height/2.7
            for i, pid in enumerate(schedule):
                active = (i == simulation_step and simulation_step < len(schedule))
                timeline_box = TimelineBox(time_x + i * (screen_height/21.6), timeline_y, screen_height/22.5, screen_height/22.5, pid, active=active)
                timeline_box.draw(screen)
        ##########------------------------------------------------------------##########

        pygame.display.flip()
        clock.tick(360)


