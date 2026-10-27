# Usage
	Must run with "python3 pac-man.py config.json"
	-> must take exactly 1 arg
	-> Any error (missing file, invalid value, missing key) must be handled

# Config file
	- in json
	- must handle comments (startwith # lines must be ignored)
	- Suggested keys:
		highscore_filename, level, width, height, lives:3, pacgum:42, points_per_pacgum:10, points_per_super_pacgum:50. points_per_ghost:200, seed:42, level_max_time:90

## Faulty config
	--> clamp to safe defaults + log a clear message then continue
	- Unknown keys must be ignored

# Maze gen
	no modif allowed
	PERFECT will be set to False

# Highscore system
	- documented in the README.md
	- Handle platers names (max 10 chars, alphanumeric and spaces only)
	- Handle scores (int >= 0)
	- 10 highscores kept (with name and score)
	- Load HS at game start and save at game end
	- Player can enter their name when they end game (W or L)
	- HS in main menu

# Game Specs

## Level Struct
	-> first level is from a fixed seed (e.g. 42) then the rest is randomly generated
	- pacgums + super-pacgums in the corners
	- 4 ghost and player start in the middle

## Player
	- Can move through corridors only (collision)
	- 4 dir using WASD or arrow keys
	- 3 lives
	- lose a life when touching ghost
	- respawn in middle
	- game over when no life left
	- win level when all pacgums eaten
	- win game when all level won
	- when eating super-gum, ghost can be eaten
	- X, Y, Z points for pacgum, super-pacgum, ghost respectively

## Ghosts
	- Move autonomously
	- Chase the player
	- Run away when edible
	- Respawn in corner (after 5 - 10 second for example)

## Pacgums & Super-pacgums
	- pacgums = small dots
	- super-pacgums = bigger dots in corners

## Cheat mode
	- can be activated for peer view
	- suggested features:
		invincibility
		level skip
		ghost freeze
		extra lives
		increased speed
	-> Cheat mode is for testing purposes so it must help the reviewer

## Scoring
	eating pacgum=X, super-pacgum=Y, ghost=Z
	do not decrease

## Game Progression
	- multiple level (>= 10)
	- time limit for each level (eg 90)
	- if limit reached you decide what happens (restart level, lose game)
	- when a level is completed, player moves to the next one
	- player score and lives are kept between levels
	- game end when all level done or no lifes left
	- player can pause and resume game
	- game end (W or L) -> score displayed + player can enter name
	- after end, player is returned to the main menu

## User Interface
	- Main Menu
		Start Game
		View Highscores
		Instructions
		Exit
	- In-Game HUD
		Current score
		Remaining lives
		Current level
		Remaining time for the level
	- Pause Menu
		Resume the game
		Return to the main menu
	- Game Over Screen
		Displays the final score
		Prompts the player to enter their name
	- Victory Screen:
		Displays the final score and congrats message
		Prompts the player to enter their name

# Project packaging
	Must be installed and launched from a public platform (Steam or Itch.io) as a free unlisted/private build.
	Provide minimal instructions (controls, options, config)
	git repo must contain source and packaging script/spec at root

# Project Management
	Structured approach to drive the project and provide evidence
	Must produce various documents that prove your approach
	dedicated subdir for this
	Examples:
		- timeline, Gantt, Kanban
		- Progress tracking compared to the timeline
		- Project analysis and choices
		- Risk analysis
		- Organization of the team
		- Acceptance test plan
		- Summary of problems encountered

# README
	additionals sections:
	- Configuration
	- Highscore
	- Maze Generation
	- Implementation
	- General Software Architecture
	- Project Management

#TODO
	class Direction(Enum):       # N/E/S/W avec dx, dy et le bit de mur associé
	class GhostState(Enum):      # CHASE, FRIGHTENED, EATEN
	class Maze:                  # width, height, has_wall(x, y, d), is_open(x, y), center, corners
	class Player / Ghost:        # pos (case), direction, progress entre deux cases (0..1), state
	class Level:                 # maze, player, ghosts, pacgums: set[pos], super_pacgums, time_left
	class GameSession:           # score, lives, level_number, cheats, current_level, is_over, won
