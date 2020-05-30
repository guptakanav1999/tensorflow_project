import os 
def updating_epoch():
	file1=open("epoch.txt","r")
	line1=file1.readline()
	arr=line1.split('=')
	a_final=int(arr[1])+1
	file1.close()

	file1=open("epoch.txt","w")
	file1.write("epoch="+str(a_final))
	file1.close()

def addingNeurons():
	f= open("project.py","r+")
	file = open("project1.py","w+")
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
	
	os.remove("project.py")
	os.rename(r'project1.py',r'project.py')

def main():
	updating_epoch()
	addingNeurons()

if __name__=="__main__":
	main()


