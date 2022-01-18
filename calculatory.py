import sys

from PySide6.QtWidgets import QApplication

import controller as ctrl
from views import CalculatorUI

if __name__ == '__main__':
    program = QApplication(sys.argv)

    win = CalculatorUI()
    win.show()

    ctrl.handle_calculator_pad_buttons_click(win)

    sys.exit(program.exec())
