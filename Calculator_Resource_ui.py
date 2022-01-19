from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
)

from Calculator_Resource_ut import (
    CalculatorButton,
    CalculatorRightButton,
    IconButton,
    Frameless,
    Label,
)


class CalculatorScreen(QFrame):
    def __init__(self) -> None:
        super(CalculatorScreen, self).__init__()

        self.input_screen = QLineEdit('0')
        self.input_screen.setMinimumHeight(25)
        self.input_screen.setMaximumHeight(25)
        self.input_screen.setObjectName('input-screen')
        self.input_screen.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.output_screen = Label('0')
        self.output_screen.setMinimumHeight(50)
        self.output_screen.setObjectName('output-screen')
        self.output_screen.setAlignment(Qt.AlignmentFlag.AlignRight)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.input_screen)
        mainLayout.addWidget(self.output_screen)


class CalculatorPad(QFrame):
    def __init__(self) -> None:
        super(CalculatorPad, self).__init__()

        self.one = CalculatorButton('1')
        self.two = CalculatorButton('2')
        self.three = CalculatorButton('3')
        self.four = CalculatorButton('4')
        self.five = CalculatorButton('5')
        self.six = CalculatorButton('6')
        self.seven = CalculatorButton('7')
        self.eight = CalculatorButton('8')
        self.nine = CalculatorButton('9')
        self.zero = CalculatorButton('0')
        self.mod = CalculatorButton('%')
        self.decimal = CalculatorButton('.')
        self.clear_btn = CalculatorButton('C')
        self.open_brace = CalculatorButton('(')
        self.close_brace = CalculatorButton(')')

        self.division = CalculatorRightButton('÷')
        self.multiplier = CalculatorRightButton('×')
        self.minus = CalculatorRightButton('−')
        self.plus = CalculatorRightButton('+')
        self.solve_btn = CalculatorRightButton('=')

        self.clear_btn.setObjectName('special-calc-btn')
        self.open_brace.setObjectName('special-calc-btn')
        self.close_brace.setObjectName('special-calc-btn')
        self.mod.setObjectName('special-calc-btn')
        self.mod.setObjectName('mod')
        self.solve_btn.setObjectName('equal')

        grid_lay = QGridLayout(self)
        grid_lay.setContentsMargins(1, 1, 1, 1)

        grid_lay.setHorizontalSpacing(1)
        grid_lay.setVerticalSpacing(1)

        grid_lay.addWidget(self.clear_btn, 0, 0)
        grid_lay.addWidget(self.open_brace, 0, 1)
        grid_lay.addWidget(self.close_brace, 0, 2)
        grid_lay.addWidget(self.division, 0, 3)

        grid_lay.addWidget(self.seven, 1, 0)
        grid_lay.addWidget(self.eight, 1, 1)
        grid_lay.addWidget(self.nine, 1, 2)
        grid_lay.addWidget(self.multiplier, 1, 3)

        grid_lay.addWidget(self.four, 2, 0)
        grid_lay.addWidget(self.five, 2, 1)
        grid_lay.addWidget(self.six, 2, 2)
        grid_lay.addWidget(self.minus, 2, 3)

        grid_lay.addWidget(self.one, 3, 0)
        grid_lay.addWidget(self.two, 3, 1)
        grid_lay.addWidget(self.three, 3, 2)
        grid_lay.addWidget(self.plus, 3, 3)

        grid_lay.addWidget(self.mod, 4, 0)
        grid_lay.addWidget(self.zero, 4, 1)
        grid_lay.addWidget(self.decimal, 4, 2)
        grid_lay.addWidget(self.solve_btn, 4, 3)


class CalculatorUI(Frameless):
    def __init__(self) -> None:
        super(CalculatorUI, self).__init__()

        self.screen_ = CalculatorScreen()

        self.delete_btn = IconButton()
        self.delete_btn.setIcon('clear_symbol.png', '#FF6159', QSize(32, 32))

        lay = QHBoxLayout()
        lay.addWidget(self.delete_btn)
        lay.setContentsMargins(0, 0, 10, 5)
        lay.setSpacing(10)
        lay.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.pad = CalculatorPad()

        self.content_lay.addWidget(self.screen_)
        self.content_lay.addLayout(lay)
        self.content_lay.addWidget(self.pad)
        self.content_lay.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.content_lay.setSpacing(0)

        self.content_frame.setMaximumWidth(380)
        self.setMaximumWidth(380)
