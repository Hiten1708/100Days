from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import lxml

GOOGLE_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSe-OSG61-iFrble7x3syyRRVpFvLUcEJZH7IKhYkkkllnaPaQ/viewform?usp=sf_link'
ZILLOW = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61220015478516%2C%22east%22%3A-122.25445784521484%2C%22south%22%3A37.65239508094029%2C%22north%22%3A37.89798387341942%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
GOOGLE_DRIVER = '/Users/hitenpatel/Driver/chromedriver'

prices = []
adds = []
links = []

req_head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-ca',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
}


web = requests.get(url=ZILLOW, headers=req_head)
content = web.text
soup = BeautifulSoup(content, "lxml")
prices_html = soup.select(selector="div.list-card-heading > div")
adds_html = soup.select(selector="div.list-card-info > a > address")
links_html = soup.select(selector="div.list-card-top > a")

for link in links_html:
    links.append(link.get("href"))

for price in prices_html:
    prices.append(price.string)

for add in adds_html:
    adds.append(add.string)

all_data = []

try:
    for num in range(len(links)):
        if adds[num] is not None and prices[num] is not None and links[num] is not None:
            all_data.append(
                {"add": adds[num],
                 "ppm": prices[num],
                 "link": links[num]
                 }
            )
except IndexError as ele:
    print(f"{ele} out of range")


driver = webdriver.Chrome(GOOGLE_DRIVER)
driver.get(GOOGLE_FORM)

for char in all_data:
    driver.get(GOOGLE_FORM)
    time.sleep(3)
    address = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(char["add"])

    ppm = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ppm.send_keys(char["ppm"])

    link_prop = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_prop.send_keys(char["link"])

    sub = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span')
    sub.click()
