import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.background_color = (0, 0, 0)
        self.text_color = (255, 255, 255)

        self.title_font = pygame.font.Font(None, 100)
        self.menu_font = pygame.font.Font(None, 50)
    
        self.options = ["PLAY", "OPTIONS", "EXIT", "INSTRUCTIONS", "HIGHSCORES"]

        self.wallpaper_menu = pygame.image.load(
                'assets/wallpaper_menu.png'
        ).convert()
        self.wallpaper_menu = pygame.transform.scale(
                self.wallpaper_menu, (self.width, self.height)
            )
    
    def draw(self):
        for i, option in enumerate(self.options):
            option_surface = self.menu_font.render(option, True, self.text_color)
            option_rect = option_surface.get_rect(center=(self.width // 2, self.height // 2 + i * 60))
            self.screen.blit(option_surface, option_rect)
