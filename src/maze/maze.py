from mazegenerator import MazeGenerator

w = 10
h = 10
gen = MazeGenerator(size=(w, h), perfect=False, seed=42)
grid: list[list[int]] = gen.maze
print(grid)
