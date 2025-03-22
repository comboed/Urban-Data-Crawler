from flask import Flask, render_template, request
from crawler import scraper

import summarizer
import hashlib
import base64
import json
import time

with open("./config/config.json", "r") as file:
    config = json.load(file)

google_scraper = scraper.Scraper(config["CAPSOLVER_KEY"], config["CRAWLERS"])
summary = summarizer.Summarizer(base64.b64decode(config["OAI_64"]).decode())

app = Flask(__name__)
cache = {}
CACHE_TTL = 60 * 60 * 24

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}

    if request.method == "POST":
        query = request.form.get("query")
        page = int(request.form.get("page", 1))
        limit = int(request.form.get("limit", 1))
        cache_key = hashlib.sha256(f"{query.lower()}:{page}".encode()).hexdigest()

        if cache_key in cache:
            cached = cache[cache_key]
            if time.time() - cached["timestamp"] < CACHE_TTL:
                print("✅ Returning cached result")
                results = cached["data"]
            else:
                del cache[cache_key]  # Expired
        else:
            print("🔄 Fetching new result")
            scraped = google_scraper.lookup_query(query, page, limit)
            results = summary.process_scraped_data(scraped)

            cache[cache_key] = {
                "data": results,
                "timestamp": time.time()
            }

    return render_template("index.html", results=results)

if __name__ == "__main__":    
    app.run(debug = True)