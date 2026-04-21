from loguru import logger
import os

# ensure logs folder exists or it might be a problem later
os.makedirs("logs", exist_ok=True)

# configuring logger
logger.add(
    "logs/app.log",
    rotation="1 MB", 
    level="INFO",
    format="{time} | {level} | {message}"
)

def get_logger():
    return logger