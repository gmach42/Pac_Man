import pygame
from src.engine.engine import Engine
from src.maze.maze import Maze
from src.ui.menu import Menu


def main():
    engine = Engine(width=1920, height=1080, title="PacMan")
    menu = Menu(engine.screen)
    maze = Maze(width=20, height=15, seed=42)
    
    game_state = 'MENU'
    
    while engine.running:
        events = engine.get_events()
        
        for event in events:
            if event.type == pygame.QUIT:
                engine.running = False
                
            elif event.type == pygame.KEYDOWN:
                if game_state == 'MENU':
                    if event.key == pygame.K_RETURN:
                        game_state = 'GAME'
                    elif event.key == pygame.K_ESCAPE:
                        engine.running = False
                        
                elif game_state == 'GAME':
                    if event.key == pygame.K_ESCAPE:
                        game_state = 'MENU'
                
        
        if game_state == 'MENU':
            menu.draw()
        elif game_state == 'GAME':
            maze.draw(engine.screen)
            
        engine.tick(60)
        
    engine.quit()

    
if __name__ == "__main__":
    main()