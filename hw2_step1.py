import pandas as pd
import praw
import re
import requests
import time 
import json
import numpy as np

CLIENT_ID = "Yew9qy_Emf2ltiSuOqjiEQ"
CLIENT_SECRET = "wjbSF31tGZSE0J5qbzr-bIXeLnKXew"
USER_AGENT = "sommer-clarku"

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT 
)

urls = []
for thread in reddit.subreddit('nbl').hot(limit=50):
    url = thread.url
    if re.search('www.reddit.com/r/', url):
        urls.append(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0'
}

with open('reddit.json', 'w+') as fp:
    for url in urls:
        try:
            response = requests.get(url + ".json", timeout=10, \
                                    headers = headers)
            json_data = response.json()
            if (len(json_data) >= 2):
                jstr = json.dumps(json_data)
                fp.write(jstr + '\n')
            time.sleep(np.random.uniform(1, 5))
            print(f"Successfully fetching {url}")
            
        except Exception as e:
            print(e)
            print(f"Error fetching {url}")


with open('reddit.json', 'r+') as fp:
    lines = fp.readlines()

print(len(lines))