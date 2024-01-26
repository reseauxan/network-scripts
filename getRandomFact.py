#!/usr/bin/env python

"""
Author: Khalid Mouss
Purpose: The script will request the public API in order to get a random fact.
Next, the script have to store the data obtained in a file called "random_acts.txt"
"""

import requests


def get_api_data():
	api_path = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
	# auth = ("user", "pass")
	headers = {"Content-Type": "application/json"}

	# Issue HTTP GET request to the proper URL to request data
	resp = requests.get(
		f"{api_path}", headers=headers, verify=False
	)

	# If successful, print data obtained. Else, raise HTTPError with details
	resp.raise_for_status()
	data = resp.json()["text"]
	return data


def main():
	# ran_fact = get_api_data()
	# print(ran_fact)
	i = 0
	filex = open("ran_facts_a.txt", "a")
	while i < 10:
		rf = get_api_data()
		filex.write(rf + "\n")
		i = i + 1

	filex.close()

	filex = open("ran_facts_a.txt", "r")
	content = filex.readlines()
	# print(content)
	filex.close()

	for line in content:
		print(line)


if __name__ == "__main__":
	main()
