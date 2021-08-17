from bs4 import BeautifulSoup
import requests
from smtplib import SMTP

header = {
    "Request Line": "GET / HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-ca",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
}

response = requests.get("https://www.amazon.ca/Instant-Programmable-Pressure-Cooker-Pot/dp/B01M71BZD9/ref=sr_1_1_sspa?crid=1CMPYVKQS3IFM&dchild=1&keywords=instant+pot&qid=1629185024&sprefix=instant+%2Caps%2C201&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSURMWFlKU0tIU1VXJmVuY3J5cHRlZElkPUExMDAxNDc4MVBCTThOQk1QVlRCSyZlbmNyeXB0ZWRBZElkPUEwMTI2MTkwMzgxQjM0MTJXRk9OVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=", headers=header)

ama_html = response.text

soup = BeautifulSoup(ama_html, "lxml")

price = float(soup.select_one(
    selector="#priceblock_ourprice").string.split("$")[1])


if price < 90:
    with SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(
            user="",
            password=""
        )
        server.sendmail(
            from_addr="",
            to_addrs="",
            msg=""
        )
