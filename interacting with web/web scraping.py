from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://olympus.realpython.org/profiles").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

base_url = "http://olympus.realpython.org"

for link in soup.find_all("a"):
    href = base_url + link["href"]
    print(f"......fecthing {href}")
    html = urlopen(href).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text())
print("......done\n")