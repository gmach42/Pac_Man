# Risk analysis

| Risk | Impact | Mitigation |
|------|--------|------------|
| Packaging (PyInstaller + pygame + local wheel) breaks late | Cannot deliver on itch.io | Minimal packaging test on day 5, well before the release |
| Logic and rendering drift apart | Integration takes days | Shared contract agreed on day 1, daily 15-min sync, first integration on day 5 |
| Maze generator quirks (closed `42` cells, crash on tiny sizes, global RNG reseed) | Crash or unfair spawn during the defense | Wrapper with size clamping and `try/except`, tests on many sizes and seeds |
| Config changed during the defense | Crash or silent wrong values | Every key validated and clamped, faulty configs covered by tests |
| Ghost AI or collisions take longer than planned | Feature freeze slips | Simple BFS chase first, refined only if time allows; buffer on day 14 |
