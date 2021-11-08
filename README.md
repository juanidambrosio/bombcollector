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
CHECK_ERRORS_FREQUENCY_SECONDS=30
REFRESH_BROWSER_COOLDOWN_MINUTES=5
```

- `HEROES_TO_WORK_FREQUENCY_MINUTES`: Frequency to quit the map and get up the workers
- `NEW_MAP_CHECK_FREQUENCY_SECONDS`: Frequency to check for new map button to avoid getting stuck in that screen
- `CHECK_ERRORS_FREQUENCY_SECONDS`: Frequency to check for possible in-game errors. It refreshes the browser and connects the wallet again
- `REFRESH_BROWSER_COOLDOWN_MINUTES`: Frequency to wait every time you retry to restart the game because of an in-game error. This is to prevent infinite processing while server doesn't respond

2. Take a screenshot of every image stores in `images` folder
