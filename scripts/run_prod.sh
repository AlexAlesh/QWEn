#!/usr/bin/env bash
# DiLS — Production server (Linux)
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# Activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Load .env
if [ -f ".env" ]; then
    set -a
    source .env
    set +a
fi

# Ensure logs and backups dirs exist
mkdir -p logs backups

WORKERS="${WORKERS:-4}"
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"

echo "Starting DiLS in production mode..."
echo "  Host: ${HOST}:${PORT}"
echo "  Workers: ${WORKERS}"
echo ""

exec gunicorn app.main:app \
    --workers "$WORKERS" \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind "${HOST}:${PORT}" \
    --access-logfile logs/access.log \
    --error-logfile logs/error.log \
    --log-level info \
    --timeout 120
