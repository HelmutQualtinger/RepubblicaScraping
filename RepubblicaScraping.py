#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import json
# Funzione per creare l'hash di una stringa e aggiungerla a un insieme
import hashlib
import time
import datetime
import locale
import webbrowser
import urllib.parse
import pathlib as path


def time_now():
    """
    Returns the current date and time in Italian format.

    Returns:
        str: The current date and time in Italian format.
    """
    # Set the locale to Italian
    locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')
    # Get the current date and time
    now = datetime.datetime.now()
    # Format the date and time with Italian day and month names
    return now.strftime('%A, %d. %B %Y, ore %H:%M:%S')


def read_persistent_hash_set() -> set:
    """
    Reads the last run hash set from the 'last_run_hash.json' file.
    If the file doesn't exist or is empty, a new hash set is created.
    You cannot use the Python hash() function because it uses different random seeds at every run.

    Returns:
        last_run_hash_set (set): The last run hash set.
    """
    try:
        with open("last_run_hash.json", "r") as f:
            hash_list = json.load(f)
            last_run_hash_set = set(hash_list)
    except:
        print("Warning: No last run hash set found. Creating a new one.")
        last_run_hash_set = set()
    return last_run_hash_set


url = "https://www.repubblica.it/"


def read_webpage(url):
    """
    Reads the content of a webpage and returns the parsed HTML using BeautifulSoup.

    Parameters:
    url (str): The URL of the webpage to be read.

    Returns:
    BeautifulSoup: The parsed HTML of the webpage.
    """
    response = requests.get(url)
    webpage = response.content
    webpage_parsed = BeautifulSoup(webpage, "html.parser")
    return webpage_parsed


def analyse_webpage(webpage, hash_set):
    """
    Analyzes a webpage and extracts headers and paragraphs.

    Parameters:
    - webpage: BeautifulSoup object representing the webpage to be analyzed.
    - hash_set: Set containing the hash values of previously extracted content.

    Returns:
    A tuple containing the following information:
    - extracted_paragraphs: titles and links of the extracted titles.
    - hash_set: Updated set of hash values.
    """

    headers = webpage.find_all("h2")
    extracted_paragraphs = 0
    extracted_header = 0
    new_paragraphs = 0
    new_title = 0
    found_articles = []
    for header in headers:
        article = header.text
        try:
            extracted_header += 1
            # Assuming the text is stored in a variable called t
            t = " ".join(article.strip().split())
            hash_object = hashlib.sha1(t.encode('utf-8'))
            hash_value = hash_object.hexdigest()
            link_url = header.find("a").get("href")
            if not hash_value in hash_set:
                #                print( t)
                found_articles.append((t, link_url))
#                print("Link: ", link_url)
                # Set the hash_value in last_run_hash_set
                hash_set.add(hash_value)
                new_title += 1
        except:
            pass

    return (found_articles, hash_set)


def main():
    hash_set = read_persistent_hash_set()
    parsed_webpage = read_webpage(url)
    found_articles, hash_set = analyse_webpage( parsed_webpage, hash_set)
    with open("last_run_hash.json", "w") as f:
        json.dump(list(hash_set), f)
    print( time_now())
    for i,(article, link) in enumerate(found_articles):
        print(f"{i:>4}. {article} {link}")
 
 
    file_path = "repubblica.html"

       
    with open(file_path, "w") as f:
        f.write("<html>\n<head>\n<title>Articoli Nuovi della Repubblica</title>\n</head>\n<body>\n")
        f.write(f"<h1>Articoli Nuovi della Repubblica</h1>\n")
        f.write(f"<h2>{time_now()}</h2>\n<ol>")
        for i, (article, link) in enumerate(found_articles):
            f.write(f"<li><a href='{link}'>{article}</a></li>\n")
        f.write(",/<ol></body>\n</html>")


     # Open the file in a browser
    uri = path.Path(file_path).absolute()
    webbrowser.get().open(uri.as_uri())

if __name__ == "__main__":
    main()
