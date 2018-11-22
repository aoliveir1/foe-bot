from pyvirtualdisplay import Display
from selenium import webdriver

with Display():
  browser = webdriver.Firefox()
  
  try:
    browser.get('https://br5.forgeofempires.com/')
    browser.save_screenshot('screenshot.png')
    print(browser.title)
  finally:
    browser.quit()
