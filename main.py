import schedule
import time
import os
from dotenv import load_dotenv
from work import putHeroesToWork

load_dotenv()

def job():
    putHeroesToWork()

schedule.every(int(os.getenv("HEROES_TO_WORK_FREQUENCY"))).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)