import random
import matplotlib.pyplot as plt

CPT_A = [[1, 1, 1, 0.8873, 0.1127],
		[1, 1, 0, 0.9921, 0.0079],
		[0, 1, 1, 0.2727, 0.7273],
        [0, 1, 0, 0.8517, 0.1429]]

CPT_B = [[1, 0.9130, 0.0870],
		 [0, 0.0184, 0.9816]]

CPT_D = [[1, 1, 1, 0.027, 0.973],
		 [1, 1, 0, 0.692, 0.308],
		 [0, 1, 1, 0.308, 0.692],
		 [0, 1, 0, 0.973, 0.027]]

CPT_E = [[1, 1, 0.1, 0.9],
		 [1, 0, 0.9, 0.1]]


def plot(ratioList):
	plt.plot(ratioList, 'bo')
	plt.ylabel('B Ratio')
	plt.show()


def main():

	for i in range(0, 5):
		nodes = []
		for j in range(0, 5):
			nodes.append(random.randint(0, 1))

		bCounter = 0
		ratioList = []

		for j in range(1, 50001):

			# A
			rand_guess = random.randint(0, 100) / 100
			for k in range(0, len(CPT_A)):

				if (CPT_A[k][0] == nodes[1]) and (CPT_A[k][2] == nodes[3]):
					if nodes[0] == 1:
						if rand_guess > CPT_A[k][3]:
							nodes[0] = 0
					elif nodes[0] == 0:
						if rand_guess > CPT_A[k][4]:
							nodes[0] = 1

			# B
			rand_guess = random.randint(0, 100) / 100
			for k in range(0, len(CPT_B)):

				if CPT_B[k][0] == nodes[0]:
					if nodes[1] == 1:
						if rand_guess > CPT_B[k][1]:
							nodes[1] = 0
					elif nodes[1] == 0:
						if rand_guess > CPT_B[k][2]:
							nodes[1] = 1

			# D
			rand_guess = random.randint(0, 100) / 100
			for k in range(0, len(CPT_D)):

				if (CPT_D[k][0] == nodes[0]) and (CPT_D[k][2] == nodes[4]):
					if nodes[3] == 1:
						if rand_guess > CPT_D[k][3]:
							nodes[3] = 0
					elif nodes[3] == 0:
						if rand_guess > CPT_D[k][4]:
							nodes[3] = 1

			# E
			rand_guess = random.randint(0, 100) / 100
			for k in range(0, len(CPT_E)):

				if CPT_E[k][1] == nodes[3]:
					if nodes[4] == 1:
						if rand_guess > CPT_E[k][2]:
							nodes[4] = 0
					elif nodes[4] == 0:
						if rand_guess > CPT_E[k][3]:
							nodes[4] = 1

			if nodes[1] == 1:
				bCounter += 1

			if j % 200 == 0:
				ratioList.append(bCounter/j)

		print(ratioList)
		plot(ratioList)


main()
