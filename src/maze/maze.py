import pygame
from mazegenerator import MazeGenerator
from enum import IntFlag


class Border(IntFlag):
    EMPTY = 0
    NORTH = 0b0001
    EAST = 0b0010
    SOUTH = 0b0100
    WEST = 0b1000


class MazeError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(f"MazeError:\n{msg}")


class Maze:
    def __init__(self, width: int, height: int, seed: int, cell_size: int = 55, wall_width: int = 4):
        self.width = width
        self.height = height
        self.seed = seed
        self.cell_size = cell_size
        self.wall_width = wall_width
        
        self.perfect: bool = False
        self.center = (self.width // 2, self.height // 2)
        self.corners = [
            (0, 0), 
            (self.width - 1, 0), 
            (0, self.height - 1),
            (self.width - 1, self.height - 1)
        ]
        
        self.maze_generator = self.build_maze()
        self.grid = self.maze_generator.maze
        
        self.wallpaper = pygame.image.load('assets/wallpaper/wallpaper_game.png').convert()
        self.wall = pygame.image.load('assets/wall/wall.png').convert_alpha()
        self.closed_wall = pygame.image.load('assets/wall/closed.png').convert_alpha()

    def build_maze(self) -> MazeGenerator:
        try:
            maze = MazeGenerator(
                size=(self.width, self.height),
                seed=self.seed,
                perfect=self.perfect
            )
        except Exception as e:
            raise MazeError(
                "Une erreur est survenue lors de la création du labyrinthe de "
                f"{self.width=}, {self.height=}:\n{e}"
            )
        return maze

    def draw(self, screen):
        screen_width, screen_height = screen.get_size()

        img_width, img_height = self.wallpaper.get_size()
        scale = min(screen_width / img_width, screen_height / img_height)
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        scaled_wallpaper = pygame.transform.scale(self.wallpaper, (new_width, new_height))
        
        screen.blit(
            scaled_wallpaper,
            ((screen_width - new_width) // 2, (screen_height - new_height) // 2)
        )

        maze_total_width = self.width * self.cell_size
        maze_total_height = self.height * self.cell_size
        
        offset_x = (screen_width - maze_total_width) // 2
        offset_y = (screen_height - maze_total_height) // 2

        self.draw_maze_walls(screen, offset_x, offset_y)

    def draw_maze_walls(self, screen, offset_x, offset_y):
        for row in range(self.height):
            for col in range(self.width):
                cell_value = self.grid[row][col]
                y = row * self.cell_size + offset_y
                x = col * self.cell_size + offset_x

                if cell_value != (Border.NORTH | Border.SOUTH | Border.EAST | Border.WEST):
                    
                    if cell_value & Border.NORTH:
                        pygame.draw.rect(
                            screen, 
                            (200, 200, 200), 
                            (x, y, self.cell_size + self.wall_width, self.wall_width)
                        )

                    if cell_value & Border.SOUTH:
                        pygame.draw.rect(
                            screen, 
                            (200, 200, 200), 
                            (x, y + self.cell_size, self.cell_size + self.wall_width, self.wall_width)
                        )

                    if cell_value & Border.WEST:
                        pygame.draw.rect(
                            screen, 
                            (200, 200, 200), 
                            (x, y, self.wall_width, self.cell_size + self.wall_width)
                        )

                    if cell_value & Border.EAST:
                        pygame.draw.rect(
                            screen, 
                            (200, 200, 200), 
                            (x + self.cell_size, y, self.wall_width, self.cell_size + self.wall_width)
                        )
                
