WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

MAP =[]

for i in range(10):
    temp = []
    for j in range(10):
        if j == 0 or j== 9 or i == 0 or i == 9:
            temp.append(0)
        else:
            temp.append(1)
    MAP.append(temp)