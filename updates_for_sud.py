import os
import shutil
import tkinter as tk
import tkinter.filedialog as fd
from datetime import datetime, timedelta
from pathlib import Path
from tkinter.messagebox import showinfo

from base_app import create_children_window, determining_date, create_progressbar


def updates_for_sud(children_window_updates_for_sud, label_where_from, label_where, button_star_copy):
    base_names = ['ARB', 'CJI', 'CMB', 'DOF', 'INT', 'LAW', 'OTN', 'PDR', 'PGU', 'PKG', 'PKP',
                  'PKS', 'PPVS', 'PSG', 'PSP', 'PTS', 'QSOV', 'REXP265', 'RGSS', 'RLAW265', 'SIP', 'SOCN',
                  'SODV', 'SOPV', 'SOSB', 'SOSK', 'SOSZ', 'SOUG', 'SOUR', 'STR', 'PRJB', 'SOKI', 'PAS', 'KSOJ001',
                  'KSOJ002', 'KSOJ003', 'KSOJ004', 'KSOJ005', 'KSOJ006', 'KSOJ007', 'KSOJ008', 'KSOJ009', 'SOAS',
                  'KSOJF', 'OFS', 'KGL']
    path_where_from_copy = Path(f'{label_where_from["text"]}')
    path_where_copy = Path(f'{label_where["text"]}')
    data_delete = (datetime.now() - timedelta(14)).date()
    last_data = 0
    button_star_copy.destroy()
    for file in os.listdir(path_where_copy):
        data_file = determining_date(path_where_copy, file)
        if not last_data:
            last_data = data_file
        if data_file > last_data:
            last_data = data_file
        if data_file < data_delete:
            os.remove(os.path.join(path_where_copy, file))
    print(last_data)
    count = 0
    max_len = len(os.listdir(path_where_from_copy))
    progressbar_copy_updates = create_progressbar(
        children_window_updates_for_sud,
        count, max_len, 3, 0)
    for upd_file in os.listdir(path_where_from_copy):
        count += 1
        progressbar_copy_updates['value'] = count
        progressbar_copy_updates.update()
        base_name = upd_file.split('#')[0]
        data_file = determining_date(path_where_from_copy, upd_file)
        if base_name in base_names and data_file > last_data:
            shutil.copy2(os.path.join(path_where_from_copy, upd_file),
                         os.path.join(path_where_copy, upd_file))
    showinfo('Копирование', 'Копирование завершено')
    children_window_updates_for_sud.destroy()


def path_copy(label, button, row):
    directory = fd.askdirectory(title="Выбор папки", initialdir="/")
    if directory:
        button.destroy()
        label['text'] = directory
        label.grid(row=row, column=0, padx=20, pady=5)


def start_copy_updates_for_sud():
    children_window_updates_for_sud = create_children_window('Обновления для суда')
    label_where_from = tk.Label(children_window_updates_for_sud, text='Откуда копировать',
                                font='Calibri 13 bold')
    label_where_from.grid(row=0, column=0)
    button_where_from = tk.Button(children_window_updates_for_sud,
                                  text='Задать',
                                  font='Calibri 15 bold', width=30, height=1,
                                  command=lambda:
                                  path_copy(label_where_from, button_where_from, 0))
    button_where_from.grid(row=1, column=0, padx=20, pady=5)
    label_where = tk.Label(children_window_updates_for_sud, text='Куда копировать',
                           font='Calibri 13 bold')
    label_where.grid(row=2, column=0)
    button_where = tk.Button(children_window_updates_for_sud,
                             text='Задать',
                             font='Calibri 15 bold', width=30, height=1,
                             command=lambda:
                             path_copy(label_where, button_where, 2))
    button_where.grid(row=3, column=0, padx=20, pady=5)
    button_star_copy = tk.Button(children_window_updates_for_sud, text='Начать копирование',
                                 font='Calibri 13 bold',
                                 width=30, height=1,
                                 command=lambda: updates_for_sud(children_window_updates_for_sud,
                                                                 label_where_from, label_where,
                                                                 button_star_copy))
    button_star_copy.grid(row=4, column=0, padx=20, pady=5)
    children_window_updates_for_sud.update()
