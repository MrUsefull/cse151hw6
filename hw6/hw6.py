import math

def errOft(t):
	
	return

def alphaOft(t): 
	
	return .5 * log((1 - errOft(t)) / errOf(t))

f = open("hw6train.txt", "r")
training_data = []
line = f.readline()
while (line):
	training_data.append(line.split())
	line = f.readline()

