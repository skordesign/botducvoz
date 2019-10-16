from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
showthread = "showthread.php?t"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

def thread(a_tag):
    return a_tag.text, a_tag.get_attribute('href')

def getPosts():
    driver.switch_to.window(driver.window_handles[1])
    threads = driver.find_elements_by_xpath('//a[contains(@href, "{}")]'.format(showthread))
    threads = threads[2:]
    return list(map(thread, threads))
def condition(post):
    return True
def collect(posts):
    return list(filter(condition, posts))

def post_thread(posts):
    driver.switch_to.window(driver.window_handles[0])
    

def run():
    while True:
        posts = getPosts()
        posts = collect(posts)
        post_thread(posts)

def login(username, password):
    driver.find_element_by_name('vb_login_username').send_keys(username)
    driver.find_element_by_name('vb_login_password').send_keys(password)
    driver.find_element_by_name('cookieuser').click()
    driver.find_element_by_name('vb_login_password').send_keys(Keys.RETURN)
    
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, '//a[contains(text(), "Click here")]')))
    driver.find_element_by_xpath('//a[contains(text(), "Click here")]').click()
def init():
    driver.get(sys.argv[3])
    login(sys.argv[1], sys.argv[2])
    driver.execute_script("window.open()")
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.get(sys.argv[4])

if __name__ == "__main__":
    init()
    run()
    driver.close()

