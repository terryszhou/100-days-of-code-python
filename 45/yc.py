import requests
from bs4 import BeautifulSoup as bs

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = bs(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = [tag.getText() for tag in articles]
article_links = [tag.get("href") for tag in articles]

# for article_tag in articles:
#     article_texts.append(article_tag.getText())
#     article_links.append(article_tag.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
top_article_index = article_upvotes.index(max(article_upvotes))
top_article_text = article_texts[top_article_index]
top_article_link = article_links[top_article_index]