import os 
def reading_accuracy():
	file1=open("/root/devops/accuracy.txt","r")
	line1=file1.readline()
	accuracy=float(line1)
	file1.close()
	return accuracy

def updating_epoch():
	file1=open("/root/devops/epoch.txt","r")
	line1=file1.readline()
	arr=line1.split('=')
	a_final=int(arr[1])+1
	file1.close()

	file1=open("/root/devops/epoch.txt","w")
	file1.write("epoch="+str(a_final))
	file1.close()
	return a_final

def addingNeurons():
	f= open("/root/devops/project.py","r+")
	file = open("/root/devops/project1.py","w+")
	counter = False
	while True: 
		line = f.readline()
		var = "model.add(Dense(128, activation='relu'))"
		if(counter and not(var in line)):
			file.write(var)
			file.write("\n")
			counter = False
		if(var in line):
			counter = True
		
		file.write(line)
		if not line: 
			break
	f.close()
	file.close()
	
	os.remove("/root/devops/project.py")
	os.rename(r'/root/devops/project1.py',r'/root/devops/project.py')

def main():
	accuracy = reading_accuracy()
	while(accuracy < 98.0):
		epoch = updating_epoch()
		addingNeurons()
		os.system("project.py -e"+ str(epoch))
		accuracy = reading_accuracy()

if __name__=="__main__":
	main()


