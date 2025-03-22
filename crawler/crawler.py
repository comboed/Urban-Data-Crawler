import requests
import cookies
import captcha
import random

class Crawler:
    def __init__(self, max_crawlers, captcha_key, proxy = None):
        self.crawlers = []
        self.max_crawlers = max_crawlers
        self.captcha_key = captcha_key
        self.proxy = proxy

    def get_random_crawler(self):
        if (len(self.crawlers) < self.max_crawlers):
            new_crawler = self.create_crawler()
            self.crawlers.append(new_crawler)
            return new_crawler
        return random.choice(self.crawlers)

    def create_crawler(self, solver: captcha.Captcha):
        for i in range(10):
            crawler = requests.Session()
            crawler.headers = self.get_headers()
            if (self.proxy):
                crawler.proxies = {"http": "http://" + self.proxy, "https": "http://" + self.proxy}
                
            location = cookies.authorize_ip(crawler)
            if (location is None):
                print("[LOG]: Failed to pre-authorize IP")
                continue

            enterprise_value = cookies.get_enterprise_value(crawler, location)
            if (enterprise_value is None):
                print("[LOG]: Failed to get Google enterprise value")
                continue

            task_id = solver.create_captcha_task(location, enterprise_value)
            if (task_id is None):
                print("[LOG]: Failed to create captcha task with Capsolver")
                continue
            
            token = solver.get_captcha_result(task_id)
            if (token is None):
                print("[LOG]: Failed to get captcha token from Capsolver")
                continue
            
            abuse_location = cookies.get_abuse_cookie(crawler, token, location.split("&q=")[1])
            if (abuse_location is None):
                print("[LOG]: Failed to get abuse cookie")
                continue
            
            crawler.cookies.set("google_abuse", abuse_location.split("google_abuse=")[1].split(";")[0]) # Come back if cookies dont work to see if we need to add the domain
            return crawler

        return None



    def get_headers(self):
        return {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Downlink": "10",
            "Priority": "u=1, i",
            "Referer": "https://www.google.com/",
            "Rtt": "50",
            "Sec-CH-Prefers-Color-Scheme": "light",
            "Sec-CH-UA": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "Sec-CH-UA-Arch": '"x86"',
            "Sec-CH-UA-Bitness": '"64"',
            "Sec-CH-UA-Form-Factors": '"Desktop"',
            "Sec-CH-UA-Full-Version": '"134.0.6998.89"',
            "Sec-CH-UA-Full-Version-List": '"Chromium";v="134.0.6998.89", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.89"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Model": '""',
            "Content-Type": "application/x-www-form-urlencoded",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-CH-UA-Platform-Version": '"19.0.0"',
            "Sec-CH-UA-WoW64": "?0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "Cookie": "SG_SS="
    }