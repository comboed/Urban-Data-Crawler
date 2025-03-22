# Urban Intelligence Crawler

Urban Intelligence Crawler is a web-based tool designed to extract real-time data from the web, summarize key insights using AI, and present the results in a structured format. It is built for use cases such as urban planning, city monitoring, and research.

The application scrapes search results from Google, summarizes relevant information using OpenAI's GPT model, and categorizes the content into issues and solutions. It includes features for limiting result count, caching results to reduce repeated processing, and threaded summarization for performance.

---

## Features

- Scrapes real-time data from Google based on a search query
- Summarizes results using OpenAI (up to 3 issues and 3 solutions)
- Clean frontend with a modern, responsive design
- Supports user-defined result limits
- In-memory caching to avoid redundant API calls
- Multi-threaded summarization for faster response times

---

## Requirements

- Python 3.8+
- Flask
- Requests

---

## Configuration

API keys are stored in a `config.json` file in the following format:

```json
{
  "CAPSOLVER_KEY": "your-capsolver-key",
  "CRAWLERS": 1,
  "OPENAI_KEY": "your-openai-api-key"
}
