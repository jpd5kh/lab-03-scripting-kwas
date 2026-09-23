#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

print(GHUSER)
print(url)

def retrieve_events(url):
	"This function downloads event data from a GitHub account and returns it as a Python object."
	data = requests.get(url).text
	events = json.loads(data)
	return events

def print_events(events, n=5):
	"This function loops over the events from the GitHub account and prints it into a readable format."
	for x in events[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)

def main():
	user = GHUSER
	github_url = url
	returned_list = retrieve_events(url)
	final_list = print_events(returned_list, n=5)

if __name__ == "__main__":
	main()
