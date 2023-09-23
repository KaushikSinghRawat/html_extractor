from requests import get

def html_request(link_address):
    return get(link_address).content


link_address = "https://en.m.wikipedia.org/wiki/List_of_space_travellers_by_first_flight#Table" #link from whom html is to be extracted

request = html_request(link_address)
