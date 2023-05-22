# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# @pytest.fixture(scope="module")
# def browser():
#     # Setup: Initialize the Chrome browser
#     options = webdriver.ChromeOptions()
#     # Add any necessary options or configurations
    
#     # Provide the explicit path to the WebDriver executable
#     webdriver_path = '/usr/local/bin/chromedriver'  # Replace with the actual path to chromedriver
#     # webdriver_path = '/usr/local/bin/google'  # Replace with the actual path to chromedriver
    
    
#     service = Service(webdriver_path)
#     browser = webdriver.Chrome(service=service, options=options)
    
#     yield browser
    
#     # Teardown: Close the browser
#     browser.quit()

# def test_web_browse(browser):
#     # Rest of your test code remains the same
#     browser.get("https://www.google.com")
#     assert browser.title == "Google"
#     browser.get("https://www.python.org")
#     assert browser.title == "Welcome to Python.org"
#     browser.get("https://www.selenium.dev")
#     assert browser.title == "SeleniumHQ Browser Automation"
#     browser.get("https://www.github.com")
    
import time

from selenium import webdriver


``
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()