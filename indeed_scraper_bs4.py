from bs4 import BeautifulSoup as bs
from datetime import datetime
import time
import requests
import random
import csv

user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.51",
    "Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Android 12; Mobile; rv:103.0) Gecko/103.0 Firefox/103.0",
    "Mozilla/5.0 (Linux; Android 12; SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/103.0.5060.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2045) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/67.1.3360.57388",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.71 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (X11; CrOS x86_64 13904.77.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
]

def get_url(position, location):
    URL_template = 'https://www.indeed.com/jobs?q={}&l={}'
    url = URL_template.format(position, location)

    return  url

max_retries = 5

# Corrected list of proxies to be tried
proxies = [
    {"http://": "http://103.54.45.99:8026"},
    {"http://": "http://134.209.67.109:26000"},
    {"http://": "http://20.190.104.113:80"},
    {"http://": "http://108.170.12.11:80"},
    {"http://": "http://203.95.196.140:8080"},
    {"http://": "http://37.1.218.227:80"},
    {"http://": "http://178.18.206.9:9443"},
    {"http://": "http://162.240.75.37:80"},
    {"http://": "http://1.162.14.236:80"},
    {"http://": "http://14.56.137.86:80"},
    {"http://": "http://92.207.253.226:38157"},
    {"http://": "http://122.175.19.164:80"},
    {"http://": "http://114.143.0.179:80"},
    {"http://": "http://66.59.197.110:80"},
    {"http://": "http://84.15.154.202:80"},
    {"http://": "http://141.147.9.254:80"},
    {"http://": "http://109.195.23.223:34031"},
    {"http://": "http://191.101.80.162:80"},
    {"http://": "http://51.210.216.54:80"},
    {"http://": "http://43.255.113.232:80"},
    {"http://": "http://164.132.170.100:80"},
    {"http://": "http://167.99.174.59:80"},
    {"http://": "http://152.230.215.123:80"},
    {"http://": "http://104.225.220.233:80"},
    {"http://": "http://203.189.96.232:80"},
    {"http://": "http://173.255.119.18:80"},
    {"http://": "http://178.128.200.87:80"},
    {"http://": "http://51.89.255.67:80"},
    {"http://": "http://45.92.108.112:80"},
    {"http://": "http://89.23.112.143:80"}
]

URL = get_url("senior accountant", "Indianapolis")

for _ in range(max_retries):
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Accept-Language": "en-US,en;q=0.5",
    }
    
    try:
        proxy = random.choice(proxies)
        response = requests.get(URL, headers=headers, proxies=proxy, timeout=10)
        if response.status_code == 200:
            print("Request successful!")
            break
        else:
            print(f"Failed with status code: {response.status_code}, user agent {headers['User-Agent']}, and proxy: {proxy}")
    except requests.RequestError as e:
        print(f"Request error: {e}")
    time.sleep(random.randint(1, 5))  # Random delay between requests

if response.status_code != 200:
    print("Failed to retrieve data after maximum retries.")