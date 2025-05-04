# update.py
from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"Updated at {datetime.now()}\n")
