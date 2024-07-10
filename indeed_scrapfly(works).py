from contextlib import suppress
from dataclasses import dataclass
from pprint import pprint
from urllib.parse import urljoin
from typing import Optional
from parsel import Selector

from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse
import os

@dataclass
class Job:
    title: str
    company: str
    pay: Optional[str] = None
    easy_apply: Optional[bool] = None


scrapfly_key = os.environ.get("SCRAPFLY_API_KEY")
if scrapfly_key is None:
    raise ValueError("SCRAPFLY_KEY environment variable is not set")

scrapfly = ScrapflyClient(key=scrapfly_key)

api_response: ScrapeApiResponse = scrapfly.scrape(
    ScrapeConfig(
        url="https://www.indeed.com/jobs?q=python&l=Texas",
        render_js=True,
        asp=True,
    )
)

# Parsing function to extract job data from HTML response
def parse_jobs(scrape_api_response: ScrapeApiResponse):
    job_listings = []
    # Initialize the selector from the HTML content of the response
    selector = scrape_api_response.selector

    # Iterate over each job listing found
    for job in selector.css('div.job_seen_beacon'):
        title = job.css('h2.jobTitle a span[title]::attr(title)').get()
        company = job.css('div.css-1qv0295.e37uo190 span::text').get()
        pay = None

        if selector.css('div.mosaic-provider-jobcards-tvvxwd ecydgvn1'):
            pay = job.css('div.mosaic-provider-jobcards-tvvxwd ecydgvn1::text').get()
        elif selector.css('div.metadata.salary-snippet-container.css-5zy3wz.eu4oa1w0'):
            pay = job.css('div.metadata.salary-snippet-container.css-5zy3wz.eu4oa1w0 > div.css-1cvvo1b.eu4oa1w0::text').get()

        easy_apply = bool(job.css('.iaLabel').get())  # Checks if 'Easy Apply' label is present

        # Append the job data to the list
        job_listings.append(Job(title=title, company=company, pay=pay, easy_apply=easy_apply))

    return job_listings

# Extract jobs from the API response
jobs = parse_jobs(api_response)

# Display the parsed job information
for job in jobs:
    pprint(job.pay)