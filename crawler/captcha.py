import requests


def create_captcha_task(location, enterprise_value):

    respons = requests.post("https://api.capsolver.com/createTask")