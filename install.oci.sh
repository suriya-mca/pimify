#! OCI shell

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing dependencies..."
pip install --no-cache-dir -r requirements.txt

# Create necessary directories
echo "Ensuring necessary directories exist..."
mkdir -p data backups media

# Run migrations
echo "Running migrations..."
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate

# Collect static
echo "Collect statis files..."
python manage.py collectstatic --noinput

# Start the scheduler
echo "Starting scheduler..."
python manage.py scheduler

# Cleanup
echo "Cleaning up..."
rm -rf /root/.cache/pip /var/cache/apk/*

# Start the development server
echo "Starting the server..."
gunicorn core.wsgi:application -c script/gunicorn/gunicorn.conf.py