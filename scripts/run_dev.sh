#!/usr/bin/env bash
# DiLS — Development server
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# Activate virtual environment if exists
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Load .env if exists
if [ -f ".env" ]; then
    set -a
    source .env
    set +a
fi

echo "Starting DiLS in development mode..."
echo "  Host: ${HOST:-127.0.0.1}:${PORT:-8000}"
echo "  Debug: ${DEBUG:-true}"
echo ""

exec uvicorn app.main:app \
    --host "${HOST:-127.0.0.1}" \
    --port "${PORT:-8000}" \
    --reload \
    --log-level info
