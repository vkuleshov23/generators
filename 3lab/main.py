import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def _split(p):
	values = np.zeros(len(p))
	probs = np.zeros(len(p))
	for i in range(len(p)):
		values[i] = p[i][0]
		probs[i] = p[i][1]
	return values, probs

def m(sample, probs, values):
	print("M:", np.sum(probs*values))
	print("M_pr:", np.sum(sample)/len(sample))

def D(sample, probs, values):
	m2 = np.sum(probs*values)**2
	print("D:", np.sum(probs*(values**2))-m2)
	m_x2 = np.sum(sample**2)/len(sample)
	m_2 = (np.sum(sample)/len(sample))**2
	print("D_pr:", m_x2-m_2)

def hist_(v, p, p_pr):
	filename = "discr.csv"
	f = open(filename, "w")
	f.write("values,propabilites,propabilites_pr\n")
	for i in range(len(v)):
		f.write(str(v[i]) + "," + str(p[i]) + "," + str(p_pr[i]) + "\n")
	f.close()
	data = pd.read_csv(filename)
	ax = sns.barplot(x="values", y="propabilites", data=data)
	width_scale = 0.45
	for bar in ax.containers[0]:
	    bar.set_width(bar.get_width() * width_scale)
	ax2 = ax.twinx()
	sns.barplot(x="values", y="propabilites_pr", data=data, hatch="**", ax=ax2)
	for bar in ax2.containers[0]:
	    x = bar.get_x()
	    w = bar.get_width()
	    bar.set_x(x + w * (1- width_scale))
	    bar.set_width(w * width_scale)
	plt.show()


def hist(sample, values, probs):
	side, count = np.unique(sample, return_counts=True)
	ps = count / len(sample)
	# Plot the results
	hist_(values, probs, ps)

NUM_ROLLS = 500
p = [[-88.0, 0.186], [-66.5, 0.246], [-26.2, 0.139], [-4.5, 0.157], [-0.3, 0.207], [65.0, 0.015], [65.8, 0.050]]
# p.sort(key = lambda x: x[1])
# print(p)
values, probs = _split(p)
# values = [-88.0, -66.5, -26.2, -4.5, -0.3, 65.0, 65.8]
# probs = [0.186, 0.246, 0.139, 0.157, 0.207, 0.015, 0.050]

# Draw a weighted sample
sample = np.random.choice(values, NUM_ROLLS, p=probs)
print("Первые 30 значений:\n", sample[:30])
m(sample, probs, values)
D(sample, probs, values)
hist(sample, values, probs)