from astropy.io import fits
import matplotlib.pyplot as plt 

data = fits.getdata('image-processing/Tarantula_Nebula-sii.fit')

plt.imshow(data , cmap='gray')
plt.colorbar()
plt.show()