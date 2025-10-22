import os
from datetime import datetime, date
from ftplib import FTP, error_perm
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import tkinter as tk


def connect_to_ftp():
    ftp = FTP()
    host_name = 'upd.inform44.ru'
    login = 'Inform'
    passwd = 'service'
    try:
        ftp.connect(host_name, 21)
        ftp.login(login, passwd)
        showinfo('FTP-Server', 'FTP Connect')
        return ftp
    except error_perm:
        showerror('FTP-Server', 'FTP FAIL')
        return None


def get_data_archive(arch):
    if len(arch.split('.')[2]) > 2:
        data_arch = datetime.strptime((arch.split('.')[0] + '-'
                                       + arch.split('.')[1] + '-'
                                       + arch.split('.')[2][:2]), '%Y-%m-%d').date()
    else:
        data_arch = datetime.strptime((arch.split('.')[0] + '-'
                                       + arch.split('.')[1] + '-'
                                       + arch.split('.')[2]), '%Y-%m-%d').date()
    return data_arch


def download_arch(arch, ftp):
    with open(arch, 'wb') as local_file:
        response = ftp.retrbinary(f'RETR {arch}', local_file.write)

    return response


def determining_date(path, file):
    data = datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file))).date()
    return data


def create_progressbar(master, val, max_val, row, column):
    progressbar = ttk.Progressbar(master,
                                  orient="horizontal", value=val, maximum=max_val)
    progressbar.grid(row=row, column=column)
    return progressbar


def create_children_window(name):
    children_window = tk.Toplevel()
    children_window.title(f'{name}')
    children_window.geometry('300x300+800+300')
    children_window.grid_columnconfigure(0, weight=1)
    return children_window
