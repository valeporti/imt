import numpy as np
import matplotlib.pyplot as plt




class Neural_Network():
	def __init__(self, inputSize, hiddenSize, outputSize, learning_rate):
		#parameters
		self.inputSize = inputSize
		self.outputSize = outputSize
		self.hiddenSize = hiddenSize
		self.learning_rate = learning_rate

		#add the bias as a neuron always set to 1
		self.inputSize = self.inputSize + 1
		self.hiddenSize = self.hiddenSize + 1

		#weights
		# weight matrix from input to hidden layer
		self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
		#self.W1 = np.array(([.1, .2, .3, .4], [.2, .4, .6, .8], [.3, .6, .9, 0]), dtype=float)
		#self.W1 = 0.3 * np.ones((self.inputSize, self.hiddenSize));
		# weight matrix from hidden to output layer
		self.W2 = np.random.randn(self.hiddenSize, self.outputSize)
		#self.W2 = 0.5 * np.ones((self.hiddenSize, self.outputSize));

	def feedforward(self, X):
		# forward propagation through our network

		# add the bias to the first input neuron
		bias=np.ones((np.shape(X)[0],1))
		X_bias = np.concatenate((bias, X), axis=1)


		# compute output for hidden layer
		# dot product of X (input) and weight matrix from input to hidden layer
		self.h_pot = np.dot(X_bias, self.W1)
		# activation function
		self.h_out = self.activation_function(self.h_pot)

		# set to 1 the bias neuron on hidden layer
		self.h_out[:,0] = np.ones(np.shape(self.h_out)[0]);

		# activation function
		# dot product of hidden layer output (out_h) and weight matrix from hidden to output layer
		self.o_pot = np.dot(self.h_out, self.W2)
		# activation function
		self.o_out = self.activation_function(self.o_pot)
		return self.o_out

	def activation_function(self, s):
		# activation function
		return 1/(1+np.exp(-s))

	def activation_function_prime(self, s):
		#derivative of sigmoid
		prime = self.activation_function(s)
		return prime * (1 - prime)
	
	def backward(self, X, y, output):
		# backward propagate through the network
		# error in output
		self.o_error = y - output
		# applying derivative of activation function to error
		self.o_delta = self.o_error * self.activation_function_prime(output)
		# h_error: how much our hidden layer weights contributed to output error
		self.h_error = self.o_delta.dot(self.W2.T)
		# applying derivative of activation function  to hidden error
		self.h_delta = self.h_error*self.activation_function_prime(self.h_out)


		bias=np.ones((np.shape(X)[0],1))
		input_layer = np.concatenate((bias, X), axis=1)
		# adjusting first set (input --> hidden) weights
		self.W1 += input_layer.T.dot(self.h_delta) * self.learning_rate
		# adjusting second set (hidden --> output) weights
		self.W2 += self.h_out.T.dot(self.o_delta) * self.learning_rate


	def train (self, X, y):
		output = self.feedforward(X)
		self.backward(X, y, output)






import pandas as pd
#read data
iris = pd.read_csv('iris.csv')

#Create numeric classes for species (0,1,2) 
iris.loc[iris['species']=='virginica','species']=0
iris.loc[iris['species']=='versicolor','species']=1
iris.loc[iris['species']=='setosa','species'] = 2

data = np.array(iris)

# stuffle data
np.random.shuffle(data)

# split data on train and test
train_percent = 0.9
size_of_learn_sample = int(len(data)*train_percent)

X_train = data[:size_of_learn_sample,:4]
y_train = data[:size_of_learn_sample,4]

X_test = data[size_of_learn_sample:,:4]
y_test = data[size_of_learn_sample:,4]



# normalization
X = X_train/np.amax(X_train, axis=0)
size_y = np.shape(y_train)[0]
y = y_train.reshape(size_y,1)/2


Xt = X_test/np.amax(X_test, axis=0)
size_y = np.shape(y_test)[0]
yt = y_test.reshape(size_y,1)/2


epoch = 322
plot_error = np.zeros(epoch)

# initialization
NN = Neural_Network(4,30,1,0.01)

# trains the NN <epoch>> times
for i in range(epoch):
	predicted_output = NN.feedforward(X)
	# mean sum squared loss
	output_error = np.mean(np.square(y - NN.feedforward(X)))
	plot_error[i] = output_error

#	print("Input: \n" + str(X))
#	print("Actual Output: \n" + str(y))
#	print("Predicted Output: \n" + str(predicted_output))
#	print("Loss: \n" + str(output_error) )
#	print("\n")

	NN.train(X, y)

plt.plot(plot_error)
plt.show()

test_error = np.mean(np.square(yt - NN.feedforward(Xt)))
print(test_error)

#clearPredicted = NN.feedforward(xPredicted)