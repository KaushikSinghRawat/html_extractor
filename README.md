Usage = import html_extractor<br>
<br>
Extract HTML from a given website:<br>
Use = Extracts the HTML from a website and returns it in a given encoding format<br>
Syntax = html_extractor.extraction(website_link, character_encoding = 'utf-8')<br>
Example:<br>
    html_data = html_extractor.extraction('https://en.wikipedia.org/wiki/Python_(programming_language)')<br>
<br>
<br>
Store extracted data in a file:<br>
Use = Stores data in a file by creating/overwriting it.<br>
Syntax = html_extractor.store_data(data, file_name = 'data.txt', file_location = current directory)<br>
Example:<br>
    html_extractor.store_data(html_data, 'wiki_pythonProgramming.html')<br>
