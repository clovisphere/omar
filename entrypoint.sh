#!/bin/bash
set -euo pipefail

echo "Current ENVIRONMENT: ${ENVIRONMENT:-undefined}"

start_app() {
  echo "$1" # Keep this line for logging the startup mode
  shift # Remove the first argument so uvicorn doesn't see it
  exec uvicorn app.main:app "$@" # Pass all remaining arguments to uvicorn
}

case "${ENVIRONMENT:-}" in
  development)
    start_app "Starting in development mode with hot reload..." \
      --host 0.0.0.0 --port 8000 --reload
    ;;

  production)
    start_app "Starting in production mode with multiple workers..." \
      --host 0.0.0.0 --port 8000 --timeout-keep-alive 300 --workers 2
    ;;

  *)
    echo "Error: ENVIRONMENT must be set to either 'development' or 'production'"
    exit 1
    ;;
esac
