from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver with headless option
options = Options()
options.add_argument("--headless")  # Run headless browser to avoid opening a window
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the target website
website_url = 'https://mdsunbeam.com/'  # Replace with your target website
driver.get(website_url)

# Function to explore links on a page
def explore_links(url, depth=1):
    if depth == 0:
        return
    
    driver.get(url)
    time.sleep(2)  # Allow some time for the page to load

    # Extract all links on the page
    links = driver.find_elements(By.TAG_NAME, 'a')
    link_hrefs = [link.get_attribute('href') for link in links if link.get_attribute('href')]

    # Visit each link
    for href in link_hrefs:
        try:
            print(f'Exploring: {href}')
            driver.get(href)
            time.sleep(2)  # Allow some time for the page to load
            # Recursively explore links (one level deep)
            explore_links(href, depth - 1)
            driver.back()  # Navigate back to the previous page
            time.sleep(2)  # Allow some time for the page to load
        except Exception as e:
            print(f'Error exploring {href}: {e}')

# Start exploring from the home page
explore_links(website_url, depth=1)

# Close the WebDriver
driver.quit()