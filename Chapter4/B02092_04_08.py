import scipy
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np

ascent = scipy.misc.ascent()

ascent = scipy.misc.ascent()
lx, ly = ascent.shape
crop_ascent = ascent[int(lx/4):-int(lx/4), int(ly/4):-int(ly/4)]
crop_eyes_ascent = ascent[int(lx/2):-int(lx/2.2), int(ly/2.1):-int(ly/3.2)]
flip_ud_ascent = np.flipud(ascent)
rotate_ascent = ndimage.rotate(ascent, 45)

# Four axes, returned as a 2-d array
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(ascent, cmap=plt.cm.gray)
axarr[0, 0].axis('off')
axarr[0, 0].set_title('Original ascent Image')

axarr[0, 1].imshow(crop_ascent, cmap=plt.cm.gray)
axarr[0, 1].axis('off')
axarr[0, 1].set_title('Cropped ascent')

axarr[1, 0].imshow(crop_eyes_ascent, cmap=plt.cm.gray)
axarr[1, 0].axis('off')
axarr[1, 0].set_title('ascent Cropped Eyes')

axarr[1, 1].imshow(rotate_ascent, cmap=plt.cm.gray)
axarr[1, 1].axis('off')
axarr[1, 1].set_title('45 Degree Rotated ascent')

plt.show()
