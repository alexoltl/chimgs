import requests
from bs4 import BeautifulSoup
import os

url = ""
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

for a in soup.find_all("a"):
    a_url = a.get("href")
    if a_url.startswith("//i.4cdn.org/"):
        a_url = "https:" + a_url
        a_name = os.path.basename(a_url)
        response = requests.get(a_url)
        with open(a_name, "wb") as f:
            f.write(response.content)
            print(f"Saved {a_name}")
