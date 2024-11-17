from PyQt5.QtWidgets import QApplication
from gui import SkillAutomationGUI
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SkillAutomationGUI()
    ex.show()
    sys.exit(app.exec_())
