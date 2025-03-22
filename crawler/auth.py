import requests

def pre_authorize_ip(crawler: requests.Session):
    response = crawler.get("https://www.google.com/search?q=test")
    
    if ("302 Moved" not in response.text):
        return None
    
    return response.headers["Location"]

def get_enterprise_value(crawler: requests.Session, location):
    response = crawler.get(location).text

    if ("data-s=" not in response):
        return None
    
    return response.split('data-s="')[1].split('"')[0]