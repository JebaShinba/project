import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
driver = webdriver.Chrome()  # This assumes chromedriver is in your PATH

# Alternatively, specify the path to the ChromeDriver executable:
# driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # Adjust the path as necessary

# Your test code goes here
try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Wait for the page to load
    time.sleep(2)
    
    # Find the search box using its name attribute value
    search_box = driver.find_element("name", "q")
    
    # Type the search query and press Enter
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results to load
    time.sleep(2)
    
    # Get the search results
    results = driver.find_elements("css selector", "h3")
    
    # Print the titles of the search results
    for result in results:
        print(result.text)

finally:
    # Close the browser
    driver.quit()
# execute the script
if __name__ == "__main__":
    unittest.main()
