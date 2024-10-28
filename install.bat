@echo off

:: Check if Python is installed
where python >nul
if errorlevel 1 (
    echo Python is not installed. Please install it before proceeding.
    exit /b
)

:: Check if PostgreSQL is installed
where psql >nul
if errorlevel 1 (
    echo PostgreSQL is not installed. Please install it before proceeding.
    exit /b
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Install requirements
echo Installing dependencies...
pip install -r requirements.txt

:: Run migrations
echo Running migrations...
python manage.py migrate

:: Create superuser
echo Creating superuser. Please provide the details when prompted.
python manage.py createsuperuser

:: Start the development server
echo Starting the server...
python manage.py runserver

echo Installation complete! You can access the app at http://127.0.0.1:8000/
pause
