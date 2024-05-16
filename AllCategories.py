from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Your Python code here
# For example:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://example.com")
time.sleep(5)
driver.quit()


# Setup Chrome WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the webpage
driver.get("https://myofer.co.il/malls/ramat-aviv/shopping-online/cat/All-Categories/3000")

# Function to perform click action
def click_button():
    try:
        # Locate the button by XPath and click it
        button = driver.find_element(By.XPATH, '//*[@id="main-layer"]/div/main/div/div/div/div/div[4]/div[2]/div[3]/a[215]/a/button/span')
        button.click()
    except NoSuchElementException:
        print("Button not found.")

# Loop to click the button every 2 seconds
try:
    while True:
        click_button()
        time.sleep(2)  # Delay for 2 seconds before next click
except KeyboardInterrupt:
    print("Script interrupted by user.")

# Clean up: close the browser window
driver.quit()
