from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

def login(username, password):
    driver.find_element_by_name('vb_login_username').send_keys(username)
    driver.find_element_by_name('vb_login_password').send_keys(password)
    driver.find_element_by_name('cookieuser').click()
    driver.find_element_by_name('vb_login_password').send_keys(Keys.RETURN)
    driver.find_element_by_id('a[contains(text(), "Click here")]').click()
def init():
    driver.get(sys.argv[3])
    login(sys.argv[1], sys.argv[2])
    driver.execute_script("window.open()")
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.get(sys.argv[4])

if __name__ == "__main__":
    init()

