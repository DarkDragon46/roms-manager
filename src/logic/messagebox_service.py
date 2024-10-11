from PyQt6.QtWidgets import QMessageBox
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

class MessageBoxService:
    def aboutBox(self, parent):
        return QMessageBox.information(parent, "About", "Application made by DarkDragon46 :)")
       