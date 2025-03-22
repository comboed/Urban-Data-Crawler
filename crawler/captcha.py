import requests

class Captcha:
    def __init__(self, captcha_key):
        self.captcha_key = captcha_key

    def create_captcha_task(self, location, enterprise_value):
        response = requests.post("https://api.capsolver.com/createTask", headers = {
            "Content-Type": "application/json"
        }, json = {
            "clientkey": self.captcha_key,
            "task": {"type":"ReCaptchaV2Task","websiteURL": location, "websiteKey":"6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b","enterprisePayload":{"s": enterprise_value}}
        })

        if ("taskId" not in response.text):
            return None
        
        return response.json()["taskId"]
    
    def get_captcha_result(self, task_id):
        for _ in range(30):
            response = requests.post("https://api.capsolver.com/getTaskResult", headers = {
                "Content-Type": "application/json"
            }, json = {
                "clientkey": self.captcha_key,
                "taskId": task_id
            })

            if ("gRecaptchaResponse" in response.text):
                return response.json()["solution"]["gRecaptchaResponse"]
            
        return None