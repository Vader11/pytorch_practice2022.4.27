import torch

my_tensor = torch.randn(3, 4, 5, 2)
print(my_tensor.shape)

my_tensor01 = my_tensor.view(3, 4, 5 * 2)
print(my_tensor01.shape)

my_tensor02 = my_tensor.view(4, 3 * 5 * 2)
print(my_tensor02.shape)

my_tensor03 = my_tensor.reshape(5, 2 * 3 * 4)
print(my_tensor03.shape)
