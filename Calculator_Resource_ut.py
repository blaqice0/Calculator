from datetime import datetime, timedelta
from glob import glob

from PySide2.QtCore import QSize, QPoint
from PySide2.QtGui import QColor, Qt, QImage, QPixmap, QIcon, QFont, QFontDatabase
from PySide2.QtWidgets import (
    QGraphicsDropShadowEffect,
    QFrame,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QDesktopWidget,
    QApplication
)


def wait(msec: int) -> None:
    """ Wait for a certain amount of time and continue execution of specific process """

    end = datetime.now() + timedelta(milliseconds=msec)
    while datetime.now() < end:
        QApplication.processEvents()


def drop_shadow(parent, color='#000', alpha=0.2, blur=25, x=.5, y=3):
    color = QColor(color)
    color.setAlphaF(alpha)

    ds = QGraphicsDropShadowEffect(parent)
    ds.setBlurRadius(blur)
    ds.setXOffset(x)
    ds.setYOffset(y)
    ds.setColor(color)
    return ds


def add_roboto_fonts() -> None:
    font_path = 'fonts/Roboto/*.ttf'
    fonts = glob(font_path)

    for font in fonts:
        wait(30)  # Prevent CPU overload
        QFontDatabase.addApplicationFont(font)


def add_public_sans_fonts() -> None:
    font_path = 'fonts/Public_Sans/*.ttf'
    fonts = glob(font_path)

    for font in fonts:
        wait(30)  # Prevent CPU overload
        QFontDatabase.addApplicationFont(font)


class ModIconImage:
    """ Modifies icon color or size

    """

    def __init__(self, filepath) -> None:

        self.__img: QImage = QImage(filepath)

    def set_size(self, w: int, h: int):
        size: QSize = self.__img.size()

        if w > size.width() or h > size.height():
            raise Exception(
                'Size set will reduce icon visibility. Set size below existing size.')

        self.__img = self.__img.scaled(
            w, h, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        return self

    def set_color(self, color: str):
        color = QColor(color)
        for x in range(self.__img.height()):
            for y in range(self.__img.width()):
                color.setAlpha(self.__img.pixelColor(x, y).alpha())
                self.__img.setPixelColor(x, y, color)
        return self

    def get_pixmap(self) -> QPixmap:
        return QPixmap.fromImage(self.__img)

    def get_icon(self) -> QIcon:
        return QIcon(self.get_pixmap())


class Button(QPushButton):
    def __init__(self, text: str = '') -> None:
        super(Button, self).__init__(text)

        self.__icon_name = None
        self.__icon_size = None

        font = QFont('Public Sans')
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.setFont(font)

    def setIcon(self, name: str, color: str, size: QSize) -> None:
        self.__icon_name = name
        self.__icon_size = size

        icon = ModIconImage(f'icons/{name}').set_color(color).get_icon()
        self.setIconSize(size)
        super(Button, self).setIcon(icon)

    def updateIconColor(self, color) -> None:
        self.setIcon(self.__icon_name, color, self.__icon_size)


class IconButton(Button):
    ...


class WindowButton(IconButton):
    def __init__(self, icon_name):
        super(WindowButton, self).__init__()

        self.setMinimumSize(30, 30)
        self.setMaximumSize(30, 30)
        self.setIcon(icon_name, '#D0D1D2', QSize(17, 17))

    def enterEvent(self, event) -> None:
        event.accept()
        self.updateIconColor('#FFF')

    def leaveEvent(self, event) -> None:
        event.accept()
        self.updateIconColor('#D0D1D2')


class MinimizeButton(WindowButton):
    def __init__(self):
        super(MinimizeButton, self).__init__('minus.png')


class CloseButton(WindowButton):
    def __init__(self):
        super(CloseButton, self).__init__('close.png')


class ScreenControlButton(Button):
    def __init__(self, text: str):
        super(ScreenControlButton, self).__init__(text)

        self.setMinimumHeight(25)
        self.setMaximumHeight(25)


class CalculatorButton(Button):
    def __init__(self, text=''):
        super(CalculatorButton, self).__init__(text)

        self.setFlat(False)
        self.setMinimumSize(61, 81)


class CalculatorRightButton(CalculatorButton):
    ...


class WindowsTitleBar(QFrame):
    def __init__(self) -> None:
        super(WindowsTitleBar, self).__init__()

        left_frame = QFrame()
        right_frame = QFrame()

        self.menu_btn = IconButton()
        self.menu_btn.setIcon('menu.png', '#D0D1D2', QSize(19, 19))

        self.operation_indication_label = Label('DEC')
        self.operation_indication_label.setObjectName('indication-label')
        self.operation_indication_label.setContentsMargins(0, 0, 0, 2)

        self.minimize_btn = MinimizeButton()
        self.close_btn = CloseButton()

        left_lay = QHBoxLayout(left_frame)
        left_lay.addWidget(self.menu_btn)
        left_lay.addWidget(self.operation_indication_label)
        left_lay.setAlignment(Qt.AlignmentFlag.AlignLeft)
        left_lay.setSpacing(10)
        left_lay.setContentsMargins(10, 0, 0, 0)

        right_frame.setContentsMargins(0, 0, 0, 0)

        right_lay = QHBoxLayout(right_frame)
        right_lay.addWidget(self.minimize_btn)
        right_lay.addWidget(self.close_btn)
        right_lay.setAlignment(Qt.AlignmentFlag.AlignRight)
        right_lay.setSpacing(10)
        right_lay.setContentsMargins(0, 0, 5, 0)

        main_lay = QHBoxLayout(self)
        main_lay.addWidget(left_frame)
        main_lay.addWidget(right_frame)
        main_lay.setStretch(0, 1)
        main_lay.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_lay.setContentsMargins(0, 5, 0, 0)

        self.setMaximumHeight(40)


class FramelessContentFrame(QFrame):
    def __init__(self, parent):
        super(FramelessContentFrame, self).__init__()
        self.setGraphicsEffect(drop_shadow(parent))


class Frameless(QFrame):
    def __init__(self):
        super(Frameless, self).__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.window_bar = WindowsTitleBar()

        self.content_frame = FramelessContentFrame(self)

        self.window_bar.minimize_btn.clicked.connect(self.handleMinimizeButton)
        self.window_bar.close_btn.clicked.connect(self.handleCloseButton)

        self.content_lay = QVBoxLayout(self.content_frame)
        self.content_lay.addWidget(self.window_bar)
        self.content_lay.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.content_lay.setContentsMargins(1, 1, 1, 1)
        self.content_lay.setSpacing(0)

        self.__main_lay = QVBoxLayout(self)
        self.__main_lay.addWidget(self.content_frame)
        self.__main_lay.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.center()
        self.old_pos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()

    def handleMinimizeButton(self):
        self.showMinimized()

    def handleCloseButton(self):
        self.close()


class Label(QLabel):
    def __init__(self, text='') -> None:
        super(Label, self).__init__(text)

        font = QFont('Roboto')
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.setFont(font)
