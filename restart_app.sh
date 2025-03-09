#!/bin/bash

APP_NAME="app.py"
APP_DIR="$HOME/resume_app"
VENV_PATH="$APP_DIR/venv"
LOG_FILE="$APP_DIR/app.log"

echo "🔍 Checking for running instances of $APP_NAME..."
PID=$(pgrep -f "$APP_NAME")

if [ -n "$PID" ]; then
    echo "❌ Stopping existing instance (PID: $PID)..."
    kill -9 $PID
else
    echo "✅ No running instance found."
fi

# Check if virtual environment exists, create if missing
if [ ! -d "$VENV_PATH" ]; then
    echo "⚡ Virtual environment not found. Creating one..."
    python3 -m venv "$VENV_PATH"
    echo "✅ Virtual environment created!"
fi

# Activate virtual environment
echo "🐍 Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# Upgrade pip and install dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r "$APP_DIR/requirements.txt"

echo "🚀 Starting $APP_NAME..."
nohup python3 "$APP_DIR/$APP_NAME" > "$LOG_FILE" 2>&1 &

echo "✅ $APP_NAME started successfully! Check '$LOG_FILE' for output."
