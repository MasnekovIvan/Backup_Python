import os
import time
import zipfile

# 1. Files and folders that need to be copied adds to list
source = 'C:\\Users\\ohtha\\Documents\\Programming\\Python'

# 2. Archived copies at that path
target_dir = 'C:\\Backup'

# Create folder if doesn`t exist
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # create
    print('Folder created!')

# 3. Add files and folders to zip-achieve
# 4. Current date use as folder name
today = target_dir + os.sep + time.strftime('%d%m%Y')

# current time for zip-file name
now = time.strftime('%H%M%S')

# User comment input
comment = input('Add comment ->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

# Create folder if doesn`t exist
if not os.path.exists(today):
    os.mkdir(today)
    print('Folder created!')

zipp = zipfile.ZipFile(target, mode='w')
for root, dirs, files in os.walk(source):
    for file in files:
        zipp.write(os.path.join(root, file))

zipp.close()
