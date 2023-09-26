##HTML Extractor
 
'''python
import html_extractor
'''

<br>
'''python
html_extractor.extract_html(website_link, character_encoding = 'utf-8')'''
Use = Extracts the HTML from a website and returns it in a given encoding format<br>
<br>
Example:<br>
    '''python
    html_data = html_extractor.extraction('https://en.wikipedia.org/wiki/Python_(programming_language)')'''


'''python
html_extractor.store_data(data, file_name = 'data.txt', file_location = current directory)'''
Use = Stores data in a file by creating/overwriting it.<br>
<br>
Example:<br>
    '''python
    html_extractor.store_data(html_data, 'wiki_pythonProgramming.html')'''
