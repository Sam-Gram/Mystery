def checkAnswer(num, list):
	if sum(list) is num:
		return True
	else:
		return False

def bruteForce(n, m):
	list = []
	for i in range(1,m):
		list.append(n/m)
	while(not checkAnswer(n,list)):
		for i in range(0, len(list)):
			if sum(list) > n:
				list[i] = list[i] - 1
			if sum(list) < n:
				list[i] = list[i] + 1
			if sum(list) == n:
				break
	print(list)
