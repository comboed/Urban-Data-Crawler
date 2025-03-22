from flask import Flask, render_template, request
from crawler import scraper
import summarizer

app = Flask(__name__)

google_scraper = scraper.Scraper(1, "CAP-B367787B6A0E5DEEE4186194F7C81372")
summary = summarizer.Summarizer("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")

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}

    if request.method == "POST":
        query = request.form.get("query")
        page = int(request.form.get("page", 1))

        scraped_data = google_scraper.lookup_query(query, page)
        results = summary.process_scraped_data(scraped_data)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
