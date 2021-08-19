import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "/Users/hitenpatel/Driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python")

time.sleep(3)
signIn = driver.find_element_by_link_text("Sign in")
signIn.click()

time.sleep(1)
email_input = driver.find_element_by_id("username")
email_input.send_keys("patelhiten1409@gmail.com")
pas_input = driver.find_element_by_id("password")
pas_input.send_keys("h1t3npatel")
pas_input.send_keys(Keys.ENTER)


for char in range(1, 7):
    try:
        page = driver.find_element_by_xpath(
            f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{str(char)}]/div/div/div[1]/div[2]/div[1]/a')
        page.click()

        time.sleep(3)
        eaap = driver.find_element_by_xpath(
            '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button')
        eaap.click()

        time.sleep(1)
        phone = driver.find_element_by_name(
            "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2670344243,32472589,phoneNumber~nationalNumber)")
        phone.clear()
        phone.send_keys("6472078688")
        sub = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button')
        sub.click()
        sub2 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]')
        sub2.click()
        sub3 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]')
        sub3.click()
        x = driver.find_element_by_xpath('/html/body/div[3]/div/div/button')
        x.click()
        discard = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[3]/button[2]')
        discard.click()
    except selenium.common.exceptions.NoSuchElementException:
        x = driver.find_element_by_xpath('/html/body/div[3]/div/div/button')
        x.click()
        discard = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[3]/button[2]')
        discard.click()

'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div/div[1]/div[2]/div[1]/a'
'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[2]/div/div/div[1]/div[2]/div[1]/a'
'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[3]/div/div/div[1]/div[2]/div[1]/a'
