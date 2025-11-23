#!/bin/bash

set -e

echo "Starting the application..."
echo "Environment: ${ENV:-development}"

# Add your application startup commands here
uvicorn ../src.main:app --reload
echo "Application started successfully!" 