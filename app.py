from crawler import scraper

# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}

    if request.method == "POST":
        query = request.form.get("query")
        pages = int(request.form.get("pages", 1))
        
        

        # Placeholder: Replace this with your real scraping logic
        # results = {
        #     f"Result Title {i+1}": f"Snippet for result {i+1} on '{query}'"
        #     for i in range(pages)
        # }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)


# if __name__ == "__main__":
#     google_scraper = scraper.Scraper(1, "CAP-B367787B6A0E5DEEE4186194F7C81372")
#     data =  google_scraper.lookup_query("test", 1)
#     print(data)