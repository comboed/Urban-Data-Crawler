import threading
import requests


class Summarizer:
    def __init__(self, openAI_key):
        self.openAI_key = openAI_key

    def process_data(self, data: dict):
        

        
    def send_query(self, query): # Will probably need to add a check incase theres an error as this would crash our program
        return requests.post("https://api.openai.com/v1/chat/completions", headers = {
            "Content-Type": "application/json",
            "Authorization": self.openAI_key
        }, json = {
            "model": "gpt-3.5-turbo-0125", # Replace model
            "messages": [{"role": "user", "content": "Briefly summarize this issue/query.\n\n" + query}],
            "temperature": 0
        }).json()["choices"][0]["message"]["content"]
    
