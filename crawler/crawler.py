import requests
import auth

def create_crawler(proxy = None):
    crawler = requests.Session()
    if (proxy):
        crawler.proxies = {"http": "http://" + proxy, "https": "http://" + proxy}
    
    crawler.headers = get_headers()

    return crawler

def get_headers():
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
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-CH-UA-Platform-Version": '"19.0.0"',
        "Sec-CH-UA-WoW64": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Cookie": "SG_SS="
}