from bs4 import BeautifulSoup
import requests
import lxml

website = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")
content = website.text
soup = BeautifulSoup(content, "lxml")

# top_lists = soup.select(selector="div h3")

print(soup.div)

# __next > main > article > div.jsx-2601023975.article-content > div.jsx-3821216435.block-item.listicle-container > div:nth-child(1) > h3
