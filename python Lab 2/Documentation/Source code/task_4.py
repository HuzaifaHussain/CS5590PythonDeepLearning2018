
import numpy as np                #  import numpy
x = np.random.randint(0,21,11) # this indicates (low, high, size(int or tuple of ints))
print(x)
print('\nthe most frequent item in the list is:', np.bincount(x).argmax()) #counting most repeated number from list 'x'
