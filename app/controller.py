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
        self.vue.save_as_signal.connect(self.fonc_save_as)

        self.vue.update_rouge_signal.connect(self.fonc_update_rouge)
        self.vue.update_vert_signal.connect(self.fonc_update_vert)
        self.vue.update_bleu_signal.connect(self.fonc_update_bleu)

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

    def fonc_save_as(self) :
        dossier = QFileDialog.getExistingDirectory(parent=self.vue, caption="Choisissez un dossier pour sauvegarder l'image",options=QFileDialog.Option.ShowDirsOnly)
        self.modele.save_as(dossier)

    def fonc_update_rouge(self, value: int):
        self.modele.updateRouge(value)

    def fonc_update_vert(self, value: int):
        self.modele.updateVert(value)

    def fonc_update_bleu(self, value: int):
        self.modele.updateBleu(value)