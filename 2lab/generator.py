import random
import numpy as np
import matplotlib.pyplot as plt

def rand_sequence(n):
	seq = np.zeros(n)
	for i in range(n-1):
		seq[i] = random.random()
	return seq

def mcLaren_Marsagli_gen():
	n = 800000
	k = 399999
	x = rand_sequence(n)
	y = rand_sequence(n)
	v = x[:k]
	return mcLaren_Marsagli(k,x,y,v)
	# return np.array([np.random.uniform() for i in range(400000)])

def mcLaren_Marsagli(k, x, y, v):
	z = np.zeros(k)
	for i in range(k):
		j = int(np.floor(y[i]*k))
		z[i] = v[j]
		v[j] = x[k+i]
	return z

def mathExpectationEstimation(z):
	M = 0.5
	zM = np.sum(z)/len(z)
	print("Theory math expectation:\n" + str(M) + "\nMcLaren-Marsagli math expectation:\n" + str(zM))
	return M

def M(z):
	return np.sum(z)/len(z)

def varianceEstimation(z, M):
	D = 1/12
	zD = np.sum(np.power(z-M,2))/len(z)
	print("Theory variance: " + str(D) + "\nMcLaren-Marsagli variance: " + str(zD))
	return D

def Disp(z, M):
	return np.sum(np.power(z-M,2))/len(z)

def check_uniformity(z):
	Z = np.floor(z*10)
	freqs = np.zeros(int(np.max(Z)+1))
	for i in range(len(Z)):
		freqs[int(Z[i])] += 1
	plt.bar(range(len(freqs)), freqs)
	plt.show()

def check_uniformity_all(z):
	Z = np.floor(z)
	freqs = np.zeros(int(np.max(Z)+1))
	for i in range(len(Z)):
		freqs[int(Z[i])] += 1
	plt.bar(range(len(freqs)), freqs)
	plt.show()

def check_uniformity_shift(z, shift):
	Z = np.floor(z*shift)
	freqs = np.zeros(int(np.max(Z)+1))
	for i in range(len(Z)):
		freqs[int(Z[i])] += 1
	plt.bar(range(len(freqs)), freqs)
	plt.show()

def correlation(z, s):
	SUM = np.zeros(len(z))
	# SUM = np.multiply(z[0:len(z)-s], z [s:])
	for i in range(s+10, len(z)-s):
		SUM[i] = ( (12/(i-s)) * np.sum( np.multiply(z[0:i-s], z[s:i]) ) ) - 3
	return SUM

def plot_correlation(z):
	R2 = correlation(z, 2)
	R5 = correlation(z, 5)
	R10 = correlation(z, 10)
	plt.plot(R2)
	plt.plot(R5)
	plt.plot(R10)
	# plt.plot([-0.1, 0.1])	
	plt.grid()
	plt.show()

# n = 80192
# k = 40000
# x = rand_sequence(n)
# y = rand_sequence(n)
# v = x[:k]
# z = mcLaren_Marsagli(k, x, y, v)
# M = mathExpectationEstimation(z)
# D = varianceEstimation(z, M)
# check_uniformity(z)
# plot_correlation(z)