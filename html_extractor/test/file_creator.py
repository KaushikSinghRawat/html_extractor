from html_extractor.request_maker.html_request import request

def file_creator(request, file_location = 'data_file_creator', file_name = 'new_data.txt', character_encoding = 'utf-8'):
    with open(f'{file_location}/{file_name}', 'w') as file:
        file.write(request.decode(character_encoding))


file_name = 'astronauts_in_space.html' #name of file to be created | default = 'new_data.txt'
file_location = 'html_extractor/request_maker' #location to store created data file | default = current directory
character_encoding = 'utf-8' #character encoding for .decode() | default = utf-8

file_creator(request, file_location, file_name, character_encoding)
