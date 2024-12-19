# Seys Anthony & Prévost Louis

import os
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton , QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt , pyqtSignal

class vue(QMainWindow) :
    
    # Signaux :

    open_local_fits = pyqtSignal()
    generate_image_signal = pyqtSignal()

    # Constructeur :

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Space Viewer")
        layout = QVBoxLayout()
        
        # Affichage des champs de téléchargement
        
        self.labelRA = QLabel("Coordonnées : RA ")
        self.textRA = QLineEdit()
        self.textRA.setPlaceholderText('~ 279.23473479') 
        self.labelDEC = QLabel("Coordonnées : DEC ")
        self.textDEC = QLineEdit()
        self.textDEC.setPlaceholderText('~ 38.78368896') 
        self.labelRAD = QLabel("Radius : ")
        self.textRAD = QLineEdit()
        self.textRAD.setPlaceholderText('~ 0.001') 
        self.labelSAT = QLabel("Nom du satélite : ")
        self.textSAT = QLineEdit()
        self.textSAT.setPlaceholderText('~ JWST') 
        
        # Ajout au widget layout
        
        layout.addWidget(self.labelRA)
        layout.addWidget(self.textRA)
        layout.addWidget(self.labelDEC)
        layout.addWidget(self.textDEC)
        layout.addWidget(self.labelRAD)
        layout.addWidget(self.textRAD)
        layout.addWidget(self.labelSAT)
        layout.addWidget(self.textSAT)
        
        

        # Codes des boutons d'action :

        self.btn_charger_fichier = QPushButton("Charger des FITS en local")
        self.btn_charger_fichier.clicked.connect(self.ouvrir_fichier)
        layout.addWidget(self.btn_charger_fichier)

        self.btn_generate = QPushButton("Générer l'image")
        self.btn_generate.clicked.connect(self.generate)
        layout.addWidget(self.btn_generate)

        # Label et pixmap pour l'image actuel :

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.label)

        self.setImage()

        # Pour afficher l'app :

        widget = QWidget()
        widget.setLayout(layout)
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
        image_path = os.path.join(script_dir, 'image.png')

        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)