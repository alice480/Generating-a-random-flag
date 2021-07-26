import sys
from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtGui import QPainter, QColor


class Generation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 505)
        self.setWindowTitle('Генерация случайного флага')
        self.pushButton = QPushButton(self)
        self.pushButton.move(130, 30)
        self.do_paint = False
        self.pushButton.setText("Ввести количество цветов флага")
        self.pushButton.clicked.connect(self.dialog)

    def dialog(self):
        self.count, ok_pressed = QInputDialog.getInt(self, "Введите количество",
                                                "Сколько цветов?", 1, 1)
        if ok_pressed:
            self.paint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        for i in range(self.count):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawRect(150, 90 + 25 * i, 150, 25)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Generation()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())