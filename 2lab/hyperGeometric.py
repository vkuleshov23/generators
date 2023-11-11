from generator import *

def MD(_lambda, A, B, k, m, disp, N, D, n, exp_d, unf_d, erlang_d, norm_d_X1, norm_d_X2, hg_d):
    print("M(exp distribution):", 1/_lambda, "\tM_pr:", M(exp_d))
    print("D(exp distribution):", 1/(_lambda**2), "\tD_pr:", Disp(exp_d, M(exp_d)))
    
    print("M(uniform distribution):", A+(B-A)/2, "\tM_pr:", M(unf_d))
    print("D(uniform distribution):", ((B-A)**2)/12, "\tD_pr:", Disp(unf_d, M(unf_d)))
    
    print("M(erlang distribution):", k/_lambda, "\tM_pr:", M(erlang_d))
    print("D(erlang distribution):", k/(_lambda**2), "\tD_pr:", Disp(erlang_d, M(erlang_d)))

    print("M(normal distribution):", m, "\tM_prX1:", M(norm_d_X2), "M_prX2:", M(norm_d_X2))
    print("D(normal distribution):", disp**2, "\tD_prX1:", Disp(norm_d_X1, M(norm_d_X1)), "D_prX1:", Disp(norm_d_X2, M(norm_d_X2)))

    print("M(hyper geometric distribution):", n*D/N, "\tM_pr:", MHGD(hg_d))
    print("D(hyper geometric distribution):", (n*(D/N)*(1-(D/N))*(N-n))/(N-1), "\tD_pr:", DHGD(hg_d, MHGD(hg_d)))

def exp_distrib(z, _lambda):
	return -(1/_lambda)*np.log(z)

def uniform(A, B, z):
    return (A + (B-A)*z)

def erlang(k, _lambda):
    summ = 0
    for i in range(1, k):
	    summ += -(1/_lambda)*np.log(mcLaren_Marsagli_gen())
    return summ

def Box_Muller(m, disp):
	z1 = mcLaren_Marsagli_gen()
	z2 = mcLaren_Marsagli_gen()
	x1 = np.sqrt(-2*np.log(z1))*np.sin(2*np.pi*z2)
	x2 = np.sqrt(-2*np.log(z1))*np.cos(2*np.pi*z2)
	# x1 = x1/np.max(x1)
	# x2 = x2/np.max(x2)
	return (m+(x1*disp)),(m+(x2*disp))

def check_uniformity_hyperGeom(Z):
	for i in range(len(Z)):
		plt.bar(range(len(Z[i])), Z[i])
	plt.show()

def Binc(bcs,n,k):
    if (k>n):   return 0
    if k>n//2:  k=n-k 
    if k==0:    return 1
    if k==1:    return n
    while len(bcs)<n-3:
        for i in range(len(bcs),n-3):
            r=[]
            for j in range(2,i//2+3):
                r.append(Binc(bcs,i+3,j-1)+Binc(bcs,i+3,j))
            bcs.append(r)
    r=bcs[n-4]
    if len(r)<k-1:
        for i in range(len(r),k-1):
            r.append(Binc(bcs,n-1,k-1)+Binc(bcs,n-1,k))
    return bcs[n-4][k-2]

def MHGD(z):
	m = 0
	for i in range(len(z)):
		m += z[i] * i
		# print(m)
	return m

def DHGD(z, M):
	M2 = 0
	for i in range(len(z)):
		M2 += z[i] * i**2
	d = M2 - M**2
	# d = 0
	# for i in range(len(z)):
	# 	d += ((i-M)**2)*z[i]
	return d

def HyperGeometritDistrib(N, D, n):
	x = np.zeros(n)
	if(n > D):
		x = np.zeros(D)
	for k in range(len(x)):
		c1 = Binc([], D, k)
		c2 = Binc([],N-D, n-k)
		c3 = Binc([],N,n)
		x[k] = c1*c2/c3
	return x


z = mcLaren_Marsagli_gen()

_lambda = 0.2

A = 10
B = 100

k = 10

m = 100
disp = 20

N = 30
D = 15
n = 20

exp_d = exp_distrib(z, _lambda)
unf_d = uniform(A, B, z)
erlang_d = erlang(k, _lambda)
norm_d_X1, norm_d_X2 = Box_Muller(m,disp)
hg_d1 = HyperGeometritDistrib(N, D, n)

MD(_lambda, A, B, k, m, disp, N, D, n, exp_d, unf_d, erlang_d, norm_d_X1, norm_d_X2, hg_d1)

check_uniformity_all(exp_d)
check_uniformity_all(unf_d)
check_uniformity_all(erlang_d)
check_uniformity_all(norm_d_X1)
check_uniformity_all(norm_d_X2)
check_uniformity_hyperGeom([hg_d1])

# hg_d2 = HyperGeometritDistrib(60, 50, 20)
# hg_d3 = HyperGeometritDistrib(60, 20, 20)
# hg_d4 = HyperGeometritDistrib(60, 20, 30)
# hg_d5 = HyperGeometritDistrib(60, 20, 40)
# hg_d6 = HyperGeometritDistrib(60, 20, 50)
# hg_d7 = HyperGeometritDistrib(60, 20, 60)
# check_uniformity_hyperGeom([hg_d1, hg_d2, hg_d3, hg_d4, hg_d5, hg_d6, hg_d7])

