from tempfile import mkdtemp

from selenium import webdriver
from selenium.webdriver.common.by import By

from ..settings import CHROMEDRIVER_PATH, CHROMIUM_PATH


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    options.binary_location = CHROMIUM_PATH
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
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
