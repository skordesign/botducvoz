from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import re
import sys

start = '[IMG]'
end = '[/IMG]'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://forums.voz.vn/forumdisplay.php?f=17&order=desc")
showthread = "showthread.php?t"
count_post = "0"
quotes_count = 0
current_user = ""


def login():
    username = sys.argv[1]
    password = sys.argv[2]
    driver.find_element_by_name('vb_login_username').send_keys(username)
    driver.find_element_by_name('vb_login_password').send_keys(password)
    driver.find_element_by_name('cookieuser').click()
    driver.find_element_by_name('vb_login_password').send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, '//a[@href="/forumdisplay.php?f=17&order=desc"]')))


def clearImage():
    message = driver.find_element_by_name('message')
    text = message.text
    while text.find(start) != -1:
        t = text[text.find(start)+len(start):text.find(end)]
        text = text.replace('[IMG]{}[/IMG]'.format(t),
                            '[URL="{}"]Ảnh[/URL]'.format(t))
    while text.find('[img]') != -1:
        t = text[text.find('[img]')+len('[img]'):text.find('[/img]')]
        text = text.replace('[img]{}[/img]'.format(t),
                            '[URL="{}"]Ảnh[/URL]'.format(t))                        
    message.clear()
    # message.send_keys(text)
    script = """arguments[0].value=arguments[1]"""
    driver.execute_script(script, message, text)
    return text

def quote(oldposts, name):
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, '//tr/td/div/a[contains(@href, "newreply.php")]')))
    driver.find_element_by_xpath(
        '//tr/td/div/a[contains(@href, "newreply.php")]').click()
    val = clearImage()
    val += '\n'
    message = driver.find_element_by_name('message')
    val += 'ĐỨC :sexy:\n\n'
    if len(oldposts) == 0:
        val += '[I]Đéo tìm được threads của [/I] [COLOR="Red"][B]{}[/B][/COLOR]\n'.format(
            name)
    else:
        val += '[I]{} Latest thread of[/I] [COLOR="Red"][B]{}:[/B][/COLOR]\n'.format(
            len(oldposts), name)
    for text in oldposts:
        val += '[URL="{}"]{}[/URL]\n'.format(text[1], text[0])
    val += '\nBOT Lậu 4.0\n'
    script = """arguments[0].value=arguments[1]"""
    driver.execute_script(script, message, val)
    driver.find_element_by_id('vB_Editor_001_save').submit()
    print('ĐỨC')
    print(datetime.datetime.now())
    findZeroReplies()


def getDetail(atag):
    return atag.text, atag.get_attribute("href")


def getTenPosts():
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, '//tr/td/div/a[@class="bigusername"]')))
    name = driver.find_element_by_xpath('//tr/td/div/a[@class="bigusername"]')
    name.click()
    current_user = name.text
    driver.find_element_by_xpath(
        '//tr/td/a[contains(text(), "View Public Profile")]').click()

    driver.find_element_by_id('stats_tab').click()
    threadButton = driver.find_element_by_xpath(
        '//ul/li/a[contains(text(), "Find all threads started by")]')
    # driver.back()
    #quote([], current_user)
    if not threadButton.is_displayed():
        driver.back()
        quote([], current_user)
    else:
        threadButton.click()
        wait.until(ec.visibility_of_element_located(
            (By.XPATH, '//tr/td/a[@href="search.php?"]/strong')))
        listthread = driver.find_elements_by_xpath(
            '//tr/td/div/a[contains(@href, "%s")]' % showthread)
        texts = list(map(getDetail, listthread))
        driver.back()
        driver.back()
        quote(texts[:10], current_user)


def findZeroReplies():
    driver.get("https://forums.voz.vn/forumdisplay.php?f=17&order=desc")
    elements = driver.find_elements_by_xpath(
        '//tr/td[@class="alt1"]/a[text() = "%s"]' % count_post)
    if len(elements) == 0:
        findZeroReplies()
    else:
        elements[0].find_element_by_xpath(
            '../../td[@class="alt1"]/div/a[contains(@href, "%s")]' % showthread).click()
        getTenPosts()


login()
findZeroReplies()
driver.close()
