import requests
from config.config import BASE_URL, TIMEOUT
from utils.logger import get_logger

logger = get_logger()

def get(endpoint):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"GET Request: {url}")

    response = requests.get(url, timeout=TIMEOUT)

    logger.info(f"Response Status: {response.status_code}")
    return response