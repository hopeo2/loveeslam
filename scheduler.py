from apscheduler.schedulers.background import BackgroundScheduler

def func1():
    # Function 1 logic here
    print("Function 1 executed")

def func2():
    # Function 2 logic here
    print("Function 2 executed")

def func3():
    # Function 3 logic here
    print("Function 3 executed")

# Create a scheduler
scheduler = BackgroundScheduler()

# Add each function as a job to be executed every second
scheduler.add_job(func1, 'interval', seconds=1)
scheduler.add_job(func2, 'interval', seconds=1)
scheduler.add_job(func3, 'interval', seconds=1)

# Start the scheduler
scheduler.start()

# Keep the main thread alive
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # Gracefully shut down the scheduler
    scheduler.shutdown()
