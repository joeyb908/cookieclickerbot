from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def set_current_cookies():
    if ',' in browser.find_element(By.ID, 'cookies').text:
        return int(browser.find_element(By.ID, 'cookies').text.split(' ')[0].replace(',', ''))
    return int(browser.find_element(By.ID, 'cookies').text.split(' ')[0])

# set purchase timeout to 10 seconds
timeout = time.time() + 10

# basic selenium setup
chrome_driver_path = r'C:\Users\joeyb\Desktop\chromedriver.exe'
s = Service(chrome_driver_path)
browser = webdriver.Chrome(service=s)
browser.get('https://orteil.dashnet.org/cookieclicker/')

# choose the English language
language = browser.find_element(By.ID, 'langSelect-EN')
language.click()

# find the cookie to click
cookie = browser.find_element(By.ID, 'bigCookie')

click_cookie = True
while click_cookie:
    # click the cookie
    cookie.click()

    # after purchase timeout ends
    if time.time() > timeout:
        # find the current amount of cookies you own, find any available purchasable items
        current_cookies = set_current_cookies()
        unlocked_item = browser.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')[::-1]
        unlocked_upgrades = browser.find_elements(By.CSS_SELECTOR, '.crate.upgrade.enabled')

        # purchase any upgrades
        for element in unlocked_upgrades:
            element.click()

        # purchase any available items (first item available at 15 cookies) and reset current cookies value
        for element in unlocked_item:
            item_price = 15
            while current_cookies > item_price:
                element.click()
                current_cookies = set_current_cookies()
                item_price = int(element.text.split()[1])

        # reset the timer
        timeout = time.time() + 5
        