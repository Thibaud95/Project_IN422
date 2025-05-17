import pygame
pygame.init()  # Initialisation de Pygame avant toute utilisation

from pages import draw_beginner_page_2, draw_beginner_page_3, draw_beginner_page_4, draw_comparison_page, draw_homepage_1,draw_homepage_2,draw_beginner_page_1, draw_fcfs_page, draw_rr_page, draw_rm_page, draw_edf_page, draw_sjn_page

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

print("Largeur de l'écran :", screen_width, "pixels")
print("Hauteur de l'écran :", screen_height, "pixels")

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
running = True

# Variable de gestion de la page actuelle
current_page = "home"
action = None

while running:
    screen.fill((30, 30, 30))  # Fond gris foncé
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

                pygame.quit()
                exit()

    # Gestion des pages
    if current_page == "home":
        current_page = draw_homepage_1(screen)
    elif current_page == "home2" :
        current_page = draw_homepage_2(screen,action)
    elif current_page == "beginner1":
        current_page = draw_beginner_page_1(screen)
    elif current_page == "beginner2":
        current_page,action = draw_beginner_page_2(screen)
    elif current_page == "beginner3":
        current_page,action = draw_beginner_page_3(screen)
    elif current_page == "beginner4":
        current_page,action = draw_beginner_page_4(screen)
    elif current_page == "fcfs":
        current_page = draw_fcfs_page(screen)
    elif current_page == "rr":
        current_page = draw_rr_page(screen)
    elif current_page == "rm":
        current_page = draw_rm_page(screen)
    elif current_page == "edf":
        current_page = draw_edf_page(screen)
    elif current_page == "sjn":
        current_page = draw_sjn_page(screen)
    elif current_page == "comparison":
        current_page = draw_comparison_page(screen)

    pygame.display.flip()
    clock.tick(360)

pygame.quit()
