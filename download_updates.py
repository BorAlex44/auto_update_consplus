import os
from datetime import time, date, timedelta
from pathlib import Path
from tkinter.messagebox import showinfo
import tkinter as tk
import rarfile
import time

from base_app import download_arch, create_progressbar, get_data_archive, connect_to_ftp, create_children_window


def download_updates():
    path_ftp_update = 'updates//3000'
    ftp_server = connect_to_ftp()
    arch_list_on_disc = []
    path_save_archives = Path('E:\\ConsPlus\\Arch_update\\')
    path_update_files = Path('E:\\ConsPlus\\3000\\')
    if path_save_archives.exists():
        os.chdir(path_save_archives)
        arch_list_on_disc += os.listdir(path_save_archives)
        if len(arch_list_on_disc) > 0:
            last_data = get_data_archive(arch_list_on_disc[-1])
        else:
            last_data = date.today() - timedelta(days=7)
    else:
        Path.mkdir(path_save_archives)
        os.chdir(path_save_archives)
        last_data = date.today() - timedelta(days=7)
    if not path_update_files.exists():
        Path.mkdir(path_update_files)

    print(last_data)
    ftp_server.cwd(path_ftp_update)
    arch_update_list = ftp_server.nlst()
    print(arch_update_list)
    list_from_download = []
    for arch in arch_update_list:
        data_arch = get_data_archive(arch)
        if data_arch > last_data:
            list_from_download.append(arch)
    if not list_from_download:
        showinfo('Download', f'Новых архивов для скачивания нет')
        return
    if len(list_from_download) in (11, 12, 13, 14):
        showinfo('Download', f'Будет скачано {len(list_from_download)} архивов')
    elif len(list_from_download) % 10 == 1:
        showinfo('Download', f'Будет скачан {len(list_from_download)} архив')
    elif len(list_from_download) % 10 in (2, 3, 4):
        showinfo('Download', f'Будет скачано {len(list_from_download)} архива')
    else:
        showinfo('Download', f'Будет скачано {len(list_from_download)} архивов')
    children_window_download_updates_archives = create_children_window('Работа с файлами')
    action_arch_label = tk.Label(children_window_download_updates_archives,
                                 text='Действие', font='Calibri 13 bold')
    action_arch_label.grid(row=0, column=0)
    name_arch_label = tk.Label(children_window_download_updates_archives,
                               text='Имя', font='Calibri 13 bold')
    name_arch_label.grid(row=1, column=0)
    size_arch_label = tk.Label(children_window_download_updates_archives,
                               text='Размер', font='Calibri 13 bold')
    size_arch_label.grid(row=2, column=0)
    count = 0
    max_len = len(list_from_download)
    progressbar_download = create_progressbar(children_window_download_updates_archives,
                                              count, max_len, 3, 0)

    for name_arch in list_from_download:
        count += 1
        arch_size = ftp_server.size(name_arch)
        action_arch_label['text'] = 'Скачивание архива'
        name_arch_label['text'] = name_arch
        size_arch_label['text'] = arch_size
        children_window_download_updates_archives.update()
        progressbar_download['value'] = count
        progressbar_download.update()

        response = download_arch(name_arch, ftp_server)

        if response.startswith('226'):
            action_arch_label['text'] = 'Скачан архив'
            children_window_download_updates_archives.update()
            time.sleep(5)
        opened_rar = rarfile.RarFile(name_arch)
        action_arch_label['text'] = 'Тест архива'
        children_window_download_updates_archives.update()
        test_arch = opened_rar.testrar()
        if test_arch is None:
            action_arch_label['text'] = 'Тест архива - успешно'
            children_window_download_updates_archives.update()
            time.sleep(5)
        else:
            action_arch_label['text'] = 'Тест архива - провален'
            children_window_download_updates_archives.update()
            time.sleep(5)
            break
        action_arch_label['text'] = 'Разархивация архива'
        children_window_download_updates_archives.update()
        opened_rar.extractall(path_update_files)
        action_arch_label['text'] = 'Архив разархивирован'
        children_window_download_updates_archives.update()
        time.sleep(5)
    showinfo('Результат', 'Все архивы скачаны, протестированы и разархивированы')
    children_window_download_updates_archives.destroy()
