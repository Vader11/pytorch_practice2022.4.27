import torch

my_tensor = torch.randn(3, 4, 5)
print(my_tensor.shape)

my_tensor01 = my_tensor.unsqueeze(0)
print(my_tensor01.shape)

my_tensor02 = my_tensor.unsqueeze(2)
print(my_tensor02.shape)

my_tensor_b = torch.randn(1, 2, 3, 1, 1)
print(my_tensor_b.shape)

my_tensor03 = my_tensor_b.squeeze(0)
print(my_tensor03.shape)

my_tensor04 = my_tensor_b.squeeze()
print(my_tensor04.shape)
