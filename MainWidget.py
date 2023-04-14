from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QToolBar,QLabel, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MyApp(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("KG to Pounds converter")
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

            #Elements
            self.lbl_kg = QLabel("Kilograms")
            self.entryKG = QLineEdit("0.0")
            self.btn1 = QPushButton("Convert")

            self.lbl_pd = QLabel("Pounds")
            self.entryPD = QLineEdit("0.0")
            self.btn2 = QPushButton("Convert")
            
            # Grid layout
            self.layout.addWidget(self.lbl_kg,0,0)
            self.layout.addWidget(self.entryKG,0,1)
            self.layout.addWidget(self.btn1,0,2)

            self.layout.addWidget(self.lbl_pd,1,0)
            self.layout.addWidget(self.entryPD,1,1)
            self.layout.addWidget(self.btn2,1,2)

            # Functions
            self.btn1.clicked.connect(self.kgToPd)
            self.btn2.clicked.connect(self.PdToKg)


            self.setLayout(self.layout)
            

            

    def kgToPd(self):
        try:
            pd = self.entryKG.text()
            pd = round(float(pd) * 2.205, 3)
            self.entryPD.setText(str(pd))
        except ValueError:
            print(ValueError)
            self.entryKG.setText("0.0")
            self.entryPD.setText("0.0")
        
    def PdToKg(self):
        try:
            kg = self.entryPD.text()
            kg = round(float(kg) / 2.205, 3)
            self.entryKG.setText(str(kg))
        except ValueError:
            print(ValueError)
            self.entryKG.setText("0.0")
            self.entryPD.setText("0.0")