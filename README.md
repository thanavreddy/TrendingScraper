# GitHub Trending Scraper

This Python script scrapes the top 5 trending repositories from [GitHub Trending](https://github.com/trending) using `requests` and `BeautifulSoup`, and saves the results to a CSV file.

##  Features

- Scrapes top 5 trending repositories from GitHub
- Extracts repository name and direct GitHub link
- Saves data into a structured CSV file: `trending_repos.csv`

## Output Format

The CSV file includes the following columns:

| Repository Name     | Link                                 |
|---------------------|--------------------------------------|
| `vercel/next.js`    | `https://github.com/vercel/next.js`  |
| `microsoft/vscode`  | `https://github.com/microsoft/vscode`|
| ...                 | ...                                  |

##  How to Run

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4
```

### 2. Run the Script

```bash
python github_trending_scraper.py
```

### 3. Check the Output

A file named `trending_repos.csv` will be generated in the same directory containing the scraped data.

##  Built With

- **Python** - Core programming language
- **Requests** - HTTP library for making web requests
- **BeautifulSoup** - HTML parsing and web scraping

## Requirements

- Python 3.6+
- Internet connection
- Required packages: `requests`, `beautifulsoup4`

##  Quick Start

1. Clone or download the script
2. Install the required dependencies
3. Run the script to get the latest trending repositories
4. Open `trending_repos.csv` to view the results

## Notes

- The script fetches data from the public GitHub Trending page
- Results may vary based on GitHub's current trending repositories
- CSV output can be easily imported into spreadsheet applications 

---
