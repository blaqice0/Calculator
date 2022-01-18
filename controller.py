from PySide6.QtWidgets import QLineEdit, QLabel

from views import CalculatorUI, CalculatorPad

NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


def handle_calculator_pad_buttons_click(frame: CalculatorUI) -> None:
    inputScreen: QLineEdit = frame.screen_.inputScreen
    errorLabel: QLabel = frame.errorLabel
    outputScreen: QLabel = frame.screen_.outputScreen
    pad: CalculatorPad = frame.pad_

    def set_text(incoming_text) -> None:
        errorLabel.hide()
        current_text = inputScreen.text()

        if current_text == '0':
            if incoming_text in NUMS:
                current_text = ''

        current_text += incoming_text
        inputScreen.setText(current_text)

    def solve() -> None:
        errorLabel.hide()
        current_text = inputScreen.text()

        current_text = current_text.replace('÷', '/')
        current_text = current_text.replace('×', '*')
        current_text = current_text.replace('MOD', '%')

        try:
            result = eval(current_text)
        except SyntaxError:
            errorLabel.show()
            errorLabel.setText('<i>SyntaxError</i>')
        else:
            outputScreen.setText(f'{result}')

    def clear() -> None:
        errorLabel.hide()
        inputScreen.setText('0')
        outputScreen.setText('0')

    def delete():
        errorLabel.hide()
        current_text = inputScreen.text()
        current_text = current_text[:-1]

        if current_text == '':
            current_text = '0'

        inputScreen.setText(current_text)

    pad.one.clicked.connect(lambda func=set_text, text='1': func(text))
    pad.two.clicked.connect(lambda func=set_text, text='2': func(text))
    pad.three.clicked.connect(lambda func=set_text, text='3': func(text))
    pad.four.clicked.connect(lambda func=set_text, text='4': func(text))
    pad.five.clicked.connect(lambda func=set_text, text='5': func(text))
    pad.six.clicked.connect(lambda func=set_text, text='6': func(text))
    pad.seven.clicked.connect(lambda func=set_text, text='7': func(text))
    pad.eight.clicked.connect(lambda func=set_text, text='8': func(text))
    pad.nine.clicked.connect(lambda func=set_text, text='9': func(text))
    pad.zero.clicked.connect(lambda func=set_text, text='0': func(text))
    pad.decimal.clicked.connect(lambda func=set_text, text='.': func(text))
    pad.openBrace.clicked.connect(lambda func=set_text, text='(': func(text))
    pad.closeBrace.clicked.connect(lambda func=set_text, text=')': func(text))

    pad.division.clicked.connect(lambda func=set_text, text='÷': func(text))
    pad.multiplier.clicked.connect(lambda func=set_text, text='×': func(text))
    pad.plus.clicked.connect(lambda func=set_text, text='+': func(text))
    pad.minus.clicked.connect(lambda func=set_text, text='-': func(text))
    pad.mod.clicked.connect(lambda func=set_text, text='MOD': func(text))

    pad.solve.clicked.connect(solve)
    pad.clear.clicked.connect(clear)
    pad.delete.clicked.connect(delete)
