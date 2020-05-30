import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os
import sys,getopt
def train(epoch):
	img_rows, img_cols = 28, 28
	num_classes = 10
	batch_size = 16
	(x_train, y_train), (x_test, y_test) = mnist.load_data()
	x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
	x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
	input_shape = (img_rows, img_cols, 1)
	x_train = x_train.astype('float32')
	x_test = x_test.astype('float32')
	x_train /= 255
	x_test /= 255
	y_train = keras.utils.to_categorical(y_train, num_classes)
	y_test = keras.utils.to_categorical(y_test, num_classes)
	model = Sequential()
	model.add(Conv2D(16, kernel_size=(3, 3),
                     activation='relu',
                     input_shape=input_shape))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(num_classes, activation='softmax'))
	model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])
	model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epoch,
              verbose=1,
              validation_data=(x_test, y_test))
	accuracy = model.evaluate(x_test, y_test, verbose=0)
	accuracy = accuracy[1]*100
	# storing accuracy
	os.system("sudo touch /code/accuracy.txt")
	os.system("echo {} > /code/accuracy.txt".format(accuracy))
	# saving the model to send to the client
	model.save('/code/model.h5')

def main(argv):
	epoch=''
	try:
		opts, args = getopt.getopt(argv,"e:",["epoch="])
		print("opts"+str(opts))
	except getopt.GetoptError:
		print('project.py -e '+ epoch )
		sys.exit(2)
	for opt, arg in opts:
		print("opt "+str(opt))
		print("arg=="+str(arg))
		if opt in ("-e", "--epoch"):
			epoch = arg
	print('epoch is '+ epoch)
	if(epoch==''):
		print('epoch is null')
		sys.exit(2) 

    train(epoch)

if __name__ == "__main__":
   main(sys.argv[1:])
