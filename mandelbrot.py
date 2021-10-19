import matplotlib.pyplot as plt
import numpy as np

def get_iter(comp, thresh=5,maxSteps=25):
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=comp
    i=1
    while i<maxSteps and (z*z.conjugate()).real<thresh:
        z = z*z +comp
        #print(i,z)
        i+=1
    return i

#print(get_iter(2j))
print("yo")

#nx = 2.48 / (n-1)
#ny = 2.26 / (n-1)
#testlamb = lambda x,y: (x*x, y+1,x+y)
testlamb = lambda x,y: np.complex(x,y)

for x in range(10):
    for y in range(10):
        print(testlamb(x,y))



"""
def plotter(n, thresh, maxSteps=25):
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)
    img=np.full((n,n), 255)
    for x in range(n):
        for y in range(n):
            print(mapper(x,y))
            it = get_iter(complex(*mapper(x,y)), thresh=thresh, maxSteps=maxSteps)
            img[y][x] = 255 - it
    return img

n=100
img = plotter(n, thresh=4, maxSteps=50)
#plt.imshow(img, cmap="plasma")
plt.imshow(img)
#plt.axis("off")
plt.show()

"""