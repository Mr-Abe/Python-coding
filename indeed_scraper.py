import httpx
import time
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
}


URL = "https://www.indeed.com/?from=gnav-jobsearch--indeedmobile"
while True:
    response = httpx.get("https://www.indeed.com/jobs?q=python&l=Texas", headers=HEADERS)
    if response.status_code == 200:
        break
    else:
        print(f"Request blocked. Retrying in a few seconds...")
        time.sleep(random.randint(5, 10))  # Wait for a few seconds before retrying

print(response)
