<h2>HTML Extractor</h2>
<br>
<code>import html_extractor</code>
<br>
<br>
<code>html_extractor.extract_html(website_link, character_encoding = 'utf-8')</code><br>
Use = Extracts the HTML from a website and returns it in a given encoding format<br>
Example:<br>
    <code>
    html_data = html_extractor.extraction('https://en.wikipedia.org/wiki/Python_(programming_language)')</code>
<br>
<br>
<code>
html_extractor.store_data(data, file_name = 'data.txt', file_location = current directory)</code>
Use = Stores data in a file by creating/overwriting it.<br>
Example:<br>
    <code>
    html_extractor.store_data(html_data, 'wiki_pythonProgramming.html')</code>
