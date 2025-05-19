import pygame

class Button:
    def __init__(self, x, y, width, height, text, action, font=None, color=(0, 255, 0), active=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = font or pygame.font.SysFont("Arial", int(height * 0.6))
        self.color = color
        self.active = active

    def draw(self, screen):
        if self.active == True :
            color = (0, 200, 0) if self.rect.collidepoint(pygame.mouse.get_pos()) else (0, 255, 0)
            pygame.draw.rect(screen, color, self.rect,border_radius=8)
            #pygame.draw.rect(screen, (0, 0, 0), self.rect, border_radius=8)
            text_surf = self.font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))
        else :
            color = (150, 150, 150) if self.rect.collidepoint(pygame.mouse.get_pos()) else (150, 200, 150)
            pygame.draw.rect(screen, color, self.rect,border_radius=8)
            #pygame.draw.rect(screen, (0, 0, 0), self.rect, border_radius=8)
            text_surf = self.font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))


    def handle_event(self, event):
        if self.active and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return self.action
        return None


class InputBox:
    def __init__(self, x, y, width, height, text='', font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = (255, 255, 255)  # Gris
        self.color_active = (200, 200, 200)  # Blanc
        self.color = self.color_inactive
        self.text = text
        self.font = font or pygame.font.SysFont("Arial", int(height * 0.6))
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
    def __init__(self, x, y, width, height, text, color = (255, 255, 255), font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.visibility = True
        self.color = color
        self.font = font or pygame.font.SysFont("Arial", int(height * 0.6))
    def draw(self, screen):
        if self.visibility == True :
            color = self.color
            if color == (255,255,255):
                pygame.draw.rect(screen, color, self.rect)
                pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
                text_surf = self.font.render(self.text, True, (0, 0, 0))
                screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))
            elif color == (0, 0, 0):
                pygame.draw.rect(screen, color, self.rect)
                pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
                text_surf = self.font.render(self.text, True, (255, 255, 255))
                screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))
            else :                
                text_surf = self.font.render(self.text, True, (255, 255, 255))
                screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))

class Label:
    def __init__(self, x, y, width, height, text, font=None, bg_color=(200, 200, 200), text_color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font or pygame.font.SysFont("Arial", int(height * 0.6))
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=8)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class TimelineBox:
    def __init__(self, x, y, width, height, text, active=False, font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.active = active
        self.font = font or pygame.font.SysFont("Arial", int(height * 0.4))

    def draw(self, screen):
        color = (0, 255, 0) if self.active else (255, 255, 255) if self.text is None else (255, 255, 255)
        pygame.draw.rect(screen, color, self.rect, border_radius=4)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        label = self.font.render(self.text if self.text is not None else "None", True, (0, 0, 0))
        label_rect = label.get_rect(center=self.rect.center)
        screen.blit(label, label_rect)



