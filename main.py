import time
import os
import schedule
from dotenv import load_dotenv
from work import putHeroesToWork
from map import checkNewMap
from errors import checkNewErrors

load_dotenv()

schedule.every(int(os.getenv("HEROES_TO_WORK_FREQUENCY_MINUTES"))
               ).minutes.do(putHeroesToWork)
# schedule.every(int(os.getenv("NEW_MAP_CHECK_FREQUENCY_SECONDS"))
#                ).seconds.do(checkNewMap)
schedule.every(int(os.getenv("CHECK_ERRORS_FREQUENCY_SECONDS"))
               ).seconds.do(checkNewErrors)

while True:
    schedule.run_pending()
    time.sleep(1)
