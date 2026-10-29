import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.text_color = (255, 255, 255)
        self.menu_font = pygame.font.Font("assets/fonts/menu_font.otf", 55)
        self.options = ["PLAY", "OPTIONS", "EXIT", "INSTRUCTIONS", "HIGHSCORES"]

        self.wallpaper = pygame.image.load('assets/wallpaper/wallpaper_menu.png').convert()
        self.wallpaper = pygame.transform.scale(self.wallpaper, (self.width, self.height))
    
    def draw(self):
        self.screen.blit(self.wallpaper, (0, 0))
        for i, option in enumerate(self.options):
            option_surface = self.menu_font.render(option, True, self.text_color)
            option_rect = option_surface.get_rect(center=(self.width // 2, self.height // 2 + i * 70))
            self.screen.blit(option_surface, option_rect)
    