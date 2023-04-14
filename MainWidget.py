from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton


class MyApp(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Main app")
        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        self.form_widget = FormWidget(self) 
        self.setCentralWidget(self.form_widget)

    def quit_app(self):
        self.app.quit()

class FormWidget(QWidget):
    def __init__(self, parent):        
            super(FormWidget, self).__init__(parent)
            self.layout = QGridLayout(self)

            self.btn1 = QPushButton("btn1")
            self.btn2 = QPushButton("btn2")

            # grid = QGridLayout()  
            self.layout.addWidget(self.btn1,0,0)
            self.layout.addWidget(self.btn2,0,1)

            self.entry1 = QLineEdit("")
            self.layout.addWidget(self.entry1,1,1)

            self.btn3 = QPushButton("btn3")
            self.layout.addWidget(self.btn3,1,2)


            self.setLayout(self.layout)

    def handle_click():
         print("You clicked here !!")