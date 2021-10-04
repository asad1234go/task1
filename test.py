import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from pyupdater.client import Client,AppUpdate, LibUpdate
from client_config import ClientConfig

APP_NAME = 'Super App'
ASSET_VERSION = '1.2'
root = tk.Tk()
text = Text(root)
f = open("ver.txt", "r")
APP_VERSION = f.read().replace("\n","").strip()
f.close()
if float(APP_VERSION) > float(ASSET_VERSION):    
    messagebox.showinfo('Software Update', 'Update Available!')
    mb1 = messagebox.askyesno('Update!', f'needs to update to version {APP_VERSION}')
    if mb1 is True:        
        def print_status_info(info):            
            total = info.get(u'total')
            downloaded = info.get(u'downloaded')
            status = info.get(u'status')
            print(downloaded, total, status)

        client = Client(ClientConfig())
        #client.refresh()
        client.add_progress_hook(print_status_info)
        client = Client(
            ClientConfig(), refresh=False, progress_hooks=[print_status_info]
         )
        app_update = client.update_check(APP_NAME, ASSET_VERSION)
        if app_update is not None:
            app_update.download()
        if isinstance(app_update, AppUpdate):
                app_update.extract_restart()
    else:
        text.insert(INSERT, "Hello Version 2")        
else:
    messagebox.showinfo("No update availble")


text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
root.mainloop()