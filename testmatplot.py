import matplotlib.pyplot as plt
import numpy as np
import imageio

imageList=[]
for i in range(30):
    image = np.random.rand(200,300)
    #imageList.append(image)
    plt.imshow(image,cmap="inferno")
    plt.pause(.1)
    plt.draw()
#plt.show()
#print("end")

"""
minGif = []
for filename in imageList:
    minGif.append(imageio.imread(filename))
imageio.mimsave('./movie.gif', minGif)
"""