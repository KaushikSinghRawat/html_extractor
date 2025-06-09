from requests import get

def html_request(link_address):
    return get(link_address).content


link_address = "https://en.wikipedia.org/wiki/Python_(programming_language)" #link from whom html is to be extracted

request = html_request(link_address)
