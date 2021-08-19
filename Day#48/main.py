import selenium.common.exceptions
from selenium import webdriver
import time

chrome_driver = "/Users/hitenpatel/Driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cooks = ["Cursor", "Grandma", "Factory", "Mine",
         "Shipment", "Alchemy lab", "Portal", "Time machine"]
start = time.time()

while True:
    try:
        driver.find_element_by_id("cookie").click()
        cookie_rate = float(driver.find_element_by_id("cps").text.split()[-1])
        cookie_count = int(driver.find_element_by_id(
            "money").text.replace(",", ""))
        end = time.time()
        if (end - start) % 5 < 0.05:
            for char in cooks:
                element = driver.find_element_by_xpath(
                    f'//*[@id="buy{char}"]/b')
                price = float(element.text.split()[-1].replace(",", ""))
                if price > cookie_count:
                    driver.find_element_by_xpath(
                        f'//*[@id="buy{cooks[cooks.index(char) - 1]}"]/b').click()
                    break
    except selenium.common.exceptions.StaleElementReferenceException:
        cursor = driver.find_element_by_id("buyCursor")
        cursor.click()
