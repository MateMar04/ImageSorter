import os
from tkinter import filedialog
from tkinter import *

from ImageFile import ImageFile


def get_dir():
    root = Tk()
    root.withdraw()
    dir = filedialog.askdirectory()
    return dir


print("Seleccione directorio fuente")
src_dir = get_dir()
print("Seleccione directorio destino")
dst_dir = get_dir()

print(src_dir)
print(dst_dir)


def get_src_files():
    return os.listdir(src_dir)


def sort():
    image_files = []
    cont = 0
    for file in get_src_files():
        path = f"{src_dir}/{file}"
        image_files.append(ImageFile(path))

    for image_file in image_files:
        image_file.move_file(dst_dir)
        cont += 1
        print(f"{cont}/{len(image_files)}")


sort()
