"""
-This file organizes files from the downloads folder into separate folders in the system, based on file extensions
t
"""
__author__ = 'Sergio Andrés Herrera Velásquez'





# standard library imports
import shutil
import os


#file extensions


## Text file extensions
text_extensions = ['.txt', '.doc', '.docx', '.pdf', '.html', '.csv']

## Image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

## Audio file extensions
audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma']

## Video file extensions
video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv']

#Directories
## home directory
###used os.scandir instead of os.listdir  as per documentation states:
###The scandir() function returns directory entries along with file attribute information, 
###giving better performance for many common use cases.

with os.scandir(os.path.join(os.path.expanduser('~'), 'Downloads')) as files:
  #one workaround for the differences for home 
  
#loop through the directory  
    for entry in files:
        ## destination folders for the filetypes-audio, video,document, image
        text_dir = os.path.join(os.path.expanduser('~'), 'Documents')
        image_dir = os.path.join(os.path.expanduser('~'), 'Pictures')
        audio_dir = os.path.join(os.path.expanduser('~'), 'Music')
        video_dir = os.path.join(os.path.expanduser('~'), 'Videos')
      
#checking that there are no .
        if not entry.name.startswith('.') and entry.is_file:
          #splitting the entire entry.name into name and extension
            entry_name, entry_ext = os.path.splitext(entry.name)
          
            if entry_ext in text_extensions:
                shutil.move(os.path.join(os.path.expanduser('~'), 'Downloads', entry.name), os.path.join(text_dir, entry.name))
            elif entry_ext in image_extensions:
                shutil.move(os.path.join(os.path.expanduser(
                    '~'), 'Downloads', entry.name), os.path.join(image_dir, entry.name))
            elif entry_ext in audio_extensions:
                shutil.move(os.path.join(os.path.expanduser('~'), 'Downloads', entry.name), os.path.join(audio_dir, entry.name))
            elif entry_ext in video_extensions:
                shutil.move(os.path.join(os.path.expanduser(~'), 'Downloads', entry.name), os.path.join(video_dir, entry.name))
