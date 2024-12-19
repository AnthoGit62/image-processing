# Seys Anthony & Prévost Louis

import os
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton , QLabel, QLineEdit, QSlider
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt , pyqtSignal

class vue(QMainWindow) :
    
    # Signaux :

    open_local_fits = pyqtSignal()
    generate_image_signal = pyqtSignal()
    download_signal = pyqtSignal(float , float , float , str)
    save_as_signal = pyqtSignal()

    update_rouge_signal = pyqtSignal(int)
    update_vert_signal = pyqtSignal(int)
    update_bleu_signal = pyqtSignal(int)

    # Constructeur :

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Space Viewer")

        layout_gauche = QVBoxLayout()
        layout_centre = QVBoxLayout()
        layout_droite = QVBoxLayout()
        layout_main = QHBoxLayout()

        layout_main.addLayout(layout_gauche)
        layout_main.addLayout(layout_centre)
        layout_main.addLayout(layout_droite)

        layout_gauche.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_droite.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_centre.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Label de titre

        self.titreFits = QLabel("Recherche de fichier FITS")
        self.titreFits.setStyleSheet("font-size: 18px;")
        layout_gauche.addWidget(self.titreFits)

        self.titreCouleur = QLabel("Changement de filtre de couleur")
        self.titreCouleur.setStyleSheet("font-size: 18px;")
        layout_droite.addWidget(self.titreCouleur)
        
        # Affichage des champs pour le téléchargement
        
        self.labelRA = QLabel("Coordonnées : RA ")
        self.textRA = QLineEdit()
        self.textRA.setPlaceholderText('279.23473479')

        self.labelDEC = QLabel("Coordonnées : DEC ")
        self.textDEC = QLineEdit()
        self.textDEC.setPlaceholderText('38.78368896') 

        self.labelRAD = QLabel("Radius : ")
        self.textRAD = QLineEdit()
        self.textRAD.setPlaceholderText('0.001') 

        self.labelSAT = QLabel("Nom du satélite : ")
        self.textSAT = QLineEdit()
        self.textSAT.setPlaceholderText('JWST') 
        
        # Ajout au widget layout
        
        layout_gauche.addWidget(self.labelRA)
        layout_gauche.addWidget(self.textRA)

        layout_gauche.addWidget(self.labelDEC)
        layout_gauche.addWidget(self.textDEC)

        layout_gauche.addWidget(self.labelRAD)
        layout_gauche.addWidget(self.textRAD)

        layout_gauche.addWidget(self.labelSAT)
        layout_gauche.addWidget(self.textSAT)

        # Slider pour changer le rgb :

        self.lbl_slide_rouge = QLabel("Rouge")
        self.slider_rouge = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_rouge.setMinimum(0)
        self.slider_rouge.setMaximum(10)
        self.slider_rouge.setValue(4)
        self.slider_rouge.setTickInterval(1)
        layout_droite.addWidget(self.lbl_slide_rouge)
        layout_droite.addWidget(self.slider_rouge)

        self.slider_rouge.valueChanged.connect(self.update_rouge)

        self.lbl_slide_vert = QLabel("Vert")
        self.slider_vert = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_vert.setMinimum(0)
        self.slider_vert.setMaximum(10)
        self.slider_vert.setValue(2)
        self.slider_vert.setTickInterval(1)
        layout_droite.addWidget(self.lbl_slide_vert)
        layout_droite.addWidget(self.slider_vert)

        self.slider_vert.valueChanged.connect(self.update_vert)

        self.lbl_slide_bleu = QLabel("Bleu")
        self.slider_bleu = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_bleu.setMinimum(0)
        self.slider_bleu.setMaximum(10)
        self.slider_bleu.setValue(1)
        self.slider_bleu.setTickInterval(1)
        layout_droite.addWidget(self.lbl_slide_bleu)
        layout_droite.addWidget(self.slider_bleu)

        self.slider_bleu.valueChanged.connect(self.update_bleu)
        
        # Codes des boutons d'action :

        self.btn_download = QPushButton("Télécharger les FITS")
        self.btn_download.clicked.connect(self.download)
        layout_gauche.addWidget(self.btn_download)

        self.btn_charger_fichier = QPushButton("Charger des FITS en local")
        self.btn_charger_fichier.clicked.connect(self.ouvrir_fichier)
        layout_gauche.addWidget(self.btn_charger_fichier)

        self.btn_generate = QPushButton("Générer l'image")
        self.btn_generate.clicked.connect(self.generate)
        layout_droite.addWidget(self.btn_generate)

        self.btn_save_as = QPushButton("Sauvegarder l'image")
        self.btn_save_as.clicked.connect(self.save_as)
        layout_droite.addWidget(self.btn_save_as)

        # Label et pixmap pour l'image actuel :

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout_centre.addWidget(self.label)

        self.setImage()
        
        # Pour afficher l'app :

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        self.show()

    # Fonctions :

    def ouvrir_fichier(self):
        self.open_local_fits.emit()
        self.setImage()

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

    def update_rouge(self) :
        self.update_rouge_signal.emit(self.slider_rouge.value())

    def update_vert(self) :
        self.update_vert_signal.emit(self.slider_vert.value())

    def update_bleu(self) :
        self.update_bleu_signal.emit(self.slider_bleu.value())