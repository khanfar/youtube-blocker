import tkinter as tk
from tkinter import messagebox
import os
import shutil

# Path to the hosts file
HOSTS_FILE_PATH = r'C:\Windows\System32\drivers\etc\hosts'

# Entries to block YouTube
YOUTUBE_ENTRIES = [
    '127.0.0.1 youtube.com\n',
    '127.0.0.1 www.youtube.com\n'
]

def backup_hosts_file():
    if not os.path.exists(HOSTS_FILE_PATH + ".bak"):
        shutil.copy(HOSTS_FILE_PATH, HOSTS_FILE_PATH + ".bak")

def block_youtube():
    try:
        backup_hosts_file()
        with open(HOSTS_FILE_PATH, 'a') as hosts_file:
            hosts_file.writelines(YOUTUBE_ENTRIES)
        messagebox.showinfo("Success", "YouTube has been blocked!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def unblock_youtube():
    try:
        with open(HOSTS_FILE_PATH, 'r') as hosts_file:
            lines = hosts_file.readlines()
        with open(HOSTS_FILE_PATH, 'w') as hosts_file:
            for line in lines:
                if line not in YOUTUBE_ENTRIES:
                    hosts_file.write(line)
        messagebox.showinfo("Success", "YouTube has been unblocked!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def restore_hosts_file():
    try:
        if os.path.exists(HOSTS_FILE_PATH + ".bak"):
            shutil.copy(HOSTS_FILE_PATH + ".bak", HOSTS_FILE_PATH)
            messagebox.showinfo("Success", "Hosts file has been restored from backup!")
        else:
            messagebox.showwarning("Warning", "No backup found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("YouTube Blocker")
root.geometry("300x200")

# Create and place buttons
block_button = tk.Button(root, text="Block YouTube", command=block_youtube)
block_button.pack(pady=10)

unblock_button = tk.Button(root, text="Unblock YouTube", command=unblock_youtube)
unblock_button.pack(pady=10)

restore_button = tk.Button(root, text="Restore Hosts File", command=restore_hosts_file)
restore_button.pack(pady=10)

# Run the main event loop
root.mainloop()
