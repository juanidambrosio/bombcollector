# Bombcollector

## Installation

```
pip install pillow
pip install pyautogui
pip install python-dotenv
pip install schedule
```

## Setup

1. Create file `.env` with the following variables:

```
HEROES_TO_WORK_FREQUENCY_MINUTES=10
NEW_MAP_CHECK_FREQUENCY_SECONDS=30
```

HEROES_TO_WORK_FREQUENCY_MINUTES: It gives the frequency to quit the map and get up the workers
NEW_MAP_CHECK_FREQUENCY_SECONDS: It gives the frequency to check for new map button to avoid getting stuck in that screen

2. Take a screenshot of every image stores in `images` folder
