.PHONY: all clear hooks local server

# The name of the service you're running
SERVICE := Omar
# The port used by the server (FastAPI)
PORT    :=  8000

# 🛠️ Default target
all: local

# 🧘 Run the interactive CLI chat
local:
	@echo "[🕯️] Launching $(SERVICE), your spiritual guide..."
	@uv run cli.py

# 🌐 Run the FastAPI server
server:
	@echo "[🤖] Starting $(SERVICE)'s server..."
	@fastapi dev app/main.py

# ✅ Run all pre-commit hooks
hooks:
	@echo "[🧼] Running pre-commit hooks..."
	@pre-commit run --all-files

# 🔥 Clean up Python and tooling caches
clear:
	@echo "[🧹] Removing cache and compiled files..."
	@find . \
		\( -name ".mypy_cache" \
		-o -name ".pytest_cache" \
		-o -name "__pycache__" \
		-o -name "*.pyc" \
		-o -name "*.pyo" \) \
		-exec rm -rf {} +
