import tkinter as tk

from copy_updates_from_flash import start_process_copy_updates_from_flash
from delete_old_archives import start_delete_old_archives
from delete_old_receive_files import start_delete_old_receive_files
from download_rgt_file import download_rgt_file
from download_system import start_download_new_system
from download_updates import download_updates
from updates_for_sud import start_copy_updates_for_sud

root = tk.Tk()

root.title('Автоматизация обновления К+')
root.geometry('350x450+300+300')
button_rgt_download = tk.Button(root, text='Скачать RGT', font='Calibri 15 bold', width=30, height=1,
                                command=download_rgt_file)
button_arch_download = tk.Button(root, text='Скачать архивы пополнения',
                                 font='Calibri 15 bold', width=30, height=1,
                                 command=download_updates)
button_copy_updates_from_flesh = tk.Button(root, text='Копировать файлы \n пополнения на флешку',
                                           font='Calibri 15 bold', width=30, height=2,
                                           command=start_process_copy_updates_from_flash)
button_updates_for_sud = tk.Button(root, text='Обновление для суда',
                                   font='Calibri 15 bold', width=30, height=1,
                                   command=start_copy_updates_for_sud)
button_delete_old_archives = tk.Button(root, text='Удаление старых архивов',
                                       font='Calibri 15 bold', width=30, height=1,
                                       command=start_delete_old_archives)
button_delete_old_receive_files = tk.Button(root, text='Удаление старых \n файлов пополнения',
                                            font='Calibri 15 bold', width=30, height=2,
                                            command=start_delete_old_receive_files)
button_download_system = tk.Button(root, text='Скачать папку system',
                                   font='Calibri 15 bold', width=30, height=1,
                                   command=start_download_new_system)
button_close_app = tk.Button(root, text='Завершить работу',
                             font='Calibri 15 bold', width=30, height=1,
                             command=lambda: root.destroy())
button_rgt_download.grid(row=0, column=0, pady=5)
button_arch_download.grid(row=1, column=0, pady=3)
button_copy_updates_from_flesh.grid(row=2, column=0, pady=3)
button_updates_for_sud.grid(row=3, column=0, pady=3)
button_delete_old_archives.grid(row=4, column=0, pady=3)
button_delete_old_receive_files.grid(row=5, column=0, pady=3)
button_download_system.grid(row=6, column=0, pady=3)
button_close_app.grid(row=7, column=0, pady=3)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
