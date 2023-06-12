# pip install beautifulsoup4
#pip install requests

import requests
from bs4 import BeautifulSoup
import html5lib

url ="https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"

#Send an HTTP request to the webpage you want to scrape and retrieve its HTML content:
content = requests.get(url)

# fetching the content of html page
htmlcontent = content.content

# parsing or structuring raw html data
soup = BeautifulSoup(htmlcontent,'html.parser')

# fetching the title
title = soup.title
print(title.string)

# fetching the content of the page

pageContent = soup.get_text()
print(pageContent)