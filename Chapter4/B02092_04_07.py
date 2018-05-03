from scipy import misc
l = misc.ascent()
misc.imsave('ascent.png', l) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.gray()
plt.imshow(l)
plt.show()