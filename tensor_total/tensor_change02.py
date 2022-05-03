import torch

my_tensor = torch.randn(4, 7, 7, 3)
print(my_tensor.shape)

my_tensor01 = my_tensor.transpose(1, 3)
print(my_tensor01.shape)

my_tensor02 = my_tensor.permute(0, 3, 2, 1)
print(my_tensor02.shape)
