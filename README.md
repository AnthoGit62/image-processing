# 🌌 Image Processing - Traitement d'images astronomiques FITS

> **Application PyQt6 pour le traitement et la visualisation d'images astronomiques**

[![Projet Universitaire](https://img.shields.io/badge/Projet-Universitaire-blue.svg)](https://github.com)
[![Date](https://img.shields.io/badge/Date-Décembre%202024-green.svg)](https://github.com)
[![Python](https://img.shields.io/badge/Language-Python-yellow.svg)](https://github.com)
[![PyQt6](https://img.shields.io/badge/Framework-PyQt6-brightgreen.svg)](https://github.com)

## 👥 Équipe de développement

- **SEYS Anthony** [@Anthony](https://github.com/AnthoGit62)
- **PREVOST Louis** [@Louis Prévost](https://github.com/louisprvst)

---

## 📋 Table des matières

- [Description](#-description)
- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Captures d'écran](#-captures-décran)
- [Technologies utilisées](#-technologies-utilisées)

---

## 🎯 Description

**Image Processing** est une application de bureau développée en Python pour le traitement et la visualisation d'images astronomiques au format FITS (Flexible Image Transport System). L'application permet de composer des images en couleur RGB à partir de fichiers FITS, de télécharger des données astronomiques depuis des bases en ligne, et d'ajuster la colorisation en temps réel.

## ✨ Fonctionnalités

- 📂 **Chargement local** : Importation de fichiers FITS (canaux Rouge, Vert, Bleu)
- 🌐 **Téléchargement astronomique** : Récupération d'images depuis des catalogues en ligne
- 🎨 **Ajustement colorimétrique** : Modification interactive des paramètres de couleur
- 🔭 **Recherche par coordonnées** : Saisie des coordonnées RA/DEC pour cibler un astre
- 🛰️ **Multi-satellites** : Support de différentes missions spatiales
- 🖼️ **Visualisation temps réel** : Génération et affichage instantané des images

## 🔧 Prérequis

### Système requis

- **Python 3.8+** installé sur votre système
- **pip** (gestionnaire de paquets Python)

### Bibliothèques Python nécessaires

L'application nécessite les bibliothèques suivantes :

```
PyQt6
astropy
astroquery
numpy
pandas
scipy
```

## 🚀 Installation

### 1️⃣ Cloner le projet

```bash
git clone <url-du-projet>
cd Image-Processing
```

### 2️⃣ Installer les dépendances

Installez toutes les bibliothèques requises avec pip :

```bash
pip install PyQt6 astropy astroquery numpy pandas scipy
```

Ou utilisez un fichier requirements.txt (si disponible) :

```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application

Naviguez vers le dossier de l'application et exécutez le fichier principal :

```bash
cd app
python main.py
```

---

## 📖 Utilisation

### 1️⃣ Charger des fichiers FITS en local

#### Étapes :

1. Cliquez sur le bouton **"Charger des FITS en local"**
2. Sélectionnez successivement les fichiers FITS correspondant aux canaux :
   - **Rouge** (Red)
   - **Vert** (Green)
   - **Bleu** (Blue)
3. L'image composite s'affichera après quelques secondes de traitement

> 💡 **Astuce** : Assurez-vous que vos fichiers FITS sont bien calibrés et alignés pour un résultat optimal.

---

### 2️⃣ Télécharger des fichiers FITS depuis un catalogue

#### Paramètres requis :

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| **RA** | Ascension droite (Right Ascension) | `10h 47m 00s` ou `161.75°` |
| **DEC** | Déclinaison (Declination) | `+12° 30' 00"` ou `+12.5°` |
| **Radius** | Rayon de recherche en degrés | `0.001` (précision recommandée) |
| **Satellite** | Mission spatiale à utiliser | HST, Spitzer, JWST, etc. |

#### Étapes :

1. Remplissez les champs **RA** et **DEC** avec les coordonnées de l'astre
2. Définissez le **radius** (valeur recommandée : `0.001` pour une précision optimale)
3. Sélectionnez le **satellite** souhaité dans le menu déroulant
4. Cliquez sur **"Télécharger"**
5. L'image sera automatiquement récupérée et affichée

> ⚠️ **Attention** : Le téléchargement peut prendre plusieurs secondes selon la taille des données et votre connexion internet.

---

### 3️⃣ Modifier la colorisation de l'image

#### Personnalisation des couleurs :

1. Utilisez les **sliders** pour ajuster les paramètres colorimétriques :
   - Intensité des canaux RGB
   - Contraste
   - Luminosité
   - Saturation (selon l'implémentation)

2. Après avoir modifié les valeurs, cliquez sur **"Générer l'image"**

3. L'image sera rechargée avec vos nouveaux paramètres

> 🎨 **Conseil** : Expérimentez avec différentes valeurs pour faire ressortir les détails de l'image astronomique.

---

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| **PyQt6** | Interface graphique (GUI) |
| **Astropy** | Manipulation de fichiers FITS et calculs astronomiques |
| **Astroquery** | Requêtes vers des bases de données astronomiques |
| **NumPy** | Calculs numériques et manipulation de matrices |
| **Pandas** | Traitement de données tabulaires |
| **SciPy** | Fonctions scientifiques avancées |

---

## 🐛 Dépannage

### Problèmes courants

**L'image ne s'affiche pas après le chargement**
- Vérifiez que les fichiers FITS sont valides
- Assurez-vous que les trois canaux (RGB) ont la même dimension

**Erreur lors du téléchargement**
- Vérifiez votre connexion internet
- Assurez-vous que les coordonnées RA/DEC sont correctes
- Essayez d'augmenter légèrement le radius

**L'application se ferme inopinément**
- Vérifiez que toutes les dépendances sont installées
- Consultez les logs d'erreur dans le terminal

---

## 🤝 Contribution

Ce projet est un travail universitaire. Pour toute question ou suggestion, contactez les membres de l'équipe.

---

## 📚 Ressources utiles

- [Documentation Astropy](https://docs.astropy.org/)
- [Documentation PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Format FITS - NASA](https://fits.gsfc.nasa.gov/)
- [Astroquery Documentation](https://astroquery.readthedocs.io/)

---
