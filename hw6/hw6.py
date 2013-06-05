import math

# h[] is a list of classifiers. -- we should be able 
# to use each h[t] to classify an email x: h[t](x)

#errOft = error of h[t] on distribution Dt
def errOft(ht):	
	return

#alpha is a measure of weight on classifier h[t]
def alphaOft(t): 	
	return .5 * log((1 - errOft(h[t])) / errOf(h[t]))

def final_classifier(x):
	sum = 0
	for t in range(1, T):
		sum = sum + alphaOft(t)*h[t](x)
	
	if sum < 0:
		return -1
	return 1


f = open("hw6train.txt", "r")
training_data = []
line = f.readline()
while (line):
	training_data.append(line.split())
	line = f.readline()

