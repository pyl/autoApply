#https://github.com/BaruYogesh/Fall2021Internships/blob/master/US.md
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(ChromeDriverManager().install())

def get_info():
    with open("info.json", "r") as info:
        return json.load(info)

def rareApps():
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Family/Friend')]").click()
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Male')]").click()
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'I am not a protected veteran')]").click()
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'No, I don\'t have a disability, or a history/record of having a disability)]").click()
    except NoSuchElementException:
        pass

def applyGreenhouse(url):
    JOB_APP = get_info()
    print(JOB_APP)
    print("hi")

    driver.get(url)
    driver.find_element_by_id('first_name').send_keys(JOB_APP['user']['first_name'])
    driver.find_element_by_id('last_name').send_keys(JOB_APP['user']['last_name'])
    driver.find_element_by_id('email').send_keys(JOB_APP['user']['email'])
    driver.find_element_by_id('phone').send_keys(JOB_APP['user']['phone'])
    try:
        loc = driver.find_element_by_id('job_application_location')
        loc.send_keys(JOB_APP['location'])
        loc.send_keys(Keys.DOWN) # manipulate a dropdown menu
        loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.RETURN)
        time.sleep(2) # give user time to manually input if this fails
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    except NoSuchElementException:
        pass
    rareApps()
    c = input("Enter another link to apply to it or anything else to stop")
    if "https" in c:
        applyToForm(c)

def applyToForm(url):
    if 'greenhouse' in url:
        applyGreenhouse(url)


if __name__ == '__main__':
    url = input("Enter form")
    applyToForm(url)
