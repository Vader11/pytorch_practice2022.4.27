import torch

my_tensor_a = torch.rand(3, 25, 25)
my_tensor_b = torch.rand(3, 25, 25)

my_tensor_01 = torch.cat([my_tensor_a, my_tensor_b], dim=0)
print(my_tensor_01.shape)

my_tensor_02 = torch.stack([my_tensor_a, my_tensor_b], dim=0)
print(my_tensor_02.shape)

# my_tensor_03, my_tensor_04 = torch.split(my_tensor_01, [2, 4], dim=0)
my_tensor_03, my_tensor_04 = my_tensor_01.split([2, 4], dim=0)
print(my_tensor_03.shape, my_tensor_04.shape)

my_tensor_05, my_tensor_06, my_tensor_07 = my_tensor_01.split(2, dim=0)
print(my_tensor_05.shape, my_tensor_06.shape, my_tensor_07.shape, )

my_tensor_08, my_tensor_09 = my_tensor_01.chunk(2, dim=0)
print(my_tensor_08.shape, my_tensor_09.shape)
