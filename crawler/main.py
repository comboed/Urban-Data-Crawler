import crawler
import captcha

if __name__ == "__main__":
    solver = captcha.Captcha("CAP-B367787B6A0E5DEEE4186194F7C81372")
    location = crawler.create_crawler(solver)
    print(location)