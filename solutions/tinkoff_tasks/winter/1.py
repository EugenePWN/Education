t = int(input())
l = sorted('tinkoff')

for i in range(t):
	word = input()
	if sorted(word.lower()) == l:
		print('Yes')
	else:
		print('No')