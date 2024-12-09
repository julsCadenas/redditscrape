#!/usr/bin/env python
from summarize import Summarize
from scrape import  Scrape

def main():
    scraper = Scrape()
    summarize = Summarize()
    
    scraper.authenticate()
    post_link = 'https://www.reddit.com/r/AskPH/comments/16k5u2w/budget_friendly_yet_reliable_wireless_earbuds/'
    response = scraper.fetch_post(post_link)
    summary = summarize.process_data(response, "Summarize and highlight popular brands")
    
    print("Post Summary:", summary["post_summary"])
    print("Comments Summary:", summary["comments_summary"])

if __name__ == "__main__":
    main()