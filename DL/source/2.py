import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
Required_data = np.loadtxt('iris.txt', skiprows=1)

X_DataRequired = Required_data[:,:2]
Y_DataRequired = Required_data[:,2:]
y = tf.placeholder(tf.float32, [None, 1])
x = tf.placeholder(tf.float32, [None, 2]) #here we're making placeholders
weight = tf.Variable(tf.zeros([2, 1]))
biasing = tf.Variable([0.0])
FigureObtained = tf.matmul(x, weight) + biasing
loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=FigureObtained)
loss = tf.reduce_mean(loss)
predict_op  = tf.greater_equal(FigureObtained, tf.zeros_like(FigureObtained))
correct_op  = tf.equal(tf.cast(predict_op, tf.float32), y)
accuracy_op = tf.reduce_mean(tf.cast(correct_op, tf.float32))
RateofLearning = 0.01
EpochCount    = 100
Optimising = tf.train.GradientDescentOptimizer(RateofLearning)
trainingOperation  = Optimising.minimize(loss)
CurrentSession = tf.Session()
CurrentSession.run(tf.global_variables_initializer())
writer = tf.summary.FileWriter('./graphs/linear_reg', CurrentSession.graph)
np.random.seed(0)

for epoch in range(EpochCount):
    idx = np.random.permutation(Required_data.shape[0])
    for i in idx:
        Dictionary = {x: X_DataRequired[i:i+1], y: Y_DataRequired[i:i+1]}
        CurrentSession.run(trainingOperation, Dictionary)

    if (epoch+1) % 10 == 0:
        Dictionary = {x: X_DataRequired, y: Y_DataRequired}
        accuracy = CurrentSession.run(accuracy_op, Dictionary)
        print("After {} epochs, accuracy = {}".format(epoch+1, accuracy))

writer.close()
Weight_val, biasing_val = CurrentSession.run([weight, biasing])
Weight_val = Weight_val[:,0]
biasing_val = biasing_val[0]
print("biasing =", biasing_val)
print("weight =", Weight_val)


def predict(x_):
    return 1 * CurrentSession.run(predict_op, {x: x_})

labels = predict(X_DataRequired)[:,0]

idx_0, = np.where(labels == 0) #making indices
idx_1, = np.where(labels == 1)

plt.plot(X_DataRequired[idx_0,0], X_DataRequired[idx_0,1], 'bo', label='versicolor')
plt.plot(X_DataRequired[idx_1,0], X_DataRequired[idx_1,1], 'ro', label='virginica')


x_sep = np.linspace(X_DataRequired[:,0].min(), X_DataRequired[:,0].max())
y_sep = (-biasing_val - Weight_val[0]*x_sep) / Weight_val[1]
plt.plot(x_sep, y_sep, 'm', label="Regression Line")
plt.legend()

plt.xlabel(" = Sepal length =  ")
plt.ylabel(" = Petal legnth = ")

plt.show()