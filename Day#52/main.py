import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/hitenpatel/Driver/chromedriver"
INSTA_EMAIL = ""
INSTA_PASS = ""
SIMILAR_ACCOUNT = "chefsteps"
ins_site = "https://www.instagram.com/accounts/login/"
NUMBER_OF_SCROLLS = 5
NUMBER_OF_FOLLOWS = 100


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get(ins_site)

    def login(self):
        time.sleep(2)
        li_mail = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        li_mail.send_keys(INSTA_EMAIL)

        li_pwd = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        li_pwd.send_keys(INSTA_PASS)
        li_pwd.send_keys(Keys.RETURN)
        time.sleep(2)

        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')

    def find_followers(self):
        time.sleep(2)
        ck_folrs = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        ck_folrs.click()
        time.sleep(2)

        page = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[2]')
        for char in range(NUMBER_OF_SCROLLS):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", page)
            time.sleep(2)

    def follow(self):
        for char in range(1, NUMBER_OF_FOLLOWS):
            try:
                follow_btn = self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div/div/div[2]/ul/div/li[{char}]/div/div[2]/button')
                follow_btn.click()
                time.sleep(1)
            except selenium.common.exceptions.ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath(
                    '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
                continue
            except selenium.common.exceptions.NoSuchElementException:
                continue


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
