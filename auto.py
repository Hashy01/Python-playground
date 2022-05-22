import os
import sys
import time
import logging
import shutil
from os.path import splitext, exists
from os import scandir, rename
from shutil import move
from time import sleep

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


source_dir = "/Users/user/Downloads" #download folder location
dest_dir_sfx = "/Users/user/Desktop/Downloads/Sounds" # Sounds
dest_dir_music = "/Users/user/Desktop/Downloads/Sounds/Music" #Music
dest_dir_video = "/Users/user/Desktop/Downloads/Downloaded Videos" # videos
dest_dir_image= "/Users/user/Desktop/Downloads/Downloaded Images" 

with os.scandir(source_dir) as entries: # os.scandir() returns an iterator of all objects in a directory
    for entry in entries:  # run for each object in that list
        print(entry.name) # prints name of all files in the downloads folder

def make_unique(path):
    filename, extension = splitext(path)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(path):
        path = f"{filename} ({counter}){extension}"
        counter += 1

    return path



def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = make_unique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)

class MoverEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000:
                        dest = dest_dir_sfx
                    else:
                        dest = dest_dir_music
                    move(dest, entry, name)
                elif name.endswith('.mov') or name.endswith('.mp4'):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png') or name.endswith('.HEIC'):
                    dest = dest_dir_image
                    move(dest, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverEventHandler() ## instance of class
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()