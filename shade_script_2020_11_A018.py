import math
import random

lst = [0] * 21
lst[1]= [1,1,1]
lst[2]= [1.618,0,1/1.618]
lst[3]= [1.618,0,-1/1.618]
lst[4]= [1,1,-1]
lst[5]= [1/1.618,1.618,0]
lst[6]= [0,1/1.618,1.618]
lst[7]= [1,-1,1]
lst[8]= [1,-1,-1]
lst[9]= [0,1/1.618,-1.618]
lst[10]= [-1/1.618,1.618,0]
lst[11]= [-1,1,1]
lst[12]= [0,-1/1.618,1.618]
lst[13]= [1/1.618,-1.618,0]
lst[14]= [0,-1/1.618,-1.618]
lst[15]= [-1,1,-1]
lst[16]= [-1.618,0,1/1.618]
lst[17]= [-1,-1,1]
lst[18]= [-1/1.618,-1.618,0]
lst[19]= [-1,-1,-1]
lst[20]= [-1.618,0,-1/1.618]

hen = [0] * 31
hen[1] = [1,2]
hen[2] = [2,3]
hen[3] = [3,4]
hen[4] = [4,5]
hen[5] = [5,1]
hen[6] = [1,6]
hen[7] = [2,7]
hen[8] = [3,8]
hen[9] = [4,9]
hen[10] = [5,10]
hen[11] = [6,11]
hen[12] = [6,12]
hen[13] = [7,12]
hen[14] = [7,13]
hen[15] = [8,13]
hen[16] = [8,14]
hen[17] = [9,14]
hen[18] = [9,15]
hen[19] = [10,15]
hen[20] = [10,11]
hen[21] = [11,16]
hen[22] = [12,17]
hen[23] = [13,18]
hen[24] = [14,19]
hen[25] = [15,20]
hen[26] = [16,17]
hen[27] = [17,18]
hen[28] = [18,19]
hen[29] = [19,20]
hen[30] = [20,16]


scene = xshade.scene()
scene.begin_creating()

s = 8

for i in range(1,30+1,1):

	rd = 50
	
	pt1 = hen[i][0]
	pt2 = hen[i][1]

	x1 = lst[pt1][0] * rd
	y1 = lst[pt1][1] * rd
	z1 = lst[pt1][2] * rd
	x2 = lst[pt2][0] * rd
	y2 = lst[pt2][1] * rd
	z2 = lst[pt2][2] * rd

	px = -x1+x2 
	py = -y1+y2 
	pz = -z1+z2 
	r =  math.sqrt(px*px + py*py + pz*pz)
	th = math.acos(pz / r)

	if math.sqrt(px * px + py * py) == 0:
		fi = 0
	else:
		if py >= 0:
			fi = 1 *  math.acos(px / math.sqrt(px * px + py * py))
		else:
			fi = -1 * math.acos(px / math.sqrt(px * px + py * py))

	dx = math.sin(th) *math.cos(fi) * (r/20)
	dy = math.sin(th) *math.sin(fi) * (r/20)
	dz = math.cos(th) * (r/20)

	cx = x1
	cy = y1
	cz = z1

	for ii in range(0,20+1,1):
		scene.create_primitive_sphere(None,3,True,s,s,[cx, cy, cz],s)
		cx += dx
		cy += dy
		cz += dz


scene.end_creating()

