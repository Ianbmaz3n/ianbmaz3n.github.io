import pygame
import sys
# Initialize PyGame
pygame.init()
# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THE OREGON TRAIL: PREPARE FOR DYSENTERY EDITION")
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)
# Button class
class Button:
    def __init__(self, text, pos, icon=None):
        self.text = text
        self.pos = pos
        self.icon = icon
        self.rect = pygame.Rect(pos[0], pos[1], 300, 50)
        self.color = GRAY
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.icon:
            screen.blit(self.icon, (self.rect.x + 5, self.rect.y + 5))
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 60, self.rect.y + 10))
        for i in range(5):  # Drawing star ratings
            pygame.draw.star(screen, BLACK, (self.rect.x + 250 + i * 20, self.rect.y + 15))
    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    def on_click(self):
        print(f"{self.text} button clicked")
# Load icons (Placeholder, as we don't have actual icons)
icon_placeholder = pygame.Surface((40, 40))
icon_placeholder.fill(DARK_GRAY)
# Create buttons
buttons = [
    Button("Travel the Trail", (250, 100), icon_placeholder),
    Button("Learn About the Trail", (250, 170), icon_placeholder),
    Button("See the Oregon Top Ten", (250, 240), icon_placeholder),
    Button("Turn Sound Off", (250, 310), icon_placeholder),
    Button("Choose Management Options", (250, 380), icon_placeholder),
    Button("End", (250, 450), icon_placeholder)
]
# Main loop
running = True
while running:
    screen.fill(WHITE)
    title_surface = font.render("THE OREGON TRAIL: PREPARE FOR DYSENTERY EDITION", True, BLACK)
    screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 20))
    for button in buttons:
        button.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.is_hovered(mouse_pos):
                    button.on_click()
    pygame.display.flip()
pygame.quit()
sys.exit()