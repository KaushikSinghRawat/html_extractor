HTML Extractor
Extracts html from websites.

Usage = import html_extractor

Extract HTML from a given website:
Use = Extracts the HTML from a website and returns it in a given encoding format
Syntax = html_extractor.extraction(website_link, character_encoding = 'utf-8')
Example:
    html_data = html_extractor.extraction('https://en.wikipedia.org/wiki/Python_(programming_language)')


Store extracted data in a file:
Use = Stores data in a file by creating/overwriting it.
Syntax = html_extractor.store_data(data, file_name = 'data.txt', file_location = current directory)
Example:
    html_extractor.store_data(html_data, 'wiki_pythonProgramming.html')

