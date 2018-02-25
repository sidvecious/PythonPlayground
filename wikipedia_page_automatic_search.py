#@ Autor: Lorenzo Olivier
#@ Date: 09-15-2017

import time
import urlparse #in python 3 urllib
import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Logic"

def find_first_link(url):
    response = requests.get(url)
    html = response.text.encode("utf-8")
    soup = bs4.BeautifulSoup(html, "html.parser")

    # Div contains the article's body
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urlparse.urljoin('https://en.wikipedia.org/', article_link)
    #in python 3 urllib.parse instead of urlparse
    return first_link

def continue_crawl(search_history, target_url, max_steps=20):
    ''' keep looking for the target url until it finds it 
    or does not reach 20 attempts, or come back to a page you have already visited '''
    if search_history[-1] == target_url:
        print(search_history[-1])
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True

article_chain = [start_url]

# the search starts with a random url,
# if this url does not contain a first useful link,
# the search is aborted     
while continue_crawl(article_chain, target_url):
    print(article_chain[-1])
    first_link = find_first_link(article_chain[-1]) 
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2) # Slow things down so as to not hammer Wikipedia's servers