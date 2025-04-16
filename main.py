import pygame
pygame.init()  # Initialisation de Pygame avant toute utilisation

from pages import draw_homepage, draw_fcfs_page, draw_rr_page, draw_rm_page, draw_edf_page, draw_sjn_page

# Reste du code...

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Variable de gestion de la page actuelle
current_page = "home"

while running:
    screen.fill((30, 30, 30))  # Fond gris foncé
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des pages
    if current_page == "home":
        current_page = draw_homepage(screen)
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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
