import win32api
import win32print
import os

desk_path = r'C:\Users\341137\OneDrive - AEON\デスクトップ'
dir_path = input('フォルダ名: ')
path = f'{desk_path}\{dir_path}'

list_in_dir = os.listdir(path=path)
# print(list_in_dir)

for file_path in list_in_dir:
    print_path = f'{path}\{file_path}'
    win32api.ShellExecute(
        0,
        "print",
        print_path,
        "/c:""%s" % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    print(f'print: {file_path}')