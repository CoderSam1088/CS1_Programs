import schedule
import time


def job():
    print("I'm working...")


def runjob(func, arg1):
    schedule.every().day.at("14:00").do(func, number=arg1)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    runjob(job)
    
