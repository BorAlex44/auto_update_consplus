import os
import shutil
from pathlib import Path
from tkinter.messagebox import showinfo
import tkinter.filedialog as fd
import tkinter as tk
from base_app import determining_date, create_progressbar, create_children_window


def copy_updates_from_flash(children_window_determining_letter_flash, letter_flash, button_set_path):
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    if directory:
        label_flash = tk.Label(children_window_determining_letter_flash,
                               text='Буква флешки',
                               font='Calibri 13 bold')
        label_flash.grid(row=1, column=0)
        label_flash['text'] = directory
        letter_flash['text'] = 'Задан путь'
        button_set_path.destroy()
        path_updates_to_flash = Path(f'{label_flash["text"]}')
        last_data = 0
        for file in os.listdir(path_updates_to_flash):
            file_data = determining_date(path_updates_to_flash, file)
            if last_data == 0:
                last_data = file_data
            else:
                if file_data > last_data:
                    last_data = file_data
        path_updates_from_copy = Path('E:\\ConsPlus\\3000\\')
        count = 0
        max_len = len(os.listdir(path_updates_from_copy))
        progressbar_copy_updates = create_progressbar(
            children_window_determining_letter_flash,
            count, max_len, 3, 0)
        for file in os.listdir(path_updates_from_copy):
            count += 1
            progressbar_copy_updates['value'] = count
            progressbar_copy_updates.update()
            file_data = determining_date(path_updates_from_copy, file)
            if file_data > last_data:
                shutil.copy2(os.path.join(path_updates_from_copy, file),
                             os.path.join(path_updates_to_flash, file))
        showinfo('Копирование', 'Копирование завершено')
        children_window_determining_letter_flash.destroy()


def start_process_copy_updates_from_flash():
    children_window_determining_letter_flash = create_children_window('Копирование на флешку')
    letter_flash = tk.Label(children_window_determining_letter_flash,
                            text='Определение буквы флешки',
                            font='Calibri 13 bold')
    letter_flash.grid(row=0, column=0)

    children_window_determining_letter_flash.update()
    button_set_path = tk.Button(children_window_determining_letter_flash, text='Задать',
                                font='Calibri 15 bold', width=30, height=1,
                                command=lambda:
                                copy_updates_from_flash(children_window_determining_letter_flash,
                                                        letter_flash, button_set_path))

    button_set_path.grid(row=3, column=0, padx=20, pady=5)
    children_window_determining_letter_flash.update()

