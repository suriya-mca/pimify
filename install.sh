#!/bin/bash

# Check for Python and pip installation
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install it before proceeding."
    exit 1
fi

if ! command -v pip3 &>/dev/null; then
    echo "pip3 is not installed. Please install it before proceeding."
    exit 1
fi

# Check for PostgreSQL installation
if ! command -v psql &>/dev/null; then
    echo "PostgreSQL is not installed. Please install it before proceeding."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create a superuser
echo "Creating superuser. Please provide the details when prompted."
python manage.py createsuperuser

# Start the development server
echo "Starting the server..."
python manage.py runserver

echo "Installation complete! You can access the app at http://127.0.0.1:8000/"

# End of script
