from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time

chrome_driver = "/Users/hitenpatel/Driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://tinder.com/app/recs")

time.sleep(3)
logIn = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
logIn.click()

time.sleep(2)
logIn1 = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[3]/button')
logIn1.click()

time.sleep(20)
numPut = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[1]/div[2]/div/input')
numPut.send_keys('6472078688')

time.sleep(1)
cont = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
cont.click()

time.sleep(60)

allow = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow.click()

time.sleep(20)

while True:
    try:
        time.sleep(2)
        like = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
    except NoSuchElementException:
        break
    else:
        like.click()
