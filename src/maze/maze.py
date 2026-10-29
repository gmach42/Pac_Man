import pygame
from mazegenerator import MazeGenerator
from enum import IntFlag


class Border(IntFlag):
    """Represents the borders of a maze cell."""
    EMPTY = 0
    NORTH = 0b0001  # NORTH = 1
    EAST = 0b0010  # EAST = 2
    SOUTH = 0b0100  # SOUTH = 4
    WEST = 0b1000  # WEST = 8


class MazeError(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(f"MazeError:\n{msg}")


class Maze:

    def __init__(self, width: int, height: int, seed: int):
        self.width = width
        self.height = height
        self.seed = seed
        self.perfect: bool = False
        self.center = (self.width // 2, self.height // 2)
        self.corners = [(0, 0), (self.width - 1, 0), (0, self.height - 1),
                        (self.width - 1, self.height - 1)]
        self.maze_generator = self.build_maze()
        self.grid = self.maze_generator.maze
        
        self.wallpaper = pygame.image.load('assets/wallpaper/wallpaper_game.png').convert()
        
        self.wall = pygame.image.load('assets/wall/wall.png').convert_alpha()
        self.closed_wall = pygame.image.load('assets/wall/closed.png').convert_alpha()

    def build_maze(self) -> MazeGenerator:
        try:
            maze = MazeGenerator(size=(self.width, self.height),
                                 seed=self.seed,
                                 perfect=self.perfect)
        except Exception as e:
            raise MazeError(
                "An error happened while trying to create a maze of "
                f"{self.width=}, {self.height=}:\n{e}")
        return maze

    def draw(self, screen):
        screen_width, screen_height = screen.get_size()

        img_width, img_height = self.wallpaper.get_size()
        scale = min(
            screen_width / img_width,
            screen_height / img_height
        )

        new_width = int(img_width * scale)
        new_height = int(img_height * scale)

        scaled_wallpaper = pygame.transform.scale(
            self.wallpaper, (new_width, new_height)
        )

        screen.blit(
            scaled_wallpaper,
            (
                (screen_width - new_width) // 2,
                (screen_height - new_height) // 2
            )
        )

        rows = len(self.grid)
        cols = len(self.grid[0])

        cell_size = min(
            screen_width // cols,
            screen_height // rows
        )

        offset_x = (screen_width - cols * cell_size) // 2
        offset_y = (screen_height - rows * cell_size) // 2

        block_size = cell_size // 3

        wall = pygame.transform.scale(
            self.wall, (block_size, block_size)
        )

        closed_wall = pygame.transform.scale(
            self.closed_wall, (cell_size, cell_size)
        )

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                left = offset_x + x * cell_size
                top = offset_y + y * cell_size
                right = left + cell_size

                if cell == 15:
                    screen.blit(closed_wall, (left, top))
                    continue

                north = bool(cell & Border.NORTH)
                west = bool(cell & Border.WEST)
                east = bool(cell & Border.EAST)
                south = bool(cell & Border.SOUTH)

                if north and west:
                    for i in range(3):
                        screen.blit(
                            wall,
                            (left + i * block_size, top)
                        )
                    for i in range(3):
                        screen.blit(
                            wall,
                            (left, top + i * block_size)
                        )
                        
                elif north and not west:
                    for i in range(3):
                        screen.blit(
                            wall,
                            (left + i * block_size, top)
                        )
                
                elif west and not north:
                    for i in range(3):
                        screen.blit(
                            wall,
                            (left, top + i * block_size)
                        )
                    

                if x == cols - 1 and east:
                    for i in range(3):
                        screen.blit(
                            wall,
                            (
                                right - block_size,
                                top + i * block_size
                            )
                        )

                if y == rows - 1 and south:
                    for i in range(3):
                        screen.blit(
                            wall,
                            (
                                left + i * block_size,
                                top + cell_size - block_size
                            )
                        )
                
