import logging
import os
from datetime import datetime

# ✅ Step 1: Create a logs directory (not including log file in the folder name!)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# ✅ Step 2: Generate a log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# ✅ Step 3: Set up logging to that file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ✅ Step 4: Log a test message
if __name__ == "__main__":
    logging.info("✅ Logging has started.")
    print(f"📁 Log file created at: {LOG_FILE_PATH}")
