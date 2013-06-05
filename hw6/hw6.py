import math

# h[] is a list of classifiers. -- we should be able 
# to use each h[t] to classify an email x: h[t](x)

#errOft = error of h[t] on distribution D
#is the distribution training_data?
def errOft(h, D):	
	mistakes = 0
	for t in D:
		if h(t) is not D[t][-1] : #D[t][-1] is the actual label of x 
								  #(last element in email vector)
			mistakes = mistakes + 1
	return mistakes/len(D)

#alpha is a measure of weight on classifier h[t]
def alphaOft(t, D): 	
	return .5 * log((1 - errOft(h[t], D)) / errOf(h[t], D))

#returns result of classifying example x with classifier t
def h(t, x):

	return

def final_classifier(x):
	sum = 0
	for t in range(1, T):
		sum = sum + alphaOft(t)*h(t, x)
	
	if sum < 0:
		return -1
	return 1


f = open("hw6train.txt", "r")
training_data = []
line = f.readline()
while (line):
	training_data.append(line.split())
	line = f.readline()

