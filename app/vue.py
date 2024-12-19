# Seys Anthony & Prévost Louis

import os
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton , QLabel, QLineEdit, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt , pyqtSignal

class vue(QMainWindow) :
    
    # Signaux :

    open_local_fits = pyqtSignal()
    generate_image_signal = pyqtSignal()
    download_signal = pyqtSignal(float , float , float , str)
    save_as_signal = pyqtSignal()

    # Constructeur :

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Space Viewer")
        layout_gauche = QVBoxLayout()
        layout_main = QHBoxLayout()
        layout_main.addLayout(layout_gauche)
        
        # Affichage des champs de téléchargement
        
        self.labelRA = QLabel("Coordonnées : RA ")
        self.textRA = QLineEdit()
        self.textRA.setText('279.23473479')

        self.labelDEC = QLabel("Coordonnées : DEC ")
        self.textDEC = QLineEdit()
        self.textDEC.setText('38.78368896') 

        self.labelRAD = QLabel("Radius : ")
        self.textRAD = QLineEdit()
        self.textRAD.setText('0.001') 

        self.labelSAT = QLabel("Nom du satélite : ")
        self.textSAT = QLineEdit()
        self.textSAT.setText('JWST') 
        
        # Ajout au widget layout
        
        layout_gauche.addWidget(self.labelRA)
        layout_gauche.addWidget(self.textRA)
        layout_gauche.addWidget(self.labelDEC)
        layout_gauche.addWidget(self.textDEC)
        layout_gauche.addWidget(self.labelRAD)
        layout_gauche.addWidget(self.textRAD)
        layout_gauche.addWidget(self.labelSAT)
        layout_gauche.addWidget(self.textSAT)
        
        # Codes des boutons d'action :

        self.btn_download = QPushButton("Télécharger les FITS")
        self.btn_download.clicked.connect(self.download)
        layout_gauche.addWidget(self.btn_download)

        self.btn_charger_fichier = QPushButton("Charger des FITS en local")
        self.btn_charger_fichier.clicked.connect(self.ouvrir_fichier)
        layout_gauche.addWidget(self.btn_charger_fichier)

        self.btn_generate = QPushButton("Générer l'image")
        self.btn_generate.clicked.connect(self.generate)
        layout_gauche.addWidget(self.btn_generate)

        self.btn_save_as = QPushButton("Générer l'image")
        self.btn_save_as.clicked.connect(self.save_as)
        layout_gauche.addWidget(self.btn_save_as)

        # Label et pixmap pour l'image actuel :

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout_main.addWidget(self.label)

        self.setImage()

        # Pour afficher l'app :

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        self.setGeometry(100, 100, 800, 600)
        self.show()

    # Fonctions :

    def ouvrir_fichier(self):
        self.open_local_fits.emit()

    def generate(self):
        self.generate_image_signal.emit()
        self.setImage()

    def setImage(self) : 
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'last_image.png')

        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)

    def download(self) :
        v_ra = float(self.textRA.text())
        v_dec = float(self.textDEC.text())
        v_rad = float(self.textRAD.text())
        v_sat = self.textSAT.text()

        self.download_signal.emit(v_ra , v_dec , v_rad , v_sat)

    def save_as(self) : 
        self.save_as_signal.emit()  

