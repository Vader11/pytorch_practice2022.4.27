import torch
import numpy

my_tensor = torch.ones(5)
print(my_tensor, type(my_tensor), my_tensor.shape)

my_numpy = my_tensor.numpy()
print(my_numpy, type(my_numpy), my_numpy.shape)


