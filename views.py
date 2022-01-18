from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class ErrorLabel(QLabel):
    def __init__(self):
        super(ErrorLabel, self).__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)


class CalculatorScreen(QFrame):
    def __init__(self) -> None:
        super(CalculatorScreen, self).__init__()

        self.inputScreen = QLineEdit('0')
        self.inputScreen.setReadOnly(True)
        self.inputScreen.setMinimumHeight(45)

        self.outputScreen = QLabel('0')
        self.outputScreen.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.outputScreen.setMinimumHeight(45)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.inputScreen)
        mainLayout.addWidget(self.outputScreen)


class CalculatorButton(QPushButton):
    def __init__(self, text: str) -> None:
        super(CalculatorButton, self).__init__(text)

        self.setMinimumSize(40, 40)


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
        self.minus = CalculatorButton('−')
        self.plus = CalculatorButton('+')
        self.multiplier = CalculatorButton('×')
        self.division = CalculatorButton('÷')
        self.solve = CalculatorButton('SOLVE')
        self.clear = CalculatorButton('C')
        self.mod = CalculatorButton('MOD')
        self.delete = CalculatorButton('DEL')
        self.openBrace = CalculatorButton('(')
        self.closeBrace = CalculatorButton(')')
        self.decimal = CalculatorButton('.')

        rowA = QHBoxLayout()
        rowA.addWidget(self.clear)
        rowA.addWidget(self.delete)
        rowA.addWidget(self.mod)
        rowA.addWidget(self.division)

        rowB = QHBoxLayout()
        rowB.addWidget(self.seven)
        rowB.addWidget(self.eight)
        rowB.addWidget(self.nine)
        rowB.addWidget(self.multiplier)

        rowC = QHBoxLayout()
        rowC.addWidget(self.four)
        rowC.addWidget(self.five)
        rowC.addWidget(self.six)
        rowC.addWidget(self.minus)

        rowD = QHBoxLayout()
        rowD.addWidget(self.one)
        rowD.addWidget(self.two)
        rowD.addWidget(self.three)
        rowD.addWidget(self.plus)

        rowE = QHBoxLayout()
        rowE.addWidget(self.openBrace)
        rowE.addWidget(self.zero)
        rowE.addWidget(self.closeBrace)
        rowE.addWidget(self.decimal)

        rowF = QHBoxLayout()
        rowF.addWidget(self.solve)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(rowA)
        mainLayout.addLayout(rowB)
        mainLayout.addLayout(rowC)
        mainLayout.addLayout(rowD)
        mainLayout.addLayout(rowE)
        mainLayout.addLayout(rowF)


class CalculatorUI(QFrame):
    def __init__(self) -> None:
        super(CalculatorUI, self).__init__()

        self.screen_ = CalculatorScreen()
        self.errorLabel = ErrorLabel()
        self.pad_ = CalculatorPad()

        self.errorLabel.hide()

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.screen_)
        mainLayout.addWidget(self.errorLabel)
        mainLayout.addWidget(self.pad_)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
