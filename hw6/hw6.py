f = open("hw6train.txt", r)
training_data = []
line = f.readline()
while (line):
	training_data.add(line.split())
	line = f.readline()

