.PHONY: all clear docker hooks local start

# The name of the service you're running
SERVICE     := omar
# The port used by the server (FastAPI)
PORT        := 8000
# Set the environment mode for the container (can be overridden with `make docker ENVIRONMENT=production`)
ENVIRONMENT ?= development

# 🛠️ Default target
all: local

# 🧘 Run the interactive CLI chat
local:
	@echo "[🕯️] Launching $(SERVICE), your spiritual guide... (local-development)"
	@uv run cli.py

# 🌐 Run the FastAPI server
start:
	@echo "[🤖] Starting $(SERVICE)'s server... (local-development)"
	@fastapi dev app/main.py

# 🐳 Run the Dockerized version of the app
docker:
	@echo "[🐳] Building and running $(SERVICE) in Docker...(local-development)"
	@docker build -t $(SERVICE)-image .
	@docker run --rm -it \
		-p $(PORT):$(PORT) \
		-e ENVIRONMENT=$(ENVIRONMENT) \
		$(SERVICE)-image

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
