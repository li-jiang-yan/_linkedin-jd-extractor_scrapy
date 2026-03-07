import json
from urllib.parse import quote
import scrapy
from bs4 import BeautifulSoup

class PostsSpider(scrapy.Spider):
    name = "posts"

    def __init__(self, keywords="Computer Science", location="Singapore", number=10):
        super().__init__()
        self.start_urls = [f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={quote(keywords)}&location={quote(location)}&start={start}" for start in range(0, int(number), 25)]
        self.posts = []

    def parse(self, response):
        self.posts += list(BeautifulSoup(html_doc, "html.parser").prettify() for html_doc in response.css("div.base-card").getall())

    def closed(self, _):
        with open("posts.json", "w", encoding="utf-8") as f:
            json.dump(self.posts, f, indent=4)
