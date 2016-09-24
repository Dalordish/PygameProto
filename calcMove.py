import numpy as np
#                      Motor A    Motor B      Motor C         Motor A Motor B      Motor C
#120 120 0

#a:29 in youtube
# 30, 120+30, 120*2 + 30
# 30, 150,270


const = np.matrix([ [np.sin(np.deg2rad(30)), np.sin(np.deg2rad(150)) , np.sin(np.deg2rad(270)) ] ,
[np.cos(np.deg2rad(30)),np.cos(np.deg2rad(150)), np.cos(np.deg2rad(270))], [1,1,1] ])
vectors = np.matrix([ [100] , [0], [-100] ])
print("---------")
fin = const*vectors
print(fin)

#print(np.sin(np.deg2rad(30)))