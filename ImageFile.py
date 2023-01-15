import os
import shutil

from PIL import Image
from PIL import UnidentifiedImageError


class ImageFile:
    def __init__(self, image_path):
        self.image_path = image_path
        self.month_names = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                            "Octubre", "Noviembre", "Diciembre"]

    def get_date_taken(self):
        try:
            return Image.open(self.image_path)._getexif()[36867]
        except TypeError:  # IMAGENES SIN EXIF
            return self.generate_name(os.path.basename(self.image_path))
        except UnidentifiedImageError:  # SON VIDEOS
            return self.generate_name(os.path.basename(self.image_path))
        except KeyError:  # NO SON IMAGENES
            return self.generate_name(os.path.basename(self.image_path))

    def get_year_taken(self):
        return self.get_date_taken()[:4]

    def get_month_taken(self):
        return self.get_date_taken()[5:7]

    def create_dir(self, dst_path):
        try:
            dir = dst_path
            if not os.path.isdir(dir):
                os.mkdir(dir)
            dir += f"/{self.get_year_taken()}"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            dir += f"/{self.get_month_taken()}_{self.month_names[int(self.get_month_taken())]}"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            return dir
        except FileExistsError:
            pass

    def move_file(self, dst_path):
        dst_dir = self.create_dir(dst_path)
        try:
            shutil.move(self.image_path, dst_dir, copy_function=shutil.copy2)
        except:
            pass

    def generate_name(self, file_name):
        default_date = "9999:12:31 23:59:59"
        if file_name.endswith(".jpg") or file_name.endswith(".webp") or file_name.endswith(".jpeg"):
            if file_name.startswith("IMG-") or file_name.startswith("IMG_"):
                year = file_name[4:8]
                month = file_name[8:10]
                return f"{year}:{month}:01 00:00:00"
            else:
                return default_date
        elif file_name.endswith(".mp4"):
            if file_name.startswith("VID-"):
                year = file_name[4:8]
                month = file_name[8:10]
                return f"{year}:{month}:01 00:00:00"
            elif len(file_name) == 19:
                year = file_name[:4]
                month = file_name[4:6]
                return f"{year}:{month}:01 00:00:00"
            else:
                return default_date
        else:
            return default_date
