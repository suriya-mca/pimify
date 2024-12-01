@echo off

:: Check if Python is installed
where python >nul
if errorlevel 1 (
    echo Python is not installed. Please install it before proceeding.
    exit /b
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv env

:: Activate virtual environment
echo Activating virtual environment...
call env\Scripts\activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

:: Install requirements
echo Installing dependencies...
pip install -r requirements.txt

:: Run migrations
echo Running migrations...
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate

:: Collect static
echo Collect statis files...
python manage.py collectstatic

echo "Superuser created with username 'admin' and password 'admin123'"
echo "**IMPORTANT:** Change the password immediately after logging in for the first time."

:: Start the development server
echo Starting the server...
python manage.py runserver
