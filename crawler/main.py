import scraper
import captcha

if __name__ == "__main__":
    google_scraper = scraper.Scraper(1, "CAP-B367787B6A0E5DEEE4186194F7C81372")
    data = google_scraper.lookup_query("test", 1)
    print(data)
    #solver = captcha.Captcha("CAP-B367787B6A0E5DEEE4186194F7C81372")
    # location = crawler.create_crawler(solver)
    #print(location)