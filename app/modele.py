# Seys Anthony & Prévost Louis

from PyQt6.QtWidgets import QMessageBox
from astropy.coordinates import SkyCoord
from astroquery.mast import Observations
import matplotlib.pyplot as plt
from scipy.ndimage import zoom
from astropy import units as u
from astropy.io import fits
import pandas as pd
import numpy as np
import os

class modele:

    def __init__(self):

        self.rouge = np.zeros((100, 100))
        self.vert = np.zeros((100, 100))
        self.bleu = np.zeros((100, 100))

        self.rouge_calibre = np.zeros_like(self.rouge)
        self.vert_calibre = np.zeros_like(self.vert)
        self.bleu_calibre = np.zeros_like(self.bleu)


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

        self.facteur_rouge : int = 2
        self.facteur_vert : int = 1
        self.facteur_bleu : int = 0.5
        
        self.generate()

    def normalisation(self, data, min=1, max=99):
        min = np.percentile(data, min)
        max = np.percentile(data, max)
        scaled_data = np.clip(data, min, max)

        return (scaled_data - min) / (max - min + 1e-8)

    def resize_images(self):
        if self.rouge.shape != self.vert.shape or self.rouge.shape != self.bleu.shape:
            target_shape = min(self.rouge.shape, self.vert.shape, self.bleu.shape)
            self.rouge = zoom(self.rouge, (target_shape[0] / self.rouge.shape[0], target_shape[1] / self.rouge.shape[1]))
            self.vert = zoom(self.vert, (target_shape[0] / self.vert.shape[0], target_shape[1] / self.vert.shape[1]))
            self.bleu = zoom(self.bleu, (target_shape[0] / self.bleu.shape[0], target_shape[1] / self.bleu.shape[1]))

    def generate(self):
        self.resize_images()

        self.rouge = self.normalisation(self.rouge)
        self.vert = self.normalisation(self.vert)
        self.bleu = self.normalisation(self.bleu)

        # Obligé de garder des valeurs du début sinon on a des valeurs abérante a force de *
        self.rouge_calibre = self.rouge
        self.vert_calibre = self.vert
        self.bleu_calibre = self.bleu

        self.rouge_calibre = np.clip(self.rouge * self.facteur_rouge, 0, 1)
        self.vert_calibre = np.clip(self.vert * self.facteur_vert, 0, 1)
        self.bleu_calibre = np.clip(self.bleu * self.facteur_bleu, 0, 1)

        self.compil_image()

    def compil_image(self) :
        image_final = np.stack((self.rouge_calibre ,self.vert_calibre , self.bleu_calibre) , axis=-1)

        plt.imshow(image_final)
        plt.axis('off')

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'last_image')

        plt.savefig(image_path, bbox_inches='tight', pad_inches=0)

    def updateRouge(self , newvalue) :
        self.facteur_rouge = newvalue

    def updateVert(self , newvalue) :
        self.facteur_vert = newvalue

    def updateBleu(self , newvalue) :
        self.facteur_bleu = newvalue

    def save_as(self ,path : str) : 
        plt.savefig(path, bbox_inches='tight', pad_inches=0)

# Code pour le download

    def download(self , v_ra , v_dec , v_rad , v_sat) :
        ra = v_ra
        dec = v_dec
        radius = v_rad
        satellite_name = v_sat
        obs_filtered = self.get_filtered_observations(ra, dec, radius, satellite_name)
        if len(obs_filtered) > 0:
            obs_ids = pd.Series(obs_filtered['obs_id'], dtype=str)
            most_common_prefix = self.get_most_common_prefix(obs_ids)
            mask = obs_ids.str.startswith(most_common_prefix).to_numpy()
            obs_filtered_by_prefix = obs_filtered[mask]
            obs_filtered_by_prefix_sorted = self.get_sorted_observations(obs_filtered_by_prefix, ra, dec)
            download_directory = "image_test/"
            self.download_fits_files(obs_filtered_by_prefix_sorted, download_directory)

    def get_filtered_observations(self , ra, dec, radius, satellite_name):
        obs = Observations.query_object(f"{ra} {dec}", radius=radius)
        return obs[obs['obs_collection'] == satellite_name]

    def get_most_common_prefix(self , obs_ids):
        prefixes = obs_ids.str.extract('(^[a-zA-Z0-9_]+)', expand=False)
        return prefixes.value_counts().idxmax()

    def get_sorted_observations(self , obs_filtered_by_prefix, ra, dec):
        coord = SkyCoord(ra, dec, unit=(u.deg, u.deg), frame='icrs')
        obs_coords = SkyCoord(obs_filtered_by_prefix['s_ra'], obs_filtered_by_prefix['s_dec'], unit=(u.deg, u.deg), frame='icrs')
        distances = coord.separation(obs_coords)
        obs_filtered_by_prefix['distance'] = distances
        return obs_filtered_by_prefix[np.argsort(obs_filtered_by_prefix['distance'])] 

    def download_fits_files(self, obs_filtered_by_prefix_sorted, download_directory):
        os.makedirs(download_directory, exist_ok=True)
        fits_downloaded = 0
        first_file = True
        file_sizes = []

        for obs in obs_filtered_by_prefix_sorted:
            if fits_downloaded >= 3:
                break
            product_list = Observations.get_product_list(obs)
            science_products = Observations.filter_products(product_list, productType="SCIENCE", extension="fits")
            if len(science_products) > 0:
                file_size = science_products[0]['size']
                file_size_mb = file_size / (1024 * 1024)
                QMessageBox.information(None, "Taille du fichier", f"Taille du fichier : {file_size_mb:.2f} MB")

                if first_file:
                    reply = QMessageBox.question(
                        None,
                        "Confirmation de téléchargement",
                        f"Voulez-vous télécharger les fichiers ? Ils pèsent {file_size_mb:.2f} MB.",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    )
                    if reply == QMessageBox.StandardButton.Yes:
                        Observations.download_products(science_products[:3], download_dir=download_directory, cache=False)
                        fits_downloaded += 1
                        file_sizes.append(file_size)
                        first_file = False
                    else:
                        QMessageBox.warning(
                            None,
                            "Téléchargement annulé",
                            "Téléchargement annulé. Essayez un autre satellite qui aura une image moins lourde."
                        )
                        break
                else:
                    Observations.download_products(science_products[:3], download_dir=download_directory, cache=False)
                    fits_downloaded += 1
                    file_sizes.append(file_size)

        if len(file_sizes) == 3 and len(set(file_sizes)) == 1:
            QMessageBox.information(None, "Résultat", "Les trois fichiers téléchargés ont la même taille.")
        else:
            QMessageBox.information(None, "Résultat", "Les fichiers téléchargés n'ont pas la même taille.")