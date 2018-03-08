from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
from sklearn import datasets
wine_dataset = datasets.load_wine()
p = wine_dataset.data[:,:2]
q = wine_dataset.target
h=0.3
p_min, p_max = p[:, 0].min() - 1, p[:, 0].max() + 1
q_min, q_max = p[:, 1].min() - 1, p[:, 1].max() + 1
pp, qq = np.meshgrid(np.arange(p_min, p_max, h),np.arange(q_min, q_max, h))     #here we are generating all the grid points

p_train,p_test,q_train,q_test=train_test_split(p,q,test_size=0.2)   # As mentioned, 20% testing data
model_name = svm.SVC()

rbf_predic = model_name.set_params(kernel='rbf').fit(p_train, q_train).predict(p_test)

linea_predic = model_name.set_params(kernel='linear').fit(p_train, q_train).predict(p_test)

LinearAccuracy = metrics.accuracy_score(q_test,linea_predic)
print('the linear kernal accuracy is :',LinearAccuracy)
RbfAccuracy = metrics.accuracy_score(q_test,rbf_predic)
print('the rbf kernal accuracy is:',RbfAccuracy)
