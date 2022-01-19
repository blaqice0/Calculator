from PySide2.QtWidgets import QLineEdit, QLabel

import Calculator_Resource_lt as crlt
from Calculator_Resource_ui import CalculatorUI, CalculatorPad

global res
result = '0'

NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


def set_theme(frame: CalculatorUI, mode: str) -> None:
    if mode == 'light':
        frame.setStyleSheet(crlt.qss)


def handle_calculator_pad_buttons_click(frame: CalculatorUI) -> None:
    input_screen: QLineEdit = frame.screen_.input_screen
    output_screen: QLabel = frame.screen_.output_screen
    pad: CalculatorPad = frame.pad

    def set_text(incoming_text) -> None:
        current_text = input_screen.text()

        if output_screen.text() == '<i>SyntaxError</i>':
            output_screen.setText(str(result))

        if len(current_text) <= 25:
            if current_text == '0':
                if incoming_text in NUMS:
                    current_text = ''

            if current_text.endswith('.') and incoming_text == '.':
                ...
            else:
                current_text += incoming_text
                input_screen.setText(current_text)

    def handle_solve() -> None:
        global result

        current_text = input_screen.text()
        current_text = current_text.replace('÷', '/')
        current_text = current_text.replace('×', '*')
        current_text = current_text.replace('modulo', '%')

        try:
            result = eval(current_text)
            if len(str(result)) > 13:
                result = "{:e}".format(result)

        except (SyntaxError, TypeError, SyntaxWarning) as ex:
            print(ex)
            output_screen.setText('<i>SyntaxError</i>')
        else:
            output_screen.setText(str(result))

    def handle_clear() -> None:
        input_screen.setText('0')
        output_screen.setText('0')

        global result
        result = '0'

    def handle_delete():
        current_text = input_screen.text()
        current_text = current_text[:-1]

        if current_text == '':
            current_text = '0'

            global result
            result = '0'

        input_screen.setText(current_text)

        if output_screen.text() == '<i>SyntaxError</i>':
            output_screen.setText(str(result))

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
    pad.open_brace.clicked.connect(lambda func=set_text, text='(': func(text))
    pad.close_brace.clicked.connect(lambda func=set_text, text=')': func(text))

    pad.division.clicked.connect(lambda func=set_text, text='÷': func(text))
    pad.multiplier.clicked.connect(lambda func=set_text, text='×': func(text))
    pad.plus.clicked.connect(lambda func=set_text, text='+': func(text))
    pad.minus.clicked.connect(lambda func=set_text, text='-': func(text))
    pad.mod.clicked.connect(lambda func=set_text, text='modulo': func(text))

    pad.solve_btn.clicked.connect(handle_solve)
    pad.clear_btn.clicked.connect(handle_clear)
    frame.delete_btn.clicked.connect(handle_delete)
