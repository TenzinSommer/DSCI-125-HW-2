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

# CLIENT_ID = "OKi0keVw1m4blsktPESl-A"
# CLIENT_SECRET = "4WQMoXYrGgMtPH8kNiepiMS7CD8y8w"
# USER_AGENT = "IllDevelopment7829"

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT 
)

urls = []

for thread in reddit.subreddit('redsox').top(time_filter="all", limit=150):
	url = thread.url
	if re.search('www.reddit.com/r/', url):
		urls.append(url)

headers = {
	# Tenzin
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0' 

	# Elliot
	# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15"
}

counter = 1
filename = 'redsox.json'

with open(filename, 'w+') as fp:
	for url in urls:
		# print(time.time())
		try:
			response = requests.get(url + ".json", timeout=10, headers = headers)
			json_data = response.json()
			if (len(json_data) >= 2):
				jstr = json.dumps(json_data)
				fp.write(jstr + '\n')
			time.sleep(10)
			print(f"{counter}: Successfully fetching {url}")
			
		except Exception as e:
			print(f"{counter}: Error fetching {url}")
			print(e)

		counter += 1

urls.clear()

for thread in reddit.subreddit('nyyankees').top(time_filter="all", limit=150):
	url = thread.url
	if re.search('www.reddit.com/r/', url):
		urls.append(url)

counter = 1
filename = 'yankees.json'

with open(filename, 'w+') as fp:
	for url in urls:
		# print(time.time())
		try:
			response = requests.get(url + ".json", timeout=10, headers = headers)
			json_data = response.json()
			if (len(json_data) >= 2):
				jstr = json.dumps(json_data)
				fp.write(jstr + '\n')
			time.sleep(10)
			print(f"{counter}: Successfully fetching {url}")
			
		except Exception as e:
			print(f"{counter}: Error fetching {url}")
			print(e)

		counter += 1

urls.clear()

for thread in reddit.subreddit('orioles').top(time_filter="all", limit=150):
	url = thread.url
	if re.search('www.reddit.com/r/', url):
		urls.append(url)

counter = 1
filename = 'orioles.json'

with open(filename, 'w+') as fp:
	for url in urls:
		# print(time.time())
		try:
			response = requests.get(url + ".json", timeout=10, headers = headers)
			json_data = response.json()
			if (len(json_data) >= 2):
				jstr = json.dumps(json_data)
				fp.write(jstr + '\n')
			time.sleep(10)
			print(f"{counter}: Successfully fetching {url}")
			
		except Exception as e:
			print(f"{counter}: Error fetching {url}")
			print(e)

		counter += 1

urls.clear()

for thread in reddit.subreddit('torontobluejays').top(time_filter="all", limit=150):
	url = thread.url
	if re.search('www.reddit.com/r/', url):
		urls.append(url)

counter = 1
filename = 'torontobluejays.json'

with open(filename, 'w+') as fp:
	for url in urls:
		# print(time.time())
		try:
			response = requests.get(url + ".json", timeout=10, headers = headers)
			json_data = response.json()
			if (len(json_data) >= 2):
				jstr = json.dumps(json_data)
				fp.write(jstr + '\n')
			time.sleep(10)
			print(f"{counter}: Successfully fetching {url}")
			
		except Exception as e:
			print(f"{counter}: Error fetching {url}")
			print(e)

		counter += 1

urls.clear()

for thread in reddit.subreddit('tampabayrays').top(time_filter="all", limit=150):
	url = thread.url
	if re.search('www.reddit.com/r/', url):
		urls.append(url)

counter = 1
filename = 'tampabayrays.json'

with open(filename, 'w+') as fp:
	for url in urls:
		# print(time.time())
		try:
			response = requests.get(url + ".json", timeout=10, headers = headers)
			json_data = response.json()
			if (len(json_data) >= 2):
				jstr = json.dumps(json_data)
				fp.write(jstr + '\n')
			time.sleep(10)
			print(f"{counter}: Successfully fetching {url}")
			
		except Exception as e:
			print(f"{counter}: Error fetching {url}")
			print(e)

		counter += 1

urls.clear()

df = pd.read_csv('games.csv')

# Fix date format
df['Date'] = df['Date'].apply(lambda x: str.split(x,'T')[0])
df['Date']

# Remove games with no AL East teams
teamIDs = ['BOS','TOR','TB','NYY','BAL']
df = df.loc[(df['home'].apply(lambda x: x in teamIDs) | df['away'].apply(lambda x: x in teamIDs))]

# Trim unnecessary columns
df = df.drop(columns=df.columns[24:], axis=1)
df = df.drop(columns=['Walks Issued - Away', 
					  'Walks Issued - Home', 
					  'Stolen Bases - Away', 
					  'Stolen Bases - Home', 
					  'Strikeouts Thrown - Away', 
					  'Strikeouts Thrown - Home',
					  'Total Bases - Away', 
					  'Total Bases - Home',
					  'Stadium',
					  'Location'])

