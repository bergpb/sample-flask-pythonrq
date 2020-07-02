import requests
from bs4 import BeautifulSoup as bs4

import time


def count_words(url):
    print(f"Counting words at {url}")
    start = time.time()
    r = requests.get(url)
    soup = bs4(r.content.decode("utf-8"), "html.parser")
    paragraphs = " ".join([p.text for p in soup.find_all("p")])
    word_count = dict()

    for i in paragraphs.split():
        if not i in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1

    end = time.time()
    time_elapsed = end - start
    print(f"Total words: {len(word_count)}")
    print(f"Time elapsed: {time_elapsed} ms")

    time.sleep(5)

    return len(word_count)
