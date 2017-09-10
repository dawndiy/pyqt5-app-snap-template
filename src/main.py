#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import signal

from PyQt5.QtCore import pyqtProperty, pyqtSignal, QUrl, QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import qmlRegisterType


class Hello(QObject):

    text_changed = pyqtSignal("QString", name="textChanged")

    def __init__(self, parent=None):
        super().__init__(parent)

        self._text = "Hello Snap!"

    @pyqtProperty("QString", notify=text_changed)
    def text(self):
        return self._text

    @text.setter
    def text(self, txt):
        if txt is not self._text:
            self._text = txt
            self.text_changed.emit(self._text)


def main():
    app = QGuiApplication(sys.argv)
    dir_path = os.path.dirname(os.path.realpath(__file__))

    qmlRegisterType(Hello, 'Hello', 1, 0, 'Hello')

    view = QQuickView()
    view.setSource(QUrl(dir_path + "/qml/Main.qml"))

    view.show()

    return app.exec_()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    print("---start---")
    sys.exit(main())
