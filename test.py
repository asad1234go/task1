import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from pyupdater.client import Client
from client_config import ClientConfig

APP_NAME = 'Super App'
ASSET_VERSION = '1.1'

#ASSET_NAME = 'ffmpeg'
#ASSET_VERSION = '2.3.2'

root = tk.Tk()
text = Text(root)
text.insert(INSERT, "Hello Version 1") 
f = open(r"C:Users\asad.elahi\AppData\Local\Programs\Python\Python39\Scripts\version.txt", "r")
APP_VERSION = f.readline()
if float(ASSET_VERSION) > float(APP_VERSION):    
    messagebox.showinfo('Software Update', 'Update Available!')
    mb1 = messagebox.askyesno('Update!', f'{__version__} needs to update to version {ASSET_VERSION}')
    if mb1 is True:        
        def print_status_info(info):            
            total = info.get(u'total')
            downloaded = info.get(u'downloaded')
            status = info.get(u'status')
        client = Client(ClientConfig())
        client.refresh()
        client.add_progress_hook(print_status_info)
        client = Client(
            ClientConfig(), refresh=True, progress_hooks=[print_status_info]
         )
        app_update = client.update_check(APP_NAME, APP_VERSION)
        if app_update is not None:
            app_update.download()
        if app_update.is_downloaded():
            app_update.extract_restart()
    else:
        text.insert(INSERT, "Hello Version 1")        
else:
    messagebox.showinfo("No update availble")


text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
root.mainloop()