import threading
import requests


class Summarizer:
    def __init__(self, openAI_key):
        self.openAI_key = openAI_key

    def process_scraped_data(self, data: dict):
        points = {}
        threads = []

        for key in data.keys():
            thread = threading.Thread(target = self.process_points, args = (points, key, data[key]))
            thread.daemon = True
            threads.append(thread)
            
        for thread in threads:
            thread.start()    

        for thread in threads:
            thread.join()

        return points
            
    def process_points(self, points, key, data):
        for _ in range(5):
            response = self.send_query(data)
            if (response is not None):
                points[key] = response.split("* ")[1:]
                break
            points["Unexpected Error"] = ["Error", "Error"]

    def send_query(self, data): # Will probably need to add a check incase theres an error as this would crash our program
        response = requests.post("https://api.openai.com/v1/chat/completions", headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.openAI_key
        }, json = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": "Summarize this issue/data with multiple bullet points. (Start with *) Make just a tiny bit longer. Max 3 issues and then 3 solutions. Do not add any extra white space \n\n" + data}],
            "temperature": 0
        })

        if ("choices" not in response.text):
            print("[LOG]: AI Issue | " + response.text)
            return None
            
        return response.json()["choices"][0]["message"]["content"]
    
if __name__ == "__main__":
    summarize = Summarizer("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")
    data = summarize.send_query("Issues with texas cities")
    print(data)
    # print(data.split("*"))
    # print(data.split("(S")[0])
    # print("\n")
    # print(data.split("(S")[1])
