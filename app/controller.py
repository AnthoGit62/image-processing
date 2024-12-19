# Seys Anthony & Prévost Louis

import vue , modele
from PyQt6.QtWidgets import QFileDialog

class controller() : 
    
    def __init__(self) :
        self.modele = modele.modele()
        self.vue = vue.vue()

        self.vue.open_local_fits.connect(self.fonc_open_local_fits)
        self.vue.generate_image_signal.connect(self.fonc_generate)
        self.vue.download_signal.connect(self.fonc_download)


    def fonc_open_local_fits(self) :
        try:
            chemin_rouge, _ = QFileDialog.getOpenFileName(self.vue, "Choisir le fichier FITS (Rouge)")
            chemin_vert, _ = QFileDialog.getOpenFileName(self.vue, "Choisir le fichier FITS (Vert)")
            chemin_bleu, _ = QFileDialog.getOpenFileName(self.vue, "Choisir le fichier FITS (Bleu)")

            if chemin_bleu and chemin_vert and chemin_rouge :
                self.modele.charger_fichier_fits(chemin_rouge , chemin_vert , chemin_bleu)
        except ValueError as e:
            print(f"Erreur lors du chargement des produits: {e}")


    def fonc_generate(self) :
        self.modele.generate()

    
    def fonc_download(self , v_ra , v_dec , v_rad , v_sat) :
        self.modele.download(v_ra , v_dec , v_rad , v_sat)