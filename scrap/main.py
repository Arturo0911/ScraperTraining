#!/usr/bin/python

import requests
import lxml.html as html
from pprint import pprint

# constants defined
HOME_URL = "https://www.larepublica.co"

XPATH_LINK_TO_ARTICLE = '//div[contains(@class, "V")]/a[contains(@class, "kicker")]/@href'
#XPATH_LINK_TO_ARTICLE = '//h2[@class="headline"]/a/@href'
XPATH_TITLE = '//h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            # response.content html document from the response
            home = response.content.decode('utf-8')

            # take the html content in home as text and transform in
            # special document to do xpath
            parsed = html.fromstring(home)

            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            pprint(links_to_notices)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(str(ve))

def run():
    parse_home()



if __name__ == '__main__':
    run()
