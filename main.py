# The sys module is responsible for processing command line arguments
import sys
from PySide6.QtWidgets import QApplication

from MainWidget import MyApp
# from app import myApp

# Initiate the application
app = QApplication(sys.argv)

window = MyApp(app)
window.show()

# we call app.exec() to enter the Qt main loop and start to execute the Qt code
app.exec()
