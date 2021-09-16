from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.select("#name")
# print(heading)