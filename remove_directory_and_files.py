import shutil
import shutil
import os

home_dir = os.path.expanduser("~")
location = "Documents"

dir = 'NOtes'


path = os.path.join(home_dir,location, dir)
#remove files
shutil.rmtree(path)
