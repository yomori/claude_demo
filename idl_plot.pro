; Simple IDL example: open a FITS file and plot the image

file = 'my_image.fits'

; Requires the IDL Astronomy User's Library
img = mrdfits(file, 0, hdr)

; Print some basic info
help, img
print, sxpar(hdr, 'NAXIS1'), sxpar(hdr, 'NAXIS2')

; Display image
window, 0, xsize=800, ysize=800
tvscl, img

; Make a simple line plot through the middle row
ny = n_elements(img[0, *])
midrow = ny / 2

profile = img[*, midrow]

window, 1, xsize=800, ysize=500
plot, profile, $
    xtitle='Pixel', $
    ytitle='Intensity', $
    title='Middle-row profile from FITS image'
