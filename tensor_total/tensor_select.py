import torch

my_tensor = torch.randn(4, 3, 4, 5)
print(my_tensor.shape)

my_select01 = my_tensor[:2]
my_select02 = my_tensor[:2, :1]
my_select03 = my_tensor[:2, -1:, ...]

print(my_select01.shape, my_select02.shape, my_select03.shape)

my_select04 = my_tensor.index_select(0, torch.tensor([0, 1, 3]))
my_select05 = my_tensor.index_select(0, torch.arange(1))
print(my_select04.shape, my_select04.shape)
print(my_select05.shape, my_select05.shape)

my_tensor_b = torch.tensor([[1, 2, 3], [3, 2, 6]])
my_select06 = torch.take(my_tensor_b, torch.tensor([2, 4, 3]))
print(my_tensor_b, my_select06)
