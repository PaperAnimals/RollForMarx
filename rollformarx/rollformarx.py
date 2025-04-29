from bs4 import BeautifulSoup
import requests
import json
import random
import webbrowser

author_json_URL = "https://www.marxists.org/admin/js/data/authors.json"
page = requests.get(author_json_URL)

author_json_str = str(BeautifulSoup(page.content, "html.parser"))
author_json = json.loads(author_json_str)

author = random.choice(author_json)

href = author['href']
working_URL = "https://www.marxists.org/" + href

if href[-9:] != "index.htm":
  webbrowser.open_new(working_URL)

else:
  working_page = requests.get(working_URL)
  author_index_soup = BeautifulSoup(working_page.content, "html.parser")
  valid_links = []

  for a in author_index_soup.find_all('a'):
    if a['href'][-9:] != 'index.htm':
      valid_links.append(a['href'])

  reading_extension = random.choice(valid_links)
  webbrowser.open_new(working_URL[:-9] + reading_extension)