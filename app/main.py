# Seys Anthony & Prévost Louis

from PyQt6.QtWidgets import QApplication
import sys
import controller

if __name__ == "__main__":

    app = QApplication(sys.argv)

    mon_controller = controller.controller()

    sys.exit(app.exec())
