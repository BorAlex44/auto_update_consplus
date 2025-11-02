import os
from datetime import datetime, timedelta
from base_app import create_progressbar, create_children_window, get_data_archive
from pathlib import Path
from tkinter.messagebox import showinfo
import tkinter.filedialog as fd
import tkinter as tk


def delete_old_archives(children_delete_old_archives,
                        letter_path, button_star_delete):
    path_delete_old_archives = Path(f'{letter_path["text"]}')
    data_delete = (datetime.now() - timedelta(30)).date()
    button_star_delete.destroy()
    count = 0
    max_len = len(os.listdir(path_delete_old_archives))
    progressbar_copy_updates = create_progressbar(
        children_delete_old_archives,
        count, max_len, 2, 0)
    for file in os.listdir(path_delete_old_archives):
        data_file = get_data_archive(file)
        if data_file < data_delete:
            os.remove(os.path.join(path_delete_old_archives, file))
        count += 1
        progressbar_copy_updates['value'] = count
        progressbar_copy_updates.update()
    showinfo('Удаление', 'Удаление завершено')
    children_delete_old_archives.destroy()


def path_copy(label, button, row):
    directory = fd.askdirectory(title="Выбор папки", initialdir="/")
    if directory:
        button.destroy()
        label['text'] = directory
        label.grid(row=row, column=0, padx=20, pady=5)


def start_delete_old_archives():
    children_delete_old_archives = create_children_window('Удаление старых архивов')
    letter_path = tk.Label(children_delete_old_archives,
                           text='Выбор директории',
                           font='Calibri 13 bold')
    letter_path.grid(row=0, column=0)

    children_delete_old_archives.update()
    button_set_path = tk.Button(children_delete_old_archives, text='Задать',
                                font='Calibri 15 bold', width=30, height=1,
                                command=lambda:
                                path_copy(letter_path, button_set_path, 0))
    button_star_delete = tk.Button(children_delete_old_archives, text='Начать удаление',
                                   font='Calibri 13 bold',
                                   width=30, height=1,
                                   command=lambda: delete_old_archives(children_delete_old_archives,
                                                                       letter_path,
                                                                       button_star_delete))
    button_star_delete.grid(row=4, column=0, padx=20, pady=5)

    button_set_path.grid(row=3, column=0, padx=20, pady=5)
    children_delete_old_archives.update()
