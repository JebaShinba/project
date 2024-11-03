import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestGoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome driver
        cls.driver = webdriver.Chrome()  # This assumes chromedriver is in your PATH
        # Alternatively, specify the path to the ChromeDriver executable:
        # cls.driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # Adjust as necessary

    def test_search_selenium_python(self):
        # Open Google
        self.driver.get("https://www.google.com")

        # Wait for the page to load
        time.sleep(2)

        # Find the search box using its name attribute value
        search_box = self.driver.find_element("name", "q")

        # Type the search query and press Enter
        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(2)

        # Get the search results
        results = self.driver.find_elements("css selector", "h3")

        # Check if the results contain expected text
        self.assertGreater(len(results), 0, "No results found")  # Ensure there are results
        for result in results:
            print(result.text)

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

# Execute the tests
if __name__ == "__main__":
    unittest.main()
