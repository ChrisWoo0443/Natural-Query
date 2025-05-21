#!/bin/bash
BACKEND_PATH=$(pwd)/backend
if [[ ":$PYTHONPATH:" != *":$BACKEND_PATH:"* ]]; then
    export PYTHONPATH="$PYTHONPATH:$BACKEND_PATH"
fi

echo "Starting backend..."
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
fastapi run backend/main.py &
BACKEND_PID=$!

# Start the frontend
echo "Starting frontend..."
cd frontend
python3 -m http.server 8001
FRONTEND_PID=$!
cd ..

# Wait for user to terminate
echo "Frontend and backend are running. Press Ctrl+C to stop."
trap "kill $BACKEND_PID $FRONTEND_PID" SIGINT
wait