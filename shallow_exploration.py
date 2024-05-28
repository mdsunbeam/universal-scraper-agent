from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time




# # Open the target website
# website_url = 'https://mdsunbeam.com/'  # Replace with your target website
# driver.get(website_url)


# Function to explore links on a page
def explore_links(url, depth=1):

    # Set up the WebDriver with headless option
    options = Options()
    options.add_argument("--headless")  # Run headless browser to avoid opening a window
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Set to keep track of visited URLs
    visited_links = set()

    if depth == 0 or url in visited_links:
        return
    
    visited_links.add(url)
    driver.get(url)
    time.sleep(2)  # Allow some time for the page to load

    # Extract all links on the page
    links = driver.find_elements(By.TAG_NAME, 'a')
    link_hrefs = [link.get_attribute('href') for link in links if link.get_attribute('href') and link.get_attribute('href').startswith('http')]

    # Visit each link
    for href in link_hrefs:
        try:
            print(f'Exploring: {href}')
            driver.get(href)
            time.sleep(2)  # Allow some time for the page to load

            # Recursively explore links (one level deep)
            explore_links(href, depth - 1)

            # Get the total height of the page
            total_height = driver.execute_script("return document.body.scrollHeight")
            # Set the window size to the full height
            driver.set_window_size(1920, total_height)
            # Take the screenshot
            output_file = f"images/screenshot_{hash(href)}.png"
            driver.save_screenshot(output_file)
            print(f"Screenshot saved to {output_file}")
            driver.back()  # Navigate back to the previous page
            time.sleep(2)  # Allow some time for the page to load
        except Exception as e:
            print(f'Error exploring {href}: {e}')
    driver.quit()

# Start exploring from the home page
explore_links(website_url, depth=1)

