import requests
import urllib.parse

def authorize_ip(crawler: requests.Session):
    response = crawler.get("https://www.google.com/search?q=test", allow_redirects = False)
    
    if ("302 Moved" not in response.text):
        return None
        
    return response.headers["Location"]

def get_enterprise_value(crawler: requests.Session, location):
    response = crawler.get(location).text

    if ("data-s=" not in response):
        return None
    
    return response.split('data-s="')[1].split('"')[0]

def get_abuse_cookie(crawler: requests.Session, token, q_token):
    response = crawler.post("https://www.google.com/sorry/index", data = {
        "g-recaptcha-response": token,
        "q": q_token,
        "continue": "https://www.google.com/search?q=test"
    }, allow_redirects = False)

    if (response.status_code != 302):
        return None
    
    return urllib.parse.unquote(response.headers["Location"])