"""
Python equivalent of idl_plot.pro
Opens a FITS file, displays the image, and plots a middle-row intensity profile.
Requires: astropy, matplotlib, numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

file = 'my_image.fits'

# Read FITS file (equivalent to mrdfits)
with fits.open(file) as hdul:
    img = hdul[0].data
    hdr = hdul[0].header

# Print basic info (equivalent to IDL's 'help, img')
print(f"Image shape: {img.shape}, dtype: {img.dtype}")
print(f"NAXIS1={hdr.get('NAXIS1')}, NAXIS2={hdr.get('NAXIS2')}")

# Display image
fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.imshow(img, origin='lower', cmap='gray',
           vmin=np.percentile(img, 1), vmax=np.percentile(img, 99))
ax1.set_title('FITS Image')
ax1.set_xlabel('X Pixel')
ax1.set_ylabel('Y Pixel')
plt.tight_layout()

# Middle-row profile
ny = img.shape[0]
midrow = ny // 2
profile = img[midrow, :]

fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(profile)
ax2.set_xlabel('Pixel')
ax2.set_ylabel('Intensity')
ax2.set_title('Middle-row profile from FITS image')
plt.tight_layout()

plt.show()
