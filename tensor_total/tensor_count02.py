import torch

my_tensor_a = torch.rand(2, 3)
my_tensor_b = torch.rand((3, 5))
print(my_tensor_a.shape)

my_tensor01 = my_tensor_a.t()
print(my_tensor01.shape)

my_tensor02 = my_tensor_a @ my_tensor_b
print(my_tensor02.shape)
my_tensor02 = torch.mm(my_tensor_a, my_tensor_b)
print(my_tensor02.shape)
my_tensor02 = torch.matmul(my_tensor_a, my_tensor_b)
print(my_tensor02.shape)
