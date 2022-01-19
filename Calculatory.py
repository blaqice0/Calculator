import sys

from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication

import Calculator_Resource_cl as crcl
from Calculator_Resource_ui import CalculatorUI
from Calculator_Resource_ut import add_roboto_fonts, add_public_sans_fonts

if __name__ == '__main__':
    program = QApplication(sys.argv)

    add_roboto_fonts()
    add_public_sans_fonts()

    font = QFont('Roboto')
    font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
    program.setFont(font)

    win = CalculatorUI()
    win.show()

    crcl.set_theme(win, 'light')
    crcl.handle_calculator_pad_buttons_click(win)

    sys.exit(program.exec_())
