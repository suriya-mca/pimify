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

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv env

# Activate virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate

# Collect static
echo "Collect statis files..."
python manage.py collectstatic

echo "Superuser created with username 'admin' and password 'admin123'"
echo "**IMPORTANT:** Change the password immediately after logging in for the first time."

# Start the development server
echo "Starting the server..."
gunicorn core.wsgi:application -c script/gunicorn/gunicorn.conf.py
