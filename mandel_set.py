import matplotlib.pyplot as plt
import numpy as np


def mand_iter(coordZ, limit=4.0, maxIter = 50):
    # f_C(z) = z**2 + C
    # z_init = 0
    z = 0
    i=0
    while (i<maxIter) and (abs(z) < limit):
        z = z**(2) + coordZ
        i+=1
    return i


origin = (-3,-2)
largeur = 4
resolution = 5000
imag= np.full((resolution,resolution),0)

for x in range(resolution):
    for y in range(resolution):
        imag[y][x]=mand_iter(complex((x/resolution)*largeur + origin[0],(y/resolution)*largeur + origin[1]))

#print(imag)
plt.imshow(imag,cmap='inferno')
plt.show()