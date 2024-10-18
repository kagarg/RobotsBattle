from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import * 
import sys

class Window(QMainWindow):

    def __init__(self):  # создаем конструктор
        super(Window, self).__init__()  # используем конструктор родительского класса

        self.setWindowTitle("Таймер")
        self.setGeometry(300, 250, 1000, 800)

        self.initial_time = 10 * 60  # 10 минут в секундах
        self.time_left = self.initial_time  # текущее время
        self.timer_active = False  # флаг для состояния таймера

        # Основной текст
        #self.main_text = QtWidgets.QLabel(self)
        #self.main_text.setText("Таймер")
        #self.main_text.move(490, 10)
        #self.main_text.adjustSize()

        # Текущие значения таймера
        self.time_label = QtWidgets.QLabel(self)
        self.update_time_label()
        self.time_label.move(350, 300)
        self.time_label.setFont(QFont('Arial', 25))
        self.time_label.adjustSize()
        # Кнопка "Старт"
        self.start_btn = QtWidgets.QPushButton(self)
        self.start_btn.setText("Старт")
        self.start_btn.setFont(QFont('Arial', 15))
        self.start_btn.move(350, 700)
        self.start_btn.setFixedWidth(90)
        self.start_btn.clicked.connect(self.start_timer)

        # Кнопка "Стоп"
        self.stop_btn = QtWidgets.QPushButton(self)
        self.stop_btn.setText("Стоп")
        self.stop_btn.setFont(QFont('Arial', 15))
        self.stop_btn.move(450, 700)
        self.stop_btn.setFixedWidth(90)
        self.stop_btn.clicked.connect(self.stop_timer)

        # Кнопка "Сброс"
        self.reset_btn = QtWidgets.QPushButton(self)
        self.reset_btn.setText("Сброс")
        self.reset_btn.setFont(QFont('Arial', 15))
        self.reset_btn.move(550, 700)
        self.reset_btn.setFixedWidth(90)
        self.reset_btn.clicked.connect(self.reset_timer)

        # Таймер
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Таймер срабатывает каждую секунду
        self.timer.timeout.connect(self.update_timer)  # обновляем таймер каждую секунду

    def start_timer(self):
        if not self.timer_active:  # Если таймер не активен
            self.timer.start()
            self.timer_active = True

    def stop_timer(self):
        if self.timer_active:  # Если таймер активен
            self.timer.stop()
            self.timer_active = False

    def reset_timer(self):
        self.stop_timer()  # Останавливаем таймер при сбросе
        self.time_left = self.initial_time  # Возвращаем время на начальное значение
        self.update_time_label()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1  # уменьшаем значение времени
            self.update_time_label()
        else:
            self.timer.stop()  # Останавливаем таймер, когда время заканчивается
            self.timer_active = False
            self.time_label.setText("Время вышло!")
            self.time_label.adjustSize()

    def update_time_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.time_label.setText(f"Осталось: {minutes:02d}:{seconds:02d}")
        self.time_label.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()