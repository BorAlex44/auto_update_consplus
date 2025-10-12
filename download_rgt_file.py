import os
from tkinter.messagebox import showerror, showinfo

from base_app import connect_to_ftp


def download_rgt_file():
    ftp_server = connect_to_ftp()
    path_save_rgt = 'E:\\ConsPlus\\RGT\\'
    os.chdir(path_save_rgt)
    if ftp_server:
        ftp_server.cwd('updates//rgt')
        with open('CONS265.RGT', 'wb') as local_file:
            response = ftp_server.retrbinary('RETR CONS265.RGT', local_file.write)
            if response.startswith('226'):  # Transfer complete
                showinfo('Результат', 'Новый файл rgt успешно скачан')
            else:
                showerror('Результат', 'Ошибка.Файл rgt не скачан')
    else:
        showerror('Ошибка', 'Нет подключения к FTP')
    ftp_server.close()
