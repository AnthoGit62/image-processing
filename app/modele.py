# Seys Anthony & Prévost Louis

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.ndimage import zoom  # Pour redimensionner les images

class modele:

    def __init__(self):
        self.rouge = None
        self.vert = None
        self.bleu = None

    def charger_fichier_fits(self, r, v, b):
        try:  # Pour charger le fichier fits rouge
            with open(r, 'r') as f:
                self.rouge = fits.getdata(r)
                self.rouge = np.nan_to_num(self.rouge)
        except Exception as e:
            print(f"Erreur lors du chargement du fichier rouge: {e}")

        try:  # Pour charger le fichier fits vert
            with open(v, 'r') as f:
                self.vert = fits.getdata(v)
                self.vert = np.nan_to_num(self.vert)
        except Exception as e:
            print(f"Erreur lors du chargement du fichier vert: {e}")

        try:  # Pour charger le fichier fits bleu
            with open(b, 'r') as f:
                self.bleu = fits.getdata(b)
                self.bleu = np.nan_to_num(self.bleu)
        except Exception as e:
            print(f"Erreur lors du chargement du fichier bleu: {e}")

    def normalisation(self, data, min=1, max=99):
        min = np.percentile(data, min)
        max = np.percentile(data, max)
        scaled_data = np.clip(data, min, max)
        return (scaled_data - min) / (max - min + 1e-8)

    def resize_images(self):
        if self.rouge.shape != self.vert.shape or self.rouge.shape != self.bleu.shape:
            # Redimensionner les canaux pour avoir les mêmes dimensions
            target_shape = min(self.rouge.shape, self.vert.shape, self.bleu.shape)
            self.rouge = zoom(self.rouge, (target_shape[0] / self.rouge.shape[0], target_shape[1] / self.rouge.shape[1]))
            self.vert = zoom(self.vert, (target_shape[0] / self.vert.shape[0], target_shape[1] / self.vert.shape[1]))
            self.bleu = zoom(self.bleu, (target_shape[0] / self.bleu.shape[0], target_shape[1] / self.bleu.shape[1]))

    def generate(self):
        self.resize_images()

        # Normalisation des canaux
        self.rouge = self.normalisation(self.rouge)
        self.vert = self.normalisation(self.vert)
        self.bleu = self.normalisation(self.bleu)

        # Application des filtres
        self.rouge *= 2
        self.vert *= 1
        self.bleu *= 0.5

        # Clipping des valeurs
        self.rouge = np.clip(self.rouge, 0, 1)
        self.vert = np.clip(self.vert, 0, 1)
        self.bleu = np.clip(self.bleu, 0, 1)

        # Empilement des canaux
        image_final = np.stack((self.rouge, self.vert, self.bleu), axis=-1)

        # Affichage et sauvegarde de l'image
        plt.imshow(image_final)
        plt.axis('off')

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'image')

        plt.savefig(image_path)
        print(f"Image sauvegardée sous {image_path}")
