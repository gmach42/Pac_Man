import pygame
import src.ui.menu as menu

class Renderer:
    def __init__(self, maze_generator):
        pygame.init()

        self.width = 1920
        self.height = 1080

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )
        pygame.display.set_caption("PacMan")

        self.clock = pygame.time.Clock()

        self.maze = maze_generator.maze
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])

        self.cell_size = min(
            self.width // self.cols,
            self.height // self.rows
        )

        self.offset_x = (
            self.width - self.cols * self.cell_size
        ) // 2
        self.offset_y = (
            self.height - self.rows * self.cell_size
        ) // 2

        self.background_color = (0, 0, 0)
        self.wall_color = (30, 100, 255)

        self.wall_width = 10

    def draw_wall(self, x1, y1, x2, y2):
        pygame.draw.line(
            self.screen,
            self.wall_color,
            (x1, y1),
            (x2, y2),
            self.wall_width
        )

    def draw_maze(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                left = self.offset_x + x * self.cell_size
                top = self.offset_y + y * self.cell_size

                right = left + self.cell_size
                bottom = top + self.cell_size
                
                if cell == 15:
                    pygame.draw.rect(
                        self.screen,
                        self.wall_color,
                        (left, top, self.cell_size, self.cell_size)
                    )

                if cell & 1:
                    self.draw_wall(left, top, right, top)

                if cell & 2:
                    self.draw_wall(right, top, right, bottom)

                if cell & 4:
                    self.draw_wall(left, bottom, right, bottom)

                if cell & 8:
                    self.draw_wall(left, top, left, bottom)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.background_color)

            self.menu = menu.Menu(self.screen)
            self.screen.blit(self.menu.wallpaper_menu, (0, 0))
            self.menu.draw()
            # self.draw_maze()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

