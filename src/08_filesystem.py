# Download a file from any URL and print its' filesystem attributes in a human-readable form.
# If it hasn't been modified for more than 1 minute, reload it.

import os, os.path, stat, time, urllib.request

url = 'http://stackoverflow.com/questions/7162164/does-windows-have-inode-numbers-like-linux'
filepath = 'resources/stackoverflow_inode_numbers.html'

if (not os.path.isfile(filepath) or time.time() - os.stat(filepath).st_mtime > 60): # 1 minute
    print ('Updating file...')
    opener = urllib.request.FancyURLopener({})
    f = opener.open(url)
    content = f.read()
    with open(filepath, 'wb') as fout:
        fout.write(content)

statinfo = os.stat(filepath)

print ('Inode protection mode: {}'.format(stat.filemode(statinfo.st_mode)))
print ('Inode number: {}'.format(statinfo.st_ino))
print ('Inode device: {}'.format(statinfo.st_dev))
print ('Links to inode: {}'.format(statinfo.st_nlink))
print ('Owner UID: {}'.format(statinfo.st_uid))
print ('Owner group ID: {}'.format(statinfo.st_gid))
print ('Size (in bytes): {}'.format(statinfo.st_size))
print ('Time of last access: {}'.format(time.ctime(statinfo.st_atime)))
print ('Time of last modification: {}'.format(time.ctime(statinfo.st_mtime)))
print ('Time of creation: {}'.format(time.ctime(statinfo.st_ctime)))
