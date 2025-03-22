import scraper

if __name__ == "__main__":
    google_scraper = scraper.Scraper(1, "CAP-B367787B6A0E5DEEE4186194F7C81372")
    google_scraper.lookup_query("test", 1)