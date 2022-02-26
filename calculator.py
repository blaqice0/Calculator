import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

import calculator_ctrl as ctrl
from calculator_ui import CalculatorUI
from calculator_utils import add_roboto_fonts, add_public_sans_fonts

if __name__ == '__main__':
    program = QApplication(sys.argv)

    add_roboto_fonts()
    add_public_sans_fonts()

    font = QFont('Roboto')
    font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
    program.setFont(font)

    win = CalculatorUI()
    win.show()

    ctrl.set_theme(win)
    ctrl.handle_calculator_pad_buttons_click(win)

    sys.exit(program.exec())
