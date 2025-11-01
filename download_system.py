import os
from datetime import datetime, timedelta

from base_app import create_progressbar, create_children_window, get_data_archive, connect_to_ftp, download_arch
from pathlib import Path
from tkinter.messagebox import showinfo, showerror
import tkinter.filedialog as fd
import tkinter as tk


def download_new_system(children_download_new_system,
                        letter_path, button_star_download_new_system):
    button_star_download_new_system.destroy()
    process_label = tk.Label(children_download_new_system,
                             text='Идет скачивание папки system',
                             font='Calibri 13 bold')
    process_label.grid(row=2, column=0, padx=20, pady=5)
    ftp_server = connect_to_ftp()
    path_download_new_system = Path(f'{letter_path["text"]}')
    path_dir_system_on_ftp = 'updates//SYSTEM'
    os.chdir(path_download_new_system)

    if ftp_server:

        ftp_server.cwd(path_dir_system_on_ftp)
        arh_download_system = ftp_server.nlst()[-1]
        response = download_arch(arh_download_system, ftp_server)
        if response.startswith('226'):  # Transfer complete
            showinfo('Результат', 'Скачан новый каталог system')
        else:
            showerror('Результат', 'Ошибка.Новый каталог system не скачан')
    children_download_new_system.destroy()


def path_copy(label, button, row):
    directory = fd.askdirectory(title="Выбор папки", initialdir="/")
    if directory:
        button.destroy()
        label['text'] = directory
        label.grid(row=row, column=0, padx=20, pady=5)


def start_download_new_system():
    children_download_new_system = create_children_window('Скачивание папки system')
    letter_path = tk.Label(children_download_new_system,
                           text='Выбор директории',
                           font='Calibri 13 bold')
    letter_path.grid(row=0, column=0)

    children_download_new_system.update()
    button_set_path = tk.Button(children_download_new_system, text='Задать',
                                font='Calibri 15 bold', width=30, height=1,
                                command=lambda:
                                path_copy(letter_path, button_set_path, 0))
    button_star_download_new_system = tk.Button(children_download_new_system, text='Начать загрузку',
                                                font='Calibri 13 bold',
                                                width=30, height=1,
                                                command=lambda:
                                                download_new_system(children_download_new_system,
                                                                    letter_path,
                                                                    button_star_download_new_system))
    button_star_download_new_system.grid(row=4, column=0, padx=20, pady=5)

    button_set_path.grid(row=3, column=0, padx=20, pady=5)
    children_download_new_system.update()
