import os


from rich.console import Console
from rich.progress import track
from rich.theme import Theme
import time
import json
from lxml import etree

#import xmltodict
#import pandas as pd
#import html


"""
This script searches for memo files in a specific folder in a Linux system, extracts content from their "memo_content.xml" files, and writes it to a JSON file named "my_json_file.json".

The process involves the following steps:
- Determine the operating system the script is running on.
- Search for a specific folder called "SharedMemocellphone".
- Traverse this folder to find individual memo files.
- Extract content from the "memo_content.xml" file of each memo file found.
- Write the extracted content to a JSON file named "my_json_file.json".

This script uses the following third-party libraries:
- os: provides a way to interact with the operating system.
- rich: provides a way to add color and formatting to terminal output.
- time: provides a way to track the script's execution time.
- json: provides a way to work with JSON data.
- lxml: provides a way to work with XML data.

"""
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)


def determine_os():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    base_os = os.uname()[0]
    return base_os


def find_folder():
    # initial_time = datetime.datetime.now
    base_os = determine_os()

    if base_os == 'Linux':
        console.rule()
        console.print("you're on a linux system.", style='info')
        for (root, dirs, files) in track(os.walk('/', topdown=True), description='searching directories'):

            if 'SharedMemocellphone' in dirs:
                console.rule()
                console.print(
                    'folder found, moving to ShareMemocellphone folder')
                os.chdir(os.path.join(root, dirs[0]))
                console.rule()

                break
    found_folder = os.getcwd()
    console.print('folder successfully found at', os.getcwd(), style='info')
    console.rule()

    return found_folder


def find_memo_folder(found_folder):
    print(found_folder)
    memo_folders = []
    for (root, dirs, files) in track(os.walk(found_folder, topdown=True), description='searching for memo files in internal folders'):

        for dir in dirs:

            if 'Memo_20210615' in str(dir):
                console.print('individual memo files found ')

                os.chdir(os.path.join(root, dir))
                memo_folder = os.getcwd()

                memo_folders.append(memo_folder)

    return memo_folders


def process_xml_file(memo_folders):
    xml_string = []
    for folder in memo_folders:

        os.chdir(folder)

        for files in os.listdir(folder):

            if 'memo_content.xml' in files:
                with open('memo_content.xml', 'r', encoding='utf-8') as xml_file:
                    xml_doc = xml_file.read()
                    xml_string.append(xml_doc)
                    
    print(len(xml_string))
    return xml_string


def transform_xml(xml_string):
    print(xml_string)

    xml_string = json.dumps(xml_string)

    for (root, dirs, files) in os.walk('/', topdown=True):
       if 'os_automation' in dirs:
          

           os.chdir(os.path.join(root, dirs[21]))#keep in mind that the index of the directory can change if you add more projects
           
           print(dirs)

           with open('my_json_file.json', 'w', encoding='utf-8') as my_file:
               my_file.seek(0)
               my_file.write((xml_string)
                             )
               print('json file successfully created')
               print(os.getcwd())
   

#found_folder = find_folder()
#memo_folders = find_memo_folder(found_folder)
#xml_file = process_xml_file(memo_folders)
#xml_file = transform_xml(xml_file)

os.system('clear')
complexity, _ = big-O(process_xml_file, lambda n: [
                      f"Memo_{i}" for i in range(n)], min_n=1, max_n=1000, verbose=False)
print("Time complexity:", complexity)



