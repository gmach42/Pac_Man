from src.maze.maze import Maze
from src.render.render import Renderer


def main():
    maze = Maze(width=20, height=15, seed=42)
    maze_generator = maze.build_maze()
    
    renderer = Renderer(maze_generator)
    renderer.run()
    
if __name__ == "__main__":
    main()