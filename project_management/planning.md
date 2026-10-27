# Planning

Total duration: **14 days**. Days 1–10 cover development and release; days 11–14 cover tests and defense preparation.

Owners:
- **gmach**: game logic, config, maze, highscores, packaging
- **lucpelle**: pygame rendering, screens, assets
- **both**: shared work

## Phase 1 — Foundations (days 1–3)

| Day | Task | Owner | Duration |
|-----|------|-------|----------|
| 1 | Tooling setup (Makefile, flake8, mypy, pytest, .gitignore) | gmach | 2 h |
| 1 | Shared contract: types and class signatures between logic and rendering | gmach | 3 h |
| 1 | Review of the shared contract | both | 1 h |
| 1–2 | pygame backend limited to MLX-equivalent functions | lucpelle | 6 h |
| 2 | Config parser (comments, defaults, clamping) and tests | gmach | 6 h |
| 2 | Entry point (argument check, clean error messages) | gmach | 1.5 h |
| 2 | Drawing primitives rebuilt on the backend (rect, circle, line) | lucpelle | 3 h |
| 3 | Maze wrapper around the A-Maze-ing package and tests | gmach | 4 h |
| 3 | Scene state machine (menu, game, pause, end, name entry) | gmach | 3 h |
| 3 | Keyboard mapping (arrows / WASD → commands) | lucpelle | 2 h |
| 3 | Maze rendering | lucpelle | 4 h |

## Phase 2 — Gameplay (days 4–9)

| Day | Task | Owner | Duration |
|-----|------|-------|----------|
| 4 | Level: pacgums, super-pacgums, player movement, level win | gmach | 8 h |
| 4–5 | Sprites and assets (player, ghosts, pacgums) | lucpelle | 8 h |
| 5 | Packaging test (minimal build uploaded to itch.io) | gmach | 3 h |
| 5 | Collisions, lives, respawn, power mode | gmach | 5 h |
| 5 | Entity rendering with smooth movement | lucpelle | 4 h |
| 5 | First integration: player moving in the maze | both | 2 h |
| 6 | Ghost AI (chase, flee, respawn in corner) | gmach | 6 h |
| 6 | Cheat mode | gmach | 2 h |
| 6 | Text rendering (font) | lucpelle | 3 h |
| 6 | In-game HUD (score, lives, level, time left) | lucpelle | 3 h |
| 7 | Game session (levels, timer, pause, game over, victory) | gmach | 5 h |
| 7 | Main menu, highscores and instructions screens | lucpelle | 5 h |
| 7–8 | Highscore system and tests | gmach | 6 h |
| 8 | Pause, game over and victory screens, name entry | lucpelle | 5 h |
| 9 | Full integration of logic and rendering | both | 4 h |
| 9 | Lint and mypy strict pass | both | 2 h |
| 9 | Visual polish | lucpelle | 4 h |

## Phase 3 — Release (day 10)

| Day | Task | Owner | Duration |
|-----|------|-------|----------|
| 10 | Final packaging and itch.io upload, tested on a clean machine | gmach | 4 h |
| 10 | In-package instructions (controls, options, configuration) | lucpelle | 1 h |
| 10 | README (all required sections, in English) | both | 4 h |

## Phase 4 — Tests and defense (days 11–14)

| Day | Task | Owner | Duration |
|-----|------|-------|----------|
| 11–12 | Acceptance tests on the packaged build, bug fixes | both | 2 days |
| 13 | Project management docs (progress, team, decisions, test results) | both | 3 h |
| 13–14 | Defense prep: each member explains the other's code, recode practice | both | 1 day |
| 14 | Buffer for late fixes | both | – |

## Milestones

| Day | Milestone |
|-----|-----------|
| 1 | Shared contract agreed |
| 5 | Player moves in the generated maze |
| 9 | Full game loop works: menu → levels → win/lose → name entry → menu |
| 10 | Game available on itch.io |
| 14 | Ready for the defense |
