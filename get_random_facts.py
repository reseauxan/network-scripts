#!/usr/bin/env python

"""
Author: Khalid Mouss
Purpose: The script will request the public API in order to get a random fact.
Next, the script have to store the data obtained in a file called "random_acts.txt"
"""

import requests


def get_api_data():
    """function to help get random facts from the public APIs"""
    api_path = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    # auth = ("user", "pass")
    headers = {"Content-Type": "application/json"}
    resp = None

    # Issue HTTP GET request to the proper URL to request data,
    # Added timeout after remarks from Pylint.
    try:
        resp = requests.get(
            f"{api_path}", headers=headers, verify=False, timeout=10
        )
    except requests.exceptions.Timeout:
        print("Timeout")

    # If successful, print data obtained. Else, raise HTTPError with details
    resp.raise_for_status()
    data = resp.json()["text"]
    return data


def main():
    """function to HELP EXECUTE THE CODE WHEN CALLED FROM CLI"""
    # ran_fact = get_api_data()
    # print(ran_fact)
    i = 0
    while i < 10:
        random_fact = get_api_data()
        with open("ran_facts_a.txt", "a", encoding="utf-8") as randoms_file:
            randoms_file.write(random_fact)
        i = i + 1

    with open("ran_facts_a.txt", "r", encoding="utf-8") as randoms_file:
        contents = randoms_file.readlines()

    for line in contents:
        print(line)


if __name__ == "__main__":
    main()
