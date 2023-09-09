import html

replace_map={
    '&amp':'&',
    r'\"': '"'
    
    
}
with open('my_json_file.json', 'r', encoding='UTF-8') as fp:
    
    html_content=html.escape(fp.read())
    
    print(html_content.replace('&amp','&'))
    