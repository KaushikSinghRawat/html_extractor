<h2>HTML Extractor</h2>
<br>
<code>import html_extractor</code>
<br>
<br>
Extract html from link and return it in a given encoding format:<br>
Syntax: <code>html_extractor.extract_html(website_link, character_encoding = 'utf-8')</code><br>
Example: <code>html_data = html_extractor.extraction('https://en.wikipedia.org/wiki/Python_(programming_language)')</code>
<br>
<br>
Store data in a file by creating/overwriting it:<br>
Syntax: <code>html_extractor.store_data(data, file_name = 'data.txt', file_location = current directory)</code><br>
Example: <code>html_extractor.store_data(html_data, 'wiki_pythonProgramming.html')</code>
