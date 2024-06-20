import requests
from bs4 import BeautifulSoup

# Naver search URL for "반도체"
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract news article titles
titles = []
for item in soup.find_all('a', class_='news_tit'):
    titles.append(item.get_text())

# Print the titles
for idx, title in enumerate(titles, start=1):
    print(f"{idx}. {title}")
