#!/usr/bin/env python3

import getpodcast
import re
import requests

def get_podcast_url_apple(podcast_url):
    re_pattern = re.compile(r'[^w]+/id(\d+)')
    matches = re_pattern.search(podcast_url)
    if not matches:
        return None
    id = matches.group(1)
    url = f"https://itunes.apple.com/lookup?id={id}&entity=podcast"
    response = requests.get(url)
    response.raise_for_status() 

    data = response.json()
    results = data.get('results', [])

    if results:
        return results[0].get('feedUrl')
    else:
        return None

opt = getpodcast.options(
    date_from='2024-01-05',
    root_dir='./podcast')

podcasts = {
    # "Big Technology Podcast": "https://podcasts.apple.com/us/podcast/big-technology-podcast/id1522960417",
    # "Modern Wisdom": "https://feeds.megaphone.fm/SIXMSB5088139739",
    # "Hard Fork": "https://feeds.simplecast.com/l2i9YnTd",
    # "The AI Breakdown": "https://podcasts.apple.com/us/podcast/the-ai-breakdown-daily-artificial-intelligence-news/id1680633614",
    # "The Cognitive Revolution": "https://podcasts.apple.com/us/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431",
    "MLOps.community": "https://podcasts.apple.com/us/podcast/mlops-community/id1505372978"
}

for name, url in podcasts.items():
    if url.startswith('https://podcasts.apple.com'):
        new_url = get_podcast_url_apple(url)
        if new_url:
            print(f'INFO: Found XML URL for apple podcast: {name}: {new_url}')
            podcasts[name] = new_url
        else:
            print(f'WARNING: could not determine URL for apple podcast: {name}, {url}')

getpodcast.getpodcast(podcasts, opt)
