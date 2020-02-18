def solve(data):
	nums = open(data, "r").read().replace('\n', ' ')
	k = 5
	m = 4
	inp_tmp = list(map(float, nums.split()))
	p = [inp_tmp[i: i+m] for i in range(0, len(inp_tmp), m)]
	n = len(p)

	def dist(a, b):
		return sum([(a[i] - b[i]) ** 2 for i in range(m)])

	center = p[:k]

	def closest(p):
		x = 0
		d = dist(p, center[0])
		for i in range(1, k):
			_d = dist(p, center[i])
			if _d < d:
				d = _d
				x = i
		return x

	def average(cluster):
		a = [0.0 for i in range(m)]
		for c in cluster:
			a = [a[i] + c[i] for i in range(m)]
		nc = len(cluster)
		a = [a[i] / nc for i in range(m)]
		return a

	def iterate():
		assign = [closest(t) for t in p]
		for i in range(k):
			center[i] = average([p[j] for j in range(n) if assign[j] == i])

	for i in range(1110):
		iterate()

	for t in center:
		print(" ".join(["{}".format(round(t[i], 3)) for i in range(m)]))



solve("data2.txt")