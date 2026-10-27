TARGETS := install run debug clean lint lint-strict

UNKNOWN_GOALS := $(filter-out $(TARGETS),$(MAKECMDGOALS))
ifneq ($(UNKNOWN_GOALS),)
$(error Unknown target(s): $(UNKNOWN_GOALS) -- valid: $(TARGETS))
endif

LINT_PATHS := src

# Colors:
RED = \033[31m
GREEN = \033[32m
BLUE = \033[34m
YELLOW = \033[33m
BOLD = \033[1m
RESET = \033[0m

install:
	uv sync

run:
	uv run python pac-man.py config.json

debug:
	uv run python -m pdb pac-man.py config.json

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -prune -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -prune -exec rm -rf {} + 2>/dev/null || true

lint:
	uv run flake8 $(LINT_PATHS)
	uv run mypy $(LINT_PATHS) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run flake8 $(LINT_PATHS)
	uv run mypy $(LINT_PATHS) --strict

.PHONY: $(TARGETS)
