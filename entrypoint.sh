#!/bin/sh
set -euo pipefail

echo "[🌍] Environment: ${ENVIRONMENT:-undefined}"

start_app() {
  local mode_message="$1"
  shift  # Remove the mode message from args

  echo "[🚀] $mode_message"
  echo "[⚙️] Launching FastAPI with: uv run fastapi run app/main.py $*"

  exec uv run fastapi run app/main.py "$@"
}

case "${ENVIRONMENT:-}" in
  development)
    start_app "Booting up in development mode..." \
      --workers 2
    ;;

  production)
    start_app "Liftoff! Entering production orbit..." \
      --workers 4 --proxy-headers
    ;;

  *)
    echo "[❌] Invalid ENVIRONMENT: '${ENVIRONMENT:-}'"
    echo "[ℹ️] Please set ENVIRONMENT to either 'development' or 'production'"
    exit 1
    ;;
esac
