#!/bin/bash

# Check for Python and pip installation
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install it before proceeding."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv env

# Activate virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Create the 'data' and 'media' directory
echo "Creating data, backup and media directory"
mkdir data
mkdir backups
mkdir media
chmod +x data
chmod +x backup
chmod +x media

# Run migrations
echo "Running migrations..."
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate

# Collect static
echo "Collect statis files..."
python manage.py collectstatic

# Start the scheduler
echo "Starting scheduler..."
python manage.py scheduler

# Create Superuser
echo "Creating superuser..."
python manage.py createsuperuser

# Start the development server
echo "Starting the server..."
gunicorn core.wsgi:application -c script/gunicorn/gunicorn.conf.py
