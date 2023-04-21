import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio
import skimage
import skimage.draw
from PIL import Image

fname = 'bird.jpeg'

image = Image.open(fname).convert("L")

plant_seedling = np.asarray(image)

plt.imshow(plant_seedling, cmap='gray', vmin=0, vmax=255)
plt.show()

histogram, bin_edges = np.histogram(plant_seedling, bins=256)

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")

plt.plot(bin_edges[0:-1], histogram)  # <- or here

plt.show()