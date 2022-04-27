import numpy as np
import torch

my_numpy = np.ones(5)
print(my_numpy, type(my_numpy), my_numpy.shape)

my_tensor = torch.from_numpy(my_numpy)
print(my_tensor, type(my_tensor), my_tensor.shape)
