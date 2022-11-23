from tempfile import mkdtemp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service

from ..settings import CHROMEDRIVER_PATH, CHROMIUM_PATH


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    options.binary_location = CHROMIUM_PATH
    options.add_argument("--headless") # Hide the GUI
    options.add_argument("--no-sandbox") # No protection needed
    options.add_argument("--window-size=1280x1696") # Setup a fixed screens size
    options.add_argument("--single-process") # Lambda only give us only one CPU
    options.add_argument("--no-zygote") # Don't create zygote processes because Lambda give us only one CPU
    options.add_argument("--disable-dev-shm-usage") # Create temporary folder for shared memory files
    options.add_argument("--disable-dev-tools") # Disable Chrome dev tools
    options.add_argument(f"--user-data-dir={mkdtemp()}") # Create temporary folder to user data
    options.add_argument(f"--data-path={mkdtemp()}") # Create temporary folder to browser data
    options.add_argument(f"--disk-cache-dir={mkdtemp()}") # Create temporary folder to cache

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://example.com")
    header = driver.find_element(By.CSS_SELECTOR, "h1")
    text = header.text
    driver.close()
    driver.quit()
    response = {
        "statusCode": 200,
        "body": f"the header content is {text}",
    }
    print(response)
    return response


if __name__ == "__main__":
    handler()
