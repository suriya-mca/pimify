# Import necessary modules
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from djmoney.contrib.exchange.backends import OpenExchangeRatesBackend

# Function to update exchange rates
def sycn_exchange_rates():
    try:
        backend = OpenExchangeRatesBackend()  # Initialize the exchange rates backend
        backend.update_rates()  # Update rates from OpenExchangeRates
        print("Exchange rates updated successfully.")
    except Exception as e:
        print(f"Failed to update exchange rates: {e}")

# Function to delete old job executions
@util.close_old_connections  # Ensures database connections are closed properly
def delete_old_job_executions(max_age=7):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)  # Delete jobs older than 'max_age' days

# Function to start the scheduler
def start():
    scheduler = BackgroundScheduler()  # Create a background scheduler
    scheduler.add_jobstore(DjangoJobStore(), "default")  # Use Django's database as the job store

    # Add a job to update exchange rates every hour
    scheduler.add_job(
        sycn_exchange_rates,
        'interval',
        hours=1,
        jobstore='default',
        id="update_exchange_rates",
        replace_existing=True,
    )

    # Add a job to delete old job executions every 7 days
    scheduler.add_job(
        delete_old_job_executions,
        'interval',
        days=7,
        jobstore='default',
        id="delete_old_job_executions",
        replace_existing=True,
    )

    try:
        scheduler.start()  # Start the scheduler
    except KeyboardInterrupt:
        scheduler.shutdown()  # Gracefully shut down the scheduler
