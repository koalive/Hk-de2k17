#V
#E
#R
#C
#X


import numpy as np

S = np.array([50, 50, 80, 30, 110])
R = np.array([[3, 0, 1500], [0, 1, 1000], [4, 0, 500], [1, 0, 1000]])
latmat = np.array([[0, 100], [2, 200], [1, 300]])

C = [0, 0, 0]
Cnames = {}
maxSize = 100

#R = np.array([2, 1], [3, 4])
#print(R)

#print(R[:, 2])

Rh = R[R[:,2].argsort()]#np.sort(R, 0)

print(Rh)


#print(Rh[-1,-1])

n = Rh.shape[0]
#print(n)


#print(latmat)

lh = latmat[latmat[:,1].argsort()]

Rsort = Rh
Lsort = lh


print(lh)

for i in range(n-1, -1, -1):
	#print(i)
	#print(Rh[i, -1])
	
	endpoint = Rsort[i, 1]
	#print(e)
	
	# GET ENDPOINT L MATRIX

	videoIndex = Rsort[i, 0]

	videoSize = S[videoIndex]

	





	vi = Rh[i, 0]
	vs = S[vi]
	print(vs)
	print(vi in Cnames)
	if e not in Cnames:
		Cnames[e] = []
	Cnames[e].append(vi)
print(Cnames)




print(np.mt)