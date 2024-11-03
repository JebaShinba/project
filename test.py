import unittest
from unittest.mock import MagicMock
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  # Import Options here
import time

# Function to be tested
def search_google(driver, query):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    return driver.find_elements("css selector", "h3")  # Return search results


# Unit Tests
class TestSearchModule(unittest.TestCase):
    
    def test_search_google(self):
        # Mocking the webdriver
        mock_driver = MagicMock()
        mock_results = [MagicMock(text="Test Title 1"), MagicMock(text="Test Title 2")]
        mock_driver.find_elements.return_value = mock_results
        
        results = search_google(mock_driver, "Selenium Python")
        
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].text, "Test Title 1")
        self.assertEqual(results[1].text, "Test Title 2")


# End-to-End Tests
class TestGoogleE2E(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()  # Use Options for the Chrome driver
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Overcome limited resource problems
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_search_selenium_python(self):
        self.driver.get("https://www.google.com")
        time.sleep(2)  # Allow time for page to load

        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Allow time for results to load

        results = self.driver.find_elements("css selector", "h3")
        self.assertGreater(len(results), 0, "No results found.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Close the browser


# Smoke Tests
class TestGoogleSmoke(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()  # Use Options for the Chrome driver
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Overcome limited resource problems
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_basic_google_search(self):
        self.driver.get("https://www.google.com")
        time.sleep(2)

        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        results = self.driver.find_elements("css selector", "h3")
        self.assertGreater(len(results), 0, "Smoke test failed: No results found.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
