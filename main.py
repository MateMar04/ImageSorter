import os
import sys
from tkinter import *
from tkinter import filedialog

from ImageFile import ImageFile
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication
from SorterWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.src_path = ""
        self.dst_path = ""

    @Slot()
    def src_dir_slot(self):
        root = Tk()
        root.withdraw()
        self.src_path = filedialog.askdirectory()
        self.ui.lb_src_dir.setText(self.src_path)

    @Slot()
    def dst_dir_slot(self):
        root = Tk()
        root.withdraw()
        self.dst_path = filedialog.askdirectory()
        self.ui.lb_dst_dir.setText(self.dst_path)

    @Slot()
    def go_slot(self):
        image_files = []
        self.ui.lb_total_number.setText(f"{len(self.get_src_files())}")

        for file in self.get_src_files():
            path = f"{self.src_path}/{file}"
            image_files.append(ImageFile(path))
            QApplication.processEvents()

        cont = 0

        for image_file in image_files:
            image_file.move_file(self.dst_path)
            cont += 1
            value = int((cont / len(image_files)) * 100)
            self.ui.progressBar.setValue(value)
            self.ui.lb_current_number.setText(f"{cont}")
            QApplication.processEvents()

    @Slot()
    def progress_changed_slot(self):
        pass

    def get_src_files(self):
        return os.listdir(self.src_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
