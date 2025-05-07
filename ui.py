import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)

        self.visibility = True
    def draw(self, screen):
        if self.visibility == True :
            color = (0, 200, 0) if self.rect.collidepoint(pygame.mouse.get_pos()) else (0, 255, 0)
            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            text_surf = self.font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return self.action
        return None


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = (255, 255, 255)  # Gris
        self.color_active = (200, 200, 200)  # Blanc
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.Font(None, 36)  # Augmenter la taille de la police
        self.txt_surface = self.font.render(self.text, True, (0, 0, 0))
        self.active = False
        self.visibility = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Active la boîte si elle est cliquée
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change la couleur en fonction de l'état
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"Input: {self.text}")
                    self.active = False
                    self.color = self.color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Met à jour le texte affiché
                self.txt_surface = self.font.render(self.text, True, (0, 0, 0))

    def draw(self, screen):
        if self.visibility == True :
            # Dessine la boîte
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  # Bordure noire
            # Dessine le texte centré verticalement
            text_rect = self.txt_surface.get_rect(center=self.rect.center)
            screen.blit(self.txt_surface, text_rect)

class Text:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.visibility = True
    def draw(self, screen):
        if self.visibility == True :
            color = (255,255,255)
            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            text_surf = self.font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))


