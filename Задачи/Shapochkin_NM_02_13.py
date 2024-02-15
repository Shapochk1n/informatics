import os
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *


"""
Написать программу редактор текстовых файлов с графическим интерфейсом. 
Обязательно: Кнопка сохранить, кнопка выхода. 
Необязательно, но приветствуется: возможность открытия файла и отображения текста в окне, 
изменение цвета и размера текста, упаковка программы, изменение цвета кнопок принаведении мыши и др.
"""

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('text editor')
        self.setGeometry(300, 250, 350, 250)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        
        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Открыть', self.action_clicked)
        fileMenu.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Открыть':
            fname = QFileDialog.getOpenFileName(self)[0]
            
            try:
                f = open(fname, 'r', encoding="utf-8")
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print('Вы не выбрали файл!')

        elif action.text() == 'Сохранить':
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(fname, 'w', encoding="utf-8")
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print('Вы не выбрали файл!')


def application():
    app = QApplication(sys.argv)
    window = Window()
    
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()
