import numpy as np

h = 60
w = 60
p = .3

land = np.random.choice(a=[False, True], size=(h, w), p=[1-p, p])
prev = None

def update(land):
    res = land.copy()
    for i in range(h):
        for j in range(w):
            cell = land[i,j]
            n = np.sum(land[max(i-1,0):min(i+2,h),max(j-1,0):min(j+2,w)])
            if cell:
                if n < 2 or n > 3:
                    res[i,j] = False
            else:
                if n == 3:
                    res[i,j] = True
    return res

while not np.array_equal(land, prev):
    prev = land
    land = update(land)
