import time
import os
from logger import getLogger
from dotenv import load_dotenv
from work import putHeroesToWork
from map import backToMap, checkNewMap

load_dotenv()
logger = getLogger()

while True:
    # checkForErrors()
    checkNewMap()
    putHeroesToWork()
    backToMap()
    logger.info("Completed enabling workers")
    time.sleep(int(os.getenv("HEROES_TO_WORK_FREQUENCY_MINUTES")) * 60)
