from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def take_full_screenshot(url, output_file):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service('chromedriver-mac-arm64/chromedriver'), options=chrome_options)
    
    try:
        # Open the webpage
        driver.get(url)
        
        # Wait for a specific element to load (adjust the selector to match an element on your target page)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        
        # Optionally, wait for additional time to ensure the entire page is loaded
        time.sleep(2)  # Adjust the sleep time as needed
        
        # Get the total height of the page
        total_height = driver.execute_script("return document.body.scrollHeight")
        
        # Set the window size to the full height
        driver.set_window_size(1920, total_height)
        
        # Take the screenshot
        driver.save_screenshot(output_file)
        
        print(f"Screenshot saved to {output_file}")
    finally:
        driver.quit()

# Example usage
take_full_screenshot('https://mdsunbeam.com/', 'images/full_screenshot.png')