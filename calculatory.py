import sys

from PySide6.QtWidgets import QApplication, QStyleFactory

import controller as ctrl
from views import CalculatorUI

if __name__ == '__main__':
    program = QApplication(sys.argv)

    win = CalculatorUI()
    win.setStyle(QStyleFactory.create('windowsvista'))
    win.show()

    ctrl.handle_calculator_pad_buttons_click(win)

    sys.exit(program.exec())
