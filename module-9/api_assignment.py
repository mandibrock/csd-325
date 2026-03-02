# ----------------------------------------------
# Author: Amanda Brock
# Date: March 1, 2026
# Assignment: Module 9.2
# Purpose: Practice working with APIs in Python.
# ----------------------------------------------

import requests
import json


def test_connection(url):
    # Tests a URL and prints the HTTP status code.
    response = requests.get(url, timeout=10)
    print("Status Code:", response.status_code)
    return response


def tutorial_connection_test():
    # Tests the connection to the API tutorial page
    url = "https://www.dataquest.io/blog/api-in-python/"
    print("\nAPI Tutorial Connection Test")
    print("URL:", url)
    test_connection(url)


def astronauts_demo():
    # Retrieves current astronauts and prints them
    url = "http://api.open-notify.org/astros.json"

    print("\nCurrent Astronauts (Tutorial Part)")
    print("URL:", url)

    # Test connection first
    response = test_connection(url)

    # Raw response (no formatting)
    print("\nRaw Response:")
    print(response.text)

    # Formatted response (pretty JSON)
    data = response.json()
    print("\nFormatted JSON:")
    print(json.dumps(data, indent=2))

    # Clean output
    print("\nAstronaut List:")
    print("Total astronauts:", data.get("number"))
    for person in data.get("people", []):
        print(f"- {person.get('name')} ({person.get('craft')})")


def simple_api_demo():
    # Simple API of choice: Joke API
    url = "https://official-joke-api.appspot.com/random_joke"

    print("\nSimple API Demo (My Chosen API)")
    print("API Used: Official Joke API")
    print("URL:", url)

    # Test connection first
    response = test_connection(url)

    # Raw response (no formatting)
    print("\nRaw Response:")
    print(response.text)

    # Formatted response (pretty JSON)
    data = response.json()
    print("\nFormatted JSON:")
    print(json.dumps(data, indent=2))

    # Clean output
    print("\nJoke:")
    print(data.get("setup"))
    print(data.get("punchline"))


def main():
    print("Module 9 API Assignment Output")

    # Test the connection to the tutorial URL
    tutorial_connection_test()

    # Tutorial portion: astronauts + formatting output
    astronauts_demo()

    # Chosen API: connection test + raw + formatted output
    simple_api_demo()


if __name__ == "__main__":
    main()