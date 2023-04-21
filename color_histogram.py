import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio
import skimage
import skimage.draw
from PIL import Image

fname = 'bird.jpeg'

colors = ("red", "green", "blue")

image = Image.open(fname)

plant_seedling = np.asarray(image)

for channel_id, color in enumerate(colors):
    histogram, bin_edges = np.histogram(
        plant_seedling[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=color)


plt.title("Color Histogram")
plt.xlabel("Color value")
plt.ylabel("Pixel count")

plt.plot(bin_edges[0:-1], histogram)  # <- or here

plt.show()