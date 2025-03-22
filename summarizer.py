import threading
import requests


class Summarizer:
    def __init__(self, openAI_key):
        self.openAI_key = openAI_key

    def process_scraped_data(self, data: dict):
        summaries = {}
        threads = []

        for key in data.keys():
            thread = threading.Thread(target = self.process_summary, args = (summaries, key, data[key]))
            thread.daemon = True
            threads.append(thread)
            
        for thread in threads:
            thread.start()    

        for thread in threads:
            thread.join()

        return summaries
            
    def process_summary(self, summaries, key, data):
        for _ in range(5):
            summary = self.send_query(data)
            if (summary is not None):
                summaries[summary.split("TITLE: ")[1].split("|")[0]] = [summary.split("REASON: ")[1].split("|")[0], summary.split("SOLUTION: ")[1].split("|")[0], key]
                break
            summaries["Unexpected Error"] = ["Error", "Error"]

    def send_query(self, data): # Will probably need to add a check incase theres an error as this would crash our program
        response = requests.post("https://api.openai.com/v1/chat/completions", headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.openAI_key
        }, json = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": "Summarize this issue/data with multiple points seperated with |. TITLE:, REASON:, SOLUTION: Make sure the reason/issue is strong and can be just a LITTLE lengthy. Just follow the exact format.\n\n" + data}],
            "temperature": 0
        })

        if ("choices" not in response.text):
            print("[LOG]: AI Issue | " + response.text)
            return None
            
        return response.json()["choices"][0]["message"]["content"]