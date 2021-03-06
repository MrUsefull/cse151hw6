import math


def errOft(t, plusminus, data):	
	mistakes = 0
	for email in data:
		# email[-1] is the actual label of this email;
		# h(t,email,plusminus) is the result this classifier 
		#	returns for this email
		if (h(t, email, plusminus) * int(email[-1])) < 0: 
			mistakes = mistakes + 1
	return float(mistakes)/len(data)

def alphaOft(t, plusminus, data): 
	error = errOft(t, plusminus, data)
	return .5 * math.log((1 - error) / error)

def fill_in_D_of_tplus1(D, t, data, plusminus):
	# D is the 2-dimensional D matrix
	# t is the word we are considering
	# data is the set of emails we are considering
	# i is the email in set data that we are considering
	# data[i][-1] is the actual label of the email we are considering
	# h(t, i, plusminus) is the predicted label
	for i in range (0,len(D)-1):
		zt = z(D, t, i, data, plusminus)
		D[t+1][i] = (D[t][i] * math.e ** (-1*alphaOft(t, plusminus, data)*int(data[i][-1])*h(t, data[i], plusminus))) / zt
	

#if h+ classifier: returns 1 if word t is contained in email x; -1 otherwise.
#if h- classifier: returns -1 if word t is contained in email x; 1 otherwise.
def h(t, x, plusminus):
	res = 0;
	if x[t] == 1:
		res = 1
	else:
		res = -1
	
	if plusminus == 1:
		return res
	else:
		return -res

# TODO: revise
def z(D, t, i, data, plusminus):
	total = 0
	for i in range(0, len(D[t])):
		total = total + D[t][i] * math.e ** (alphaOft(t, plusminus, data) * int(data[i][-1])*h(t, data[i], plusminus))
		print "alpha:"+str(alphaOft(t, plusminus, data))
		print "h*l:"+str(int(data[i][-1])*h(t, data[i], plusminus))
	return total

#TODO: revise
def final_classifier(x):
	sum = 0
	for t in range(1, len(h)):
		sum = sum + alphaOft(t, plusminus, data)*h(t, x, plusminus)
	
	if sum < 0:
		return -1
	return 1


f = open("hw6train.txt", "r")
training_data = []
line = f.readline()
while (line):
	training_data.append(line.split())
	line = f.readline()

f = open("hw6test.txt", "r")
test_data = []
line = f.readline()
while (line):
	test_data.append(line.split())
	line = f.readline()


#training data
T = int(raw_input("Number of passes (training): "))

#initialize D
D = []
a = []
b = []
for i in range(0,len(training_data)-1):
	a.append(float(1)/len(training_data))
D.append(a)
D.append(b)

#fill in the rest of D
t = 0
while t < T:
	fill_in_D_of_tplus1(D, t, training_data, 1)
	t = t + 1
	fill_in_D_of_tplus1(D, t, training_data, -1)
	t = t + 1
print D

