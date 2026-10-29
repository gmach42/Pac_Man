import pygame

class Engine:
    def __init__(self, width: int, height: int, title: str):
        pygame.init()
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        
        self.clock = pygame.time.Clock()
        self.running = True

    def get_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        return events

    def tick(self, fps: int = 60):
        pygame.display.flip()
        self.clock.tick(fps)

    def quit(self):
        pygame.quit()