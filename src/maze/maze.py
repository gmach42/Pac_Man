import pygame
from mazegenerator import MazeGenerator
from enum import IntFlag

# TO DO: Supprimer Rect et ajouter les colissions manuellement. 
# Supprimer rotate et modifier moi meme le png.
# Supprimer scale et modifier moi meme le png.


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
    def __init__(self, width: int, height: int, seed: int, cell_size: int = 55, wall_width: int = 12):
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
    
    def init_walls_rects(self):
        self.walls_rects.clear()
        pass

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
        
        wall = pygame.transform.scale(
            self.wall,
            (self.cell_size + self.wall_width, self.wall_width)
        )
        
        closed_wall = pygame.transform.scale(
            self.closed_wall,
            (self.cell_size, self.cell_size)
        )
        
        walls_rects = set()
        
        for row in range(self.height):
            for col in range(self.width):
                cell_value = self.grid[row][col]
                y = row * self.cell_size + offset_y
                x = col * self.cell_size + offset_x
                
                if cell_value == 15:
                    screen.blit(closed_wall, (x, y))
                    walls_rects.add((x, y, self.cell_size, self.cell_size))
                    continue

                if cell_value != (Border.NORTH | Border.SOUTH | Border.EAST | Border.WEST):
                    
                    if cell_value & Border.NORTH:
                        walls_rects.add((x, y, self.cell_size + self.wall_width, self.wall_width))
                        screen.blit(wall, (x, y))

                    if cell_value & Border.SOUTH:
                        walls_rects.add((x, y + self.cell_size, self.cell_size + self.wall_width, self.wall_width))
                        screen.blit(wall, (x, y + self.cell_size))
                        
                    if cell_value & Border.EAST:
                        rotated_wall = pygame.transform.rotate(wall, -90)
                        walls_rects.add((x + self.cell_size, y, self.wall_width, self.cell_size + self.wall_width))
                        screen.blit(rotated_wall, (x + self.cell_size, y))
                        
                    if cell_value & Border.WEST:
                        rotated_wall = pygame.transform.rotate(wall, 90)
                        walls_rects.add((x, y, self.wall_width, self.cell_size + self.wall_width))
                        screen.blit(rotated_wall, (x, y))
                        
        self.walls_rects = [pygame.Rect(r) for r in walls_rects]
                        
                
