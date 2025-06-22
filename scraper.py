import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://github.com/trending"

# Send GET request to GitHub Trending
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all repo items
repo_items = soup.find_all("article", class_="Box-row")[:5]  # Top 5

# Prepare data
data = []
for item in repo_items:
    # Extract the full repository name and link
    full_name = item.h2.a.text.strip().replace("\n", "").replace(" ", "")
    link = "https://github.com" + item.h2.a['href']
    data.append([full_name, link])
# Write to CSV
with open("trending_repos.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Repository Name", "Link"])  # header
    writer.writerows(data)

print("✅ Top 5 trending repositories saved to trending_repos.csv")
