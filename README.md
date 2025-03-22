# Urban Intelligence Crawler

Urban Intelligence Crawler is a web-based tool designed to extract real-time data from the web, summarize key insights using AI, and present the results in a structured format. It is built for use cases such as urban planning, city monitoring, and research.

The application scrapes search results from Google, summarizes relevant information using OpenAI's GPT model, and categorizes the content into issues and solutions. It includes features for limiting result count, caching results to reduce repeated processing, and threaded summarization for performance.

---

## Features

- Scrapes real-time data from Google based on a search query
- Summarizes results using OpenAI (up to 3 issues and 3 solutions per result)
- Clean frontend with a modern, responsive design
- Allows user-defined result limits
- In-memory caching to avoid redundant API calls
- Multi-threaded summarization for faster response times
- Source link highlighting with animated hover effects

---

## Requirements

- Python 3.8+
- Flask
- Requests

Install dependencies:

```bash
pip install -r requirements.txt
Configuration
Create a file at ./config/config.json with the following structure:

json
Copy
Edit
{
  "CAPSOLVER_KEY": "your-capsolver-key",
  "CRAWLERS": 1,
  "OPENAI_KEY": "your-openai-api-key"
}
Running the App
bash
Copy
Edit
python app.py
Then visit: http://127.0.0.1:5000 in your browser.

Project Structure
graphql
Copy
Edit
.
├── app.py               # Main Flask application
├── summarizer.py        # OpenAI-powered summarization logic (threaded)
├── crawler/
│   └── scraper.py       # Google scraper (CAPTCHA + result parser)
├── templates/
│   └── index.html       # Web UI (Jinja2 + CSS)
├── static/
│   └── styles.css       # Styling and animations
├── config/
│   └── config.json      # Your API keys and settings
└── README.md            # This file
License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

✅ You can copy-paste that directly into `README.md`.  
Want me to generate a matching `requirements.txt` based on your code too?






