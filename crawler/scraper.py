import crawler

class Scraper:
    def __init__(self, max_crawlers, proxy = None):
        self.crawlers = []
        self.max_crawlers = max_crawlers
        self.proxy = None

    def get_random_crawler(self):
        if (len(self.crawlers) < self.max_crawlers):
            new_crawler = crawler.create_crawler(self.proxy)